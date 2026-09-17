import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js';
import { z } from 'zod';
import { promises as fs } from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
// Import necessary functions from dbUtils
import {
    readDb,
    writeDb,
    storeMessage, // Use the centralized message storing function
    getAllAgents, // Needed for broadcast
    DbData,       // Import types if needed
    Message,
    Thread
} from '../dbUtils.js';

// Determine the directory of the current module
const __filename = fileURLToPath(import.meta.url);
const uploadsDir = path.resolve(path.dirname(__filename), '../../uploads'); // Define uploads directory

// Ensure uploads directory exists
async function ensureUploadsDir() {
    try {
        await fs.access(uploadsDir);
    } catch (error) {
        console.log('Uploads directory not found, creating it...');
        await fs.mkdir(uploadsDir, { recursive: true });
    }
}

/**
 * Register communication tools with the MCP server.
 * These tools enable agents to exchange information, coordinate actions, and share files within the team.
 */
export function registerCommunicationTools(server: McpServer) {

  // Tool for sending a message either directly to another agent (using recipient_id) or to a specific discussion thread (using thread_id).
  server.tool(
    'send_message',
    {
      sender_id: z.string().describe("Your unique Agent ID."),
      recipient_id: z.string().optional().describe("The unique Agent ID of the recipient (for direct 1-to-1 messages). Do not use if sending to a thread."),
      thread_id: z.string().optional().describe("The ID of the thread to post the message in (for group discussions). Do not use if sending a direct message."),
      content: z.string().describe("The textual content of the message."),
      urgent: z.boolean().default(false).describe("Set to true if this message requires immediate attention.")
    },
    async ({ sender_id, recipient_id, thread_id, content, urgent }) => {
      if (!recipient_id && !thread_id) {
        throw new Error("Either recipient_id or thread_id must be provided.");
      }
      if (recipient_id && thread_id) {
        throw new Error("Cannot provide both recipient_id and thread_id.");
      }

      const newMessage = await storeMessage({
          sender_id,
          recipient_id, 
          thread_id,    
          content,
          urgent
      });

      return {
        content: [{ type: 'text', text: `Message ${newMessage.id} sent successfully.` }],
        data: newMessage
      };
    }
  );

  // Tool for retrieving messages relevant to the calling agent.
  server.tool(
    'get_messages',
    {
      agent_id: z.string().describe("Your unique Agent ID."),
      thread_id: z.string().optional().describe("Optional: Retrieve messages only from this specific thread ID."),
      limit: z.number().default(10).describe("Maximum number of messages to retrieve (most recent first)."),
      since: z.string().optional().describe("Optional: Retrieve messages created after this ISO 8601 timestamp (e.g., '2025-03-30T12:00:00Z').")
    },
    async ({ agent_id, thread_id, limit, since }) => {
      const db = await readDb(); 
      // db.threads is now an array
      const agentThreads = db.threads.filter(t => t.participants.includes(agent_id)).map(t => t.id);

      let relevantMessages = db.messages.filter(msg => {
        if (since && new Date(msg.timestamp) < new Date(since)) return false;
        if (msg.recipient_id === agent_id) return !thread_id || !msg.thread_id;
        if (msg.recipient_ids?.includes(agent_id)) return !thread_id || !msg.thread_id; 
        if (thread_id && msg.thread_id === thread_id) {
            // Find thread in the array
            const thread = db.threads.find(t => t.id === thread_id); 
            return thread && thread.participants.includes(agent_id);
        }
        if (!thread_id && msg.thread_id && agentThreads.includes(msg.thread_id)) return true;
        return false;
      });

      relevantMessages.sort((a, b) => new Date(b.timestamp).getTime() - new Date(a.timestamp).getTime());
      const limitedMessages = relevantMessages.slice(0, limit);

      const unreadForAgent = db.unread[agent_id] || [];
      const retrievedMessageIds = new Set(limitedMessages.map(m => m.id));
      const updatedUnread = unreadForAgent.filter(unreadId => !retrievedMessageIds.has(unreadId));

      if (updatedUnread.length !== unreadForAgent.length) {
          db.unread[agent_id] = updatedUnread;
          await writeDb(db); 
      }

      return {
        content: [{ type: 'text', text: JSON.stringify(limitedMessages, null, 2) }],
        data: { count: limitedMessages.length, messages: limitedMessages }
      };
    }
  );

  // Tool for creating a new communication thread for focused discussions.
  server.tool(
    'create_thread',
    {
      creator_id: z.string().describe("Your unique Agent ID."),
      title: z.string().describe("A concise and descriptive title for the discussion thread."),
      participants: z.array(z.string()).describe("List of unique Agent IDs of all initial participants (including yourself)."),
      initial_message: z.string().optional().describe("Optional first message to post in the newly created thread.")
    },
    async ({ creator_id, title, participants, initial_message }) => {
      const db = await readDb(); 
      const thread_id = `thread-${Date.now()}-${Math.random().toString(36).substring(2, 7)}`;

      if (!participants.includes(creator_id)) {
          participants.push(creator_id); 
      }

      const newThread: Thread = {
          id: thread_id,
          title,
          creator_id: creator_id, // Set the creator_id
          participants,
          created_at: new Date().toISOString()
      };
      // Push to the array instead of assigning by key
      db.threads.push(newThread); 

      let firstMessage: Message | null = null;
      if (initial_message) {
          firstMessage = await storeMessage({
              sender_id: creator_id,
              thread_id: thread_id,
              content: initial_message,
              urgent: false 
          });
      } else {
         await writeDb(db); 
      }

      return {
        content: [{ type: 'text', text: `Thread "${title}" (${thread_id}) created successfully.` }],
        data: { thread: newThread, initial_message_id: firstMessage?.id }
      };
    }
  );

  // Tool for an agent to join an existing communication thread.
  server.tool(
    'join_thread',
    {
      thread_id: z.string().describe("The unique ID of the thread you want to join."),
      agent_id: z.string().describe("Your unique Agent ID.")
    },
    async ({ thread_id, agent_id }) => {
      const db = await readDb(); 
      // Find thread in the array
      const thread = db.threads.find(t => t.id === thread_id); 

      if (!thread) {
        throw new Error(`Thread ${thread_id} not found.`);
      }

      if (!thread.participants.includes(agent_id)) {
        thread.participants.push(agent_id);
        await writeDb(db); 
        return {
          content: [{ type: 'text', text: `Agent ${agent_id} joined thread "${thread.title}" (${thread_id}).` }],
          data: { thread_id, agent_id, status: 'joined' }
        };
      } else {
        return {
          content: [{ type: 'text', text: `Agent ${agent_id} is already a participant in thread ${thread_id}.` }],
          data: { thread_id, agent_id, status: 'already_participant' }
        };
      }
    }
  );

  // Tool for sending the same message to multiple specific agents simultaneously.
  server.tool(
    'broadcast_message',
    {
      sender_id: z.string().describe("Your unique Agent ID."),
      recipient_ids: z.array(z.string()).min(1).describe("List of unique Agent IDs of the recipients."),
      content: z.string().describe("The textual content of the message to send to all recipients."),
      urgent: z.boolean().default(false).describe("Set to true if this message requires immediate attention from all recipients.")
    },
    async ({ sender_id, recipient_ids, content, urgent }) => {
        const newMessage = await storeMessage({
            sender_id,
            recipient_ids,
            content,
            urgent
        });

        return {
            content: [{ type: 'text', text: `Message ${newMessage.id} broadcasted to ${recipient_ids.length} agents.` }],
            data: newMessage
        };
    }
  );

  // Tool for an agent to quickly check the number of unread messages waiting for them.
  server.tool(
    'check_new_messages',
    {
      agent_id: z.string().describe("Your unique Agent ID.")
    },
    async ({ agent_id }) => {
      const db = await readDb(); 
      const unreadCount = db.unread[agent_id]?.length || 0;
      return {
        content: [{ type: 'text', text: `Agent ${agent_id} has ${unreadCount} unread message(s).` }],
        data: { agent_id, unread_count: unreadCount }
      };
    }
  );

  // Tool for securely transferring a file.
  server.tool(
      'transfer_file',
      {
          sender_id: z.string().describe("Your unique Agent ID."),
          recipient_id: z.string().describe("The unique Agent ID of the recipient."),
          source_path: z.string().describe("The absolute path to the file on your local filesystem that you want to send."),
          destination_filename: z.string().optional().describe("Optional: A specific filename for the file when the recipient accesses it (defaults to the original filename)."),
          description: z.string().optional().describe("Optional text description of the file being sent.")
      },
      async ({ sender_id, recipient_id, source_path, destination_filename, description }) => {
          await ensureUploadsDir(); 

          const filename = destination_filename || path.basename(source_path);
          const safeFilename = path.basename(filename);
          const destinationPath = path.join(uploadsDir, `${recipient_id}-${Date.now()}-${safeFilename}`);

          try {
              await fs.copyFile(source_path, destinationPath);
              console.log(`File transferred from ${source_path} to ${destinationPath}`);

              const messageContent = `File Transfer from ${sender_id}:\nFile: ${safeFilename}\n${description ? `Description: ${description}\n` : ''}Stored at server path: ${destinationPath}`; 

              const notificationMessage = await storeMessage({
                  sender_id: sender_id,
                  recipient_id: recipient_id,
                  content: messageContent,
                  urgent: false 
              });

              return {
                  content: [{ type: 'text', text: `File "${safeFilename}" transferred successfully to ${recipient_id}. Notification message ${notificationMessage.id} sent.` }],
                  data: {
                      sender_id,
                      recipient_id,
                      filename: safeFilename,
                      server_path: destinationPath, 
                      description,
                      notification_message_id: notificationMessage.id,
                      timestamp: new Date().toISOString()
                  }
              };
          } catch (error: any) {
              console.error(`File transfer failed: ${error.message}`);
              throw new Error(`Failed to transfer file: ${error.message}`);
          }
      }
  );

  // --- NEW THREAD MANAGEMENT TOOLS ---

  // Tool to get details about a specific thread.
  server.tool(
      'get_thread_details',
      {
          thread_id: z.string().describe("The unique ID of the thread to retrieve details for.")
      },
      async ({ thread_id }) => {
          const db = await readDb();
          // Find thread in the array
          const thread = db.threads.find(t => t.id === thread_id); 

          if (!thread) {
              throw new Error(`Thread ${thread_id} not found.`);
          }

          // Optionally fetch recent messages for context? For now, just metadata.
          const threadDetails = {
              id: thread.id,
              title: thread.title,
              creator_id: thread.creator_id, // Assuming creator_id exists on Thread interface
              participants: thread.participants,
              created_at: thread.created_at
          };

          return {
              content: [{ type: 'text', text: JSON.stringify(threadDetails, null, 2) }],
              data: threadDetails
          };
      }
  );

  // Tool to add a participant to an existing thread.
  server.tool(
      'add_participant_to_thread',
      {
          thread_id: z.string().describe("The unique ID of the thread."),
          agent_id_to_add: z.string().describe("The unique Agent ID of the agent to add."),
          inviting_agent_id: z.string().describe("Your unique Agent ID (must be a current participant).") // Authorization check
      },
      async ({ thread_id, agent_id_to_add, inviting_agent_id }) => {
          const db = await readDb();
          // Find thread in the array
          const thread = db.threads.find(t => t.id === thread_id); 

          if (!thread) {
              throw new Error(`Thread ${thread_id} not found.`);
          }
          // Basic authorization: check if inviter is a participant
          if (!thread.participants.includes(inviting_agent_id)) {
               throw new Error(`Agent ${inviting_agent_id} is not a participant of thread ${thread_id} and cannot add others.`);
          }
          // Check if agent is already added
          if (thread.participants.includes(agent_id_to_add)) {
              return {
                  content: [{ type: 'text', text: `Agent ${agent_id_to_add} is already in thread ${thread_id}.` }],
                  data: { thread_id, agent_id: agent_id_to_add, status: 'already_participant' }
              };
          }

          thread.participants.push(agent_id_to_add);
          // Optionally send a notification message to the thread/added agent
          await storeMessage({
              sender_id: inviting_agent_id, // Or a system ID
              thread_id: thread_id,
              content: `Agent ${inviting_agent_id} added ${agent_id_to_add} to the thread.`,
              urgent: false
          });
          await writeDb(db);

          return {
              content: [{ type: 'text', text: `Agent ${agent_id_to_add} added to thread ${thread_id}.` }],
              data: { thread_id, agent_id: agent_id_to_add, status: 'added' }
          };
      }
  );

  // Tool to remove a participant from an existing thread.
  server.tool(
      'remove_participant_from_thread',
      {
          thread_id: z.string().describe("The unique ID of the thread."),
          agent_id_to_remove: z.string().describe("The unique Agent ID of the agent to remove."),
          removing_agent_id: z.string().describe("Your unique Agent ID (must be the thread creator or the agent being removed).") // Authorization check
      },
      async ({ thread_id, agent_id_to_remove, removing_agent_id }) => {
          const db = await readDb();
          // Find thread in the array
          const thread = db.threads.find(t => t.id === thread_id); 

          if (!thread) {
              throw new Error(`Thread ${thread_id} not found.`);
          }
          // Basic authorization: check if remover is creator or the agent themselves
          if (removing_agent_id !== thread.creator_id && removing_agent_id !== agent_id_to_remove) {
               throw new Error(`Agent ${removing_agent_id} does not have permission to remove participants from thread ${thread_id}.`);
          }
          // Check if agent is actually a participant
          if (!thread.participants.includes(agent_id_to_remove)) {
              return {
                  content: [{ type: 'text', text: `Agent ${agent_id_to_remove} is not in thread ${thread_id}.` }],
                  data: { thread_id, agent_id: agent_id_to_remove, status
(Content truncated due to size limit. Use line ranges to read in chunks)