# Model Context Protocol (MCP) Implementation

This project implements the official Model Context Protocol (MCP) standard for cross-agent communication between various AI models including Claude, DeepSeek, OpenAI, and Gemini instances.

## Overview

The Model Context Protocol (MCP) is a standardized communication protocol designed to facilitate interactions between Large Language Model (LLM) applications and external services. This implementation focuses on enabling different AI models to communicate and collaborate effectively for better teamwork and problem solving.

## Features

- **Cross-Agent Communication**: Send and receive messages between different AI models
- **Multi-Model Collaboration**: Tools for task decomposition, assignment, and result merging
- **Model-Agnostic Design**: Support for Claude, DeepSeek, OpenAI, and Gemini models
- **Multiple Transport Mechanisms**: Support for both stdio and SSE transports
- **Collaboration Tools**: Task decomposition, subtask assignment, and result merging
- **Collaboration Prompts**: Structured prompts for effective multi-model collaboration
- **Agent Resources**: Information about available agents and their capabilities

## Project Structure

- `src/`: Source code for the MCP server
  - `index.ts`: Main server entry point
  - `tools/`: Tool implementations
    - `communication.ts`: Tools for agent-to-agent communication
    - `collaboration.ts`: Tools for multi-model collaboration
  - `resources/`: Resource implementations
    - `agents.ts`: Resources for agent information
  - `prompts/`: Prompt implementations
    - `collaboration.ts`: Prompts for multi-model collaboration
- `examples/`: Example client implementations
  - `claude-desktop-client.js`: Client for Claude Desktop
  - `roocode-cli-client.js`: Client for command-line instances
- `docs/`: Documentation
- `tests/`: Test files

## Installation

### Prerequisites

- Node.js 18 or later
- npm

### Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   npm install
   ```
3. Build the project:
   ```bash
   npm run build
   ```

## Usage

### Starting the Server

To start the server with stdio transport (for command-line integration):

```bash
npm start
```

To start the server with SSE transport (for web-based integration):

```bash
npm start sse
```

### Using the Claude Desktop Client

```bash
node examples/claude-desktop-client.js [client-id] [stdio|sse] [server-path] [server-url]
```

### Using the Roocode CLI Client

```bash
node examples/roocode-cli-client.js [client-id] [stdio|sse] [server-path] [server-url]
```

## Client Commands

Both clients support a variety of commands for cross-agent communication:

- `send <recipient> <message>`: Send a message to another agent
- `get-messages [thread-id]`: Get messages, optionally filtered by thread
- `create-thread <title> <participant1,participant2,...>`: Create a new thread
- `agents [model-type]`: List available agents, optionally filtered by model type
- `channels`: List available channels
  - `collaborate <title> <description> <participant1,participant2,...>`: Create a collaboration session

### Agent Status Management

Agents can manage and report their operational status using the following tools:

- **`register_agent`**: Registers an agent with the server, setting its initial status to `available`. Also used to update agent details.
- **`set_agent_status`**: Allows an agent to explicitly set its status to `available`, `working`, `idle`, `offline`, or `error`. Can include an `error_info` message if the status is `error`.
- **`report_status`**: Allows an agent to report its status along with details like the current task, plan summary, progress metric (if `working`), or error information (if `error`). This implicitly updates the agent's status and last heartbeat.
- **`get_agent_status`**: Retrieves the current status and other details (task, plan, etc.) of a specific agent.
- **`find_agents`**: Searches for agents based on criteria including their current status (using the new enum values), capabilities, role, group, and recent activity.
- **`deregister_agent`**: Removes an agent from the system.

The agent status is also reflected in the `/agents` resource and the Agent Dashboard web interface.

## Extending the Implementation

### Adding New Tools

To add a new tool, create a new function in an appropriate file in the `tools/` directory and register it with the server:

```typescript
server.tool(
  'tool_name',
  { 
    param1: z.string().describe('Parameter description'),
    param2: z.number().describe('Parameter description')
  },
  async ({ param1, param2 }) => {
    // Tool implementation
    return {
      content: [{ type: 'text', text: 'Result text' }],
      data: { /* Result data */ }
    };
  }
);
```

### Adding New Resources

To add a new resource, create a new function in an appropriate file in the `resources/` directory and register it with the server:

```typescript
server.resource(
  'resource_name',
  {
    query: z.object({
      param1: z.string().describe('Parameter description')
    })
  },
  async (query) => {
    // Resource implementation
    return {
      content: [{ type: 'text', text: 'Resource text' }],
      data: { /* Resource data */ }
    };
  }
);
```

### Adding New Prompts

To add a new prompt, create a new function in an appropriate file in the `prompts/` directory and register it with the server:

```typescript
server.prompt(
  'prompt_name',
  {
    title: 'Prompt Title',
    description: 'Prompt description',
    parameters: {
      param1: z.string().describe('Parameter description')
    }
  },
  ({ param1 }) => {
    // Prompt template
    return `Prompt text with ${param1}`;
  }
);
```

## License

This project is licensed under the ISC License.