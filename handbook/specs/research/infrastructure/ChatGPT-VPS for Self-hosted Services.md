# VPS for Self-hosted Services

**User:**   
**Created:** 4/1/2026 4:16:46  
**Updated:** 4/1/2026 4:53:47  
**Exported:** 4/20/2026 17:33:08  
**Link:** [https://chatgpt.com/c/69ccfe9c-4e4c-8332-820f-dc9df2726beb](https://chatgpt.com/c/69ccfe9c-4e4c-8332-820f-dc9df2726beb)  

## Prompt:
4/1/2026, 4:16:46 AM

Gemini
New chat
My stuff
Gems

Settings & help
Conversation with Gemini
You said
find me the cheapest\best 8core+ 64gb ram+ 500gb storage+ VPS

For hosting items like nextcloud, other self hsoted services, developer self hosted services and cpu based inference + project deployments and pg\neo4j\similar.
Gemini said
When you scale up to requirements like 64GB of RAM and 8+ cores, the line between a "high-end VPS" and a "budget dedicated server" begins to blur. Because your workloads include CPU-based inference and graph databases like Neo4j—both of which demand consistent, unshared CPU cycles and high IOPS—the underlying hardware architecture becomes just as important as the paper specs.

Here are the best options that balance absolute cost with the performance needed for heavy, self-hosted developer environments.

1. The Absolute Cheapest: Contabo (Cloud VPS 50)
If the primary goal is minimizing the monthly bill while strictly meeting the hardware requirements, Contabo is the undisputed price leader in the VPS market.

Specs: 16 vCPU, 64 GB RAM, 600 GB SSD (or 300 GB NVMe).

Price: ~$36 to $46 / month.

Location: They offer US West datacenters (Seattle/Los Angeles) for a small premium, which keeps latency extremely low if you are accessing it from the West Coast.

The Trade-off: Contabo achieves these prices through heavy overprovisioning. The vCPUs are shared. For Nextcloud, Postgres, and general project deployments, it will run perfectly fine. However, for CPU-based inference, you will likely experience "CPU steal" during peak hours, meaning inference times could be inconsistent.

2. The Performance King: Hetzner Server Auction (Bare Metal)
While technically not a VPS, at this spec tier, renting a budget bare-metal server is often cheaper and vastly superior for AI and database workloads. Hetzner auctions off their older dedicated servers at heavily discounted, unmetered rates.

Specs: You can consistently find configurations like an AMD Ryzen 5 or Intel Core i7 with 64GB ECC RAM and 2x 512GB NVMe SSDs.

Price: ~$35 to $50 / month (varies daily based on auction inventory).

The Trade-off: These auction servers are hosted in Europe (Germany/Finland). You will experience around 140ms of latency from the US West. However, because you get 100% dedicated physical CPU threads and unshared NVMe drives, your Neo4j queries and CPU inference tasks will execute significantly faster than on any budget VPS.

3. The Middle Ground: Hetzner Cloud (CCX43 - Dedicated vCPU)
If you want the flexibility of a cloud VPS, require US-based hosting for latency, but cannot compromise on inference performance, standard shared-vCPU plans from mainstream providers (like AWS, DO, or Vultr) will easily push $300+/month. Hetzner's Cloud offering in Oregon is the best bridge between enterprise performance and developer pricing.

Specs: 16 Dedicated vCPU (AMD EPYC), 64 GB RAM, 360 GB NVMe.

Price: ~$125 / month.

Location: Hillsboro, Oregon (US West).

The Trade-off: The base storage is slightly under your 500GB requirement, so you would need to attach a small, cheap block storage volume for bulk Nextcloud data. Because the vCPUs are dedicated, it behaves similarly to bare metal, ensuring your inference scripts don't stall out.

Recommendation on Architecture:
Given the mix of services, the Hetzner Bare Metal Auction offers the highest ceiling for developer tools. You can install a hypervisor like Proxmox on the bare metal machine, allowing you to carve it up into smaller, dedicated VMs—perhaps isolating Nextcloud on one VM, and giving the bulk of the CPU threads to an isolated inference and Neo4j environment.

You said
eval 50-100 options. budg 50$ a mo ideally 20. want the most perf for both tiers
Gemini said
Getting 64GB of RAM, 8+ cores, and 500GB of storage for $20 a month is practically impossible in the current standard market; that tier is entirely populated by heavily overprovisioned shared VPS plans where "CPU steal" will instantly choke your AI inference and graph database queries.

However, at the $50 tier, you cross the threshold from "shared cloud" into "budget bare metal," which is exactly where you want to be for demanding developer workloads. For deployments running Neo4j and CPU-based inference alongside Nextcloud, you need dedicated, unshared CPU cycles and high IOPS that standard VPS providers simply don't offer at this price point.

Here is the breakdown of the absolute best performance for your specific requirements across both budget tiers, prioritizing US West datacenters for optimal latency.

The $20 - $35 Tier: The High-Density VPS
At this price, you are forced to use shared vCPUs. This is fine for Nextcloud and standard developer services, but your inference scripts will experience inconsistent execution times during peak datacenter hours.

Contabo (Cloud VPS XL): ~$35 / month

Specs: 10 vCPU, 60 GB RAM, 1.6 TB SSD (or 800 GB NVMe).

The Reality: Contabo is the undisputed king of raw specs-per-dollar, and they have datacenters in Seattle and Los Angeles, offering excellent latency. However, their model relies on high-density virtualization. Your single-core performance will be lower, and IOPS can fluctuate. It will run everything you need, but the Neo4j queries and AI inference will not break any speed records.
+1

The $40 - $80 Tier: True Dedicated Performance
If you can push closer to $50, you should abandon VPS entirely and rent older, unmanaged bare-metal servers. This guarantees 100% dedicated hardware.

Hetzner Server Auction (Bare Metal): ~$40 - $50 / month

Specs: Typically Intel Core i7 (6th/7th Gen) or AMD Ryzen equivalents, 64 GB ECC RAM, 2x 512 GB NVMe SSDs.

The Reality: This is the highest absolute performance per dollar on the market. The CPU threads are yours alone, meaning inference times will be highly predictable. The catch is location: these are hosted in Germany or Finland. You will trade about 140ms of latency for enterprise-grade compute power.

OVHcloud Eco (Rise/Kimsufi lines): ~$70 - $80 / month

Specs: AMD Ryzen 5, 64 GB RAM, 2x 512 GB NVMe.

The Reality: If you cannot tolerate the European latency of Hetzner and need the server physically located in North America (they have West Coast availability), OVH's Eco line is the next best step. It stretches the budget, but it completely solves the "shared resources vs. latency" dilemma.

Deployment Strategy:
Given your stack, the most performant path is to grab a bare-metal machine (like the Hetzner auction server) and install a hypervisor like Proxmox. You can isolate Nextcloud and standard web services on one virtual machine, and dedicate the bulk of your hardware threads directly to a secondary VM tuned specifically for inference and Neo4j.

Show me the visualization

You said
85:14:27left
€38.70max. per month
€0.0620
per hour
CPU
Intel Xeon E5-1650V3
RAM
64 GB
Drives
2 x 2.0 TB Enterprise HDD
Location
#FSN1-DC12
InformationIPv4ECCiNIC
Details 
excl. VAT
General
Server AuctionID: 2842267
Traffic: unlimited
Information
4 x RAM 16384 MB DDR4 ECC reg.
2 x HDD SATA 2,0 TB Enterprise
NIC 1 Gbit - Intel I210
Support services
replacement of defective hardware
free email support
free phone support
Gemini said
Analysis of the Hetzner Xeon E5-1650V3 Auction Server
You found a classic Hetzner Server Auction machine (FSN1-DC12 is their Falkenstein, Germany datacenter). At €38.70 (roughly $42 USD), it absolutely nails your budget and gives you 100% dedicated hardware.

However, looking at your specific stack, this specific server is a hard pass. Here is the breakdown of why.

The Good
The Price & RAM: 64GB of DDR4 ECC memory for ~$42/mo is a steal. ECC RAM is a massive bonus for database integrity, particularly for Postgres and Neo4j.

Dedicated Resources: No hypervisor, no noisy neighbors. You get the whole box.

The Dealbreakers
The Drives (The Fatal Flaw): This server uses two 2.0 TB Enterprise HDDs (spinning rust). Graph databases like Neo4j are incredibly IOPS-heavy and require fast random read/write speeds. Running Neo4j on an HDD will result in severe bottlenecking and massive query latency. Furthermore, loading AI models from an HDD into memory for inference will be painfully slow. You absolutely need SSDs, and ideally NVMes, for this stack.

The CPU: The Xeon E5-1650 v3 is a workhorse, but it's a 6-core / 12-thread chip released back in 2014 (Haswell architecture). It technically misses your 8-core requirement, but more importantly, it lacks modern instruction sets. For the multi-agent Python setups and CPU inference you are spinning up, this older architecture will compute significantly slower than a modern desktop-grade chip.

Latency: FSN1 is in Germany. Routing that connection to Arizona is going to result in roughly 150ms to 160ms of latency. That is perfectly fine for background Nextcloud syncing or API calls, but typing in SSH sessions will feel noticeably "floaty."

The Verdict
Skip this one. The HDDs will crush your database performance, and the older CPU will drag out your inference times.

What to look for instead: Keep refreshing the Hetzner auction, but filter strictly for NVMe or SSD drives. You can frequently find machines in the €40 to €45 range with:

CPU: AMD Ryzen 5 3600 or Intel Core i7-8700 (much better single-thread performance for your developer environments).

RAM: 64 GB.

Drives: 2x 512 GB NVMe SSDs (perfect for your 500GB+ requirement and incredibly fast for Neo4j).

Are you expecting to store massive amounts of media or data on Nextcloud that would make you want to compromise on drive speed for sheer terabyte capacity, or is the priority strictly getting fast I/O for the databases and inference?

You said
23:19:15left
€42.70max. per month
€0.0684
per hour
CPU
Intel XEON E-2176G
RAM
64 GB
Drives
2 x 960 GB Datacenter SSD
Location
#HEL1-DC4
InformationIPv4ECCiNIC
Details 
excl. VAT
General
Server AuctionID: 2963504
Traffic: unlimited
Information
4 x RAM 16384 MB DDR4 ECC
2 x SSD U.2 NVMe 960 GB Datacenter
NIC 1 Gbit - Intel I219-LM
Support services
replacement of defective hardware
free email support
free phone support
Gemini said
The Verdict: Grab It Now.
This is exactly the kind of hidden gem you want to find in the Hetzner auction. At €42.70 (roughly $46 USD), this server easily clears your $50 budget while providing a massive leap in performance over both standard VPS options and the HDD-based server you found earlier.

Here is the breakdown of why this specific machine is a near-perfect fit for your stack.

The Breakdown
The MVP: 2x 960GB Datacenter U.2 NVMes
This is the star of the show. You aren't just getting NVMes; you are getting enterprise-grade U.2 Datacenter drives. Consumer SSDs often drop in speed under sustained read/writes, but datacenter drives maintain massive, consistent IOPS.

Impact: Neo4j graph traversals and heavy PostgreSQL queries will execute instantly. Loading your AI models into RAM for inference will take seconds. Setting these up in a RAID 1 array gives you a highly redundant, blazing-fast 1TB drive—double your 500GB requirement.

The CPU: Intel Xeon E-2176G
While it technically has 6 physical cores (12 threads) instead of your requested 8+, you should not let that deter you. This is a Coffee Lake architecture chip with a massive 4.7 GHz boost clock.

Impact: For single-threaded Python scripts, automated multi-agent loops, and web deployments, high clock speed often beats raw core count. You get 100% dedicated access to these 12 threads, meaning your inference times will be highly predictable and significantly faster than an 8-core shared VPS.

The RAM: 64 GB ECC
Hitting your 64GB requirement exactly, with the added benefit of Error-Correcting Code (ECC) memory. ECC is highly recommended for maintaining data integrity in Nextcloud and preventing silent corruption in your databases.

The Trade-off: Helsinki Latency
The only "catch" is the location: HEL1-DC4 is in Helsinki, Finland. Routing a connection from Arizona to Helsinki will result in roughly 160ms to 180ms of latency.

What this means for you: Typing in your terminal via SSH will have a slight, noticeable delay. Your Nextcloud web interface will take a fraction of a second longer to load initially.

Why it doesn't matter: Your backend multi-agent AI scripts, CPU inference jobs, and automated project deployments do not care about latency once they are running. The raw, dedicated compute power you are getting for $46 completely outweighs the minor annoyance of a higher SSH ping.

Bottom Line: For $46 a month, getting almost 2TB of datacenter NVMe storage, 64GB of ECC RAM, and a high-clock dedicated Xeon is an absolute steal for self-hosting.

If you manage to secure this server, are you planning to install a hypervisor like Proxmox to virtualize your Nextcloud and developer environments separately, or run everything bare-metal on a single Linux distribution?

You said
look on the web for altenratives
Gemini said
I scoured the market—including the major providers, the "low-end box" community favorites, and current budget bare-metal catalogs.

The reality of the current hosting market is that getting 64GB RAM, 8+ cores, and NVMe storage for under $50 forces you to pick two out of three: US Location, Dedicated Hardware, or The $50 Budget.

Here are the best alternatives to the Hetzner auction that approach your criteria, categorized by the trade-off you have to make.

1. The Best Middle-Ground: Dedicated VPS in Europe
If you want guaranteed, unshared CPU cores for inference but want to pay VPS prices, you should look at "Root Servers" (VDS) rather than standard shared VPS.

Netcup (Root Server - RS 4000 / RS 8000 G11)

Specs: 12 Dedicated AMD EPYC vCores, 48GB to 64GB RAM, 1.5TB to 2TB NVMe.

Price: ~$36 to $50 / month.

Location: Germany / Austria.

The Verdict: Netcup is Hetzner's main rival in Europe. Their "Root Servers" guarantee that you do not share CPU cycles. This is drastically better for your AI inference and Neo4j workloads than Contabo. However, you are still dealing with ~150ms latency from Arizona.

2. The US Bare-Metal Budget Market (Central US)
If you cannot tolerate European latency but need the raw power of bare metal for $50, you have to look at older enterprise liquidation datacenters in the Midwest.

NOCIX / Wholesale Internet

Specs: You can frequently configure a Dual Intel Xeon E5-2660v2 (20 Cores / 40 Threads total), 64GB to 128GB RAM, and a 500GB SSD or 1TB NVMe.

Price: ~$40 to $50 / month.

Location: Kansas City, Missouri.

The Verdict: Tempe to Kansas City is only about a 40-50ms ping, which is very snappy. You get a massive amount of older enterprise cores and huge RAM pools for dirt cheap. The single-core speed won't match a modern Ryzen, but for highly parallel multi-agent workloads and Neo4j, 40 dedicated threads will plow through tasks.

3. The Elusive "Unicorn": US West Bare Metal
If you strictly want US West (Los Angeles / Oregon), 64GB of RAM, and dedicated hardware, $50 is exceptionally tight.

OVHcloud Eco (Kimsufi / SoYouStart lines)

Specs: Intel Xeon E3 or older AMD Ryzen, 64GB RAM, 2x 512GB NVMes.

Price: ~$55 to $70 / month (when in stock).

Location: Hillsboro, Oregon (US West).

The Verdict: OVH operates a massive datacenter in Oregon. Their "Eco" line sells off older hardware. You have to stalk their availability page, as the $50-$60 64GB models sell out instantly. If you can stretch your budget by $10-$20, this is the only way to get a dedicated machine with NVMes physically located on the West Coast.

4. The Budget US West VPS Options (Heavy Compromise)
If you absolutely must stay under $40 and must be in the US West, you are stuck with shared resources.

HostHatch / RackNerd / CloudCone (Promo Hunting)

The Verdict: These providers operate out of Los Angeles and offer fantastic network routing. However, their standard pricing for 64GB RAM usually exceeds $60/mo. To get 64GB under $50, you have to wait for their cyclical promotions (Black Friday, New Years, Summer Sales). Even then, the CPU is heavily shared, meaning your AI inference will suffer from "noisy neighbor" syndrome.

Final Recommendation
If that Hetzner Intel Xeon E-2176G with 64GB RAM and U.2 NVMes is still available for $46, it remains the absolute best piece of hardware for your budget. The U.2 Datacenter NVMes will make Neo4j fly.

If you want to prioritize latency from Tempe and are willing to use slightly older hardware, look at a NOCIX Dual Xeon build in Kansas City for $40/mo.

You said
idc abt dedicated hw
Gemini said
You stopped this response
You said
resume
Gemini said
Dropping the dedicated hardware requirement completely changes the game. If you are okay with shared vCPUs, we can easily hit your specs, stay well under the $50 budget, and get the server hosted on the West Coast for ultra-low latency to Tempe.

In the high-density shared VPS market, there is one undisputed heavyweight for raw specs-per-dollar.

The Winner: Contabo (Cloud VPS XL)
Contabo’s entire business model is offering massive RAM and storage pools at dirt-cheap prices by heavily overprovisioning their physical servers.

Price: ~$35 to $38 / month (depending on the location fee).

Specs: 10 vCPU, 60 GB RAM, 800 GB NVMe (or a massive 1.6 TB standard SSD if you prefer capacity over speed).

Location: They have datacenters in Los Angeles and Seattle. Routing from Tempe to LA will give you incredibly snappy latency (around 20-30ms). Your SSH sessions will feel instantaneous.

What this means for your stack:
Because you don't care about dedicated hardware, you are trading consistency for price and location.

Nextcloud & Developer Tools: These will run flawlessly. With 60GB of RAM and NVMe speeds, your web interfaces and database queries will be extremely fast most of the time.

Neo4j & CPU Inference: This is where you will feel the "shared" aspect. You will experience "CPU steal." If the physical server is heavily loaded by other users, your AI inference times will fluctuate. A script that takes 10 seconds to run at 2:00 AM might take 25 seconds to run at 6:00 PM.

The Alternative: Promotional Hunting
If Contabo’s 60GB of RAM isn't close enough to your 64GB requirement, your only other option in the shared VPS space is hunting for cyclical promotions on sites like LowEndBox. Providers like RackNerd or HostHatch (both have LA datacenters) occasionally drop 64GB RAM / 8 Core plans for around $20 to $30 a month during Black Friday or New Year sales, but standard retail pricing will put you over $60.

If you are ready to pull the trigger today, Contabo is the most straightforward path. Are you leaning towards prioritizing the NVMe drive for faster database reads, or the 1.6TB SSD for massive Nextcloud file storage?

You said
Dedicated Server EX63
Intel® Core™ Ultra 7 265
64 GB DDR5 UDIMM
2x 1 TB NVMe SSD M.2
1 Gbit/s bandwidth
max. per month:
from € 90.44
per hour:
from € 0.1449
once-off setup:
€ 117.81
Dedicated Server EX44
Intel® Core™ i5-13500 14 Core "Raptor Lake-S"
64 GB DDR4 RAM
2 x 512 GB NVMe SSD (Gen 4, Software RAID 1)
1 Gbit/s bandwidth
more information...
max. per month:
from € 52.36
per hour:
from € 0.0839
once-off setup:
€ 117.81
any vlakue to consider
Gemini said
There is immense performance value in these machines, but there is a massive financial catch that completely derails your $50/month budget.

You are looking at Hetzner's mainline, brand-new server deployments rather than their older auction servers. Here is the reality of what these options offer versus what they cost.

The Elephant in the Room: The Setup Fee
Both of these servers carry a €117.81 (roughly $127 USD) one-time setup fee.

If you plan to keep the server for exactly one year, amortizing that setup fee adds about $10.50 to your monthly cost.

The EX44 effectively becomes ~$68/month for the first year.

The EX63 effectively becomes ~$108/month for the first year.

Given your goal was ideally $20 and max $50, the EX63 is entirely out of the question. However, the EX44 warrants a closer look if you are willing to break your budget for bleeding-edge speed.

Why the EX44 is a Monster
Even though you don't care about dedicated hardware in principle, you do care about CPU inference and database performance. The EX44 offers a modern Intel Core i5-13500 (Raptor Lake).

The Architecture Advantage: This chip has 14 cores (6 Performance cores and 8 Efficient cores) and 20 threads. When you start spinning up local multi-agent Python systems or running heavy parallel inference tasks, those modern P-cores will execute code exponentially faster than any heavily shared Contabo vCPU or older 2018 Xeon from the auction block.

Gen 4 NVMe: The jump from standard NVMe to PCIe Gen 4 NVMe means your read/write speeds will be practically instant. Neo4j graph traversals will fly.

The Verdict: Is there any value to consider?
Yes, but only if you view it as a long-term investment.

If you plan to run this server for 2+ years and want a machine that can handle complex, modern AI workloads without breaking a sweat, the EX44 is one of the best performance-per-dollar ratios in the world right now. You just have to be willing to swallow that $127 setup fee on day one.

However, if you strictly want to stay under $50 out-of-pocket today:
You must ignore these mainline EX servers entirely. You are back to the two original champions:

Contabo Cloud VPS XL (~$35/mo, $0 setup): If you want to avoid upfront fees, stay strictly in budget, and have the server located on the West Coast for snappy SSH latency.

Hetzner Server Auction (~$45/mo, $0 setup): If you want to stalk the auction page for an older dedicated machine with NVMes to guarantee consistent inference times, accepting the European latency.

Are you willing to eat a $130 upfront cost for top-tier processing power, or is the hard $50-a-month limit non-negotiable?

You said
for GPU inference. I have a 3090ti at home that could be meshed (can add a 1080ti to system too) but for altnerates lets review.

Skip to Navigation

Skip to Right Sidebar

Back

Go to LocalLLaMA
r/LocalLLaMA
•1mo agoJohnTheNerd3

Running Qwen3.5 27b dense with 170k context at 100+t/s decode and ~1500t/s prefill on 2x3090 (with 585t/s throughput for 8 simultaneous requests)
Other

0:06 / 0:22

Hi everyone!
I've been trying to run the new Qwen models as efficiently as possible with my setup - and seem to have performance higher than I've seen around, so wanted to share my scripts and metrics!
The above video is simulating ideal conditions - due to the nature of MTP, it does get slower once your response requires more intelligence and creativity. However, even at the worst-case scenario I rarely ever see my decode speeds drop below 60t/s. And for multi-user throughput, I have seen as high as 585t/s across 8 requests.
To achieve this, I had to:
Use vLLM with tensor parallelism (I also have NVLink, which probably plays a role considering tensor parallelism does better with GPU interconnect).
Enable MTP with 5 tokens predicted. This is in contrast to any documentation I've seen which suggests 3, but in practice I am getting mean acceptance length values above 3 with my setup so I think 5 is appropriate. I found values above 5 not to be worth it, since the mean acceptance length never exceeded 5 when I tried with higher values. I have also observed a noticable slowdown when I cranked MTP above 5 tokens.
Compile vLLM from scratch on my own hardware. It's a fairly slow operation, especially if your CPU is not great or you don't have a lot of RAM - I typically just leave the compilation running overnight. It also doesn't seem to increase the performance much, so it's certainly not a requirement but something I did to get the absolute most out of my GPU's.
Use this exact quant because the linear attention layers are kept at full-precision (as far as I can tell, linear attention still quantizes rather poorly) and the full attention layers are quantized to int4. This matters, because 3090's have hardware support for int4 - massively boosting performance.
Play around a lot with the vLLM engine arguments and environment variables.
The tool call parser for Qwen3 Coder (also used in Qwen3.5 in vLLM) seems to have a bug where tool calling is inaccurate when MTP is enabled, so I cherry-picked this pull request into the current main branch (and another pull request to fix an issue where reasoning content is lost when using LiteLLM). My fork with the cherry-picked fixes are available on my GitHub if you'd like to use it, but please keep in mind that I am unlikely to maintain this fork.
Edit: The PR with the tool calling fix is merged and the fork is no longer necessary.
Prefill speeds appear to be really good too, at ~1500t/s.
My current build script is:
#!/bin/bash

. /mnt/no-backup/vllm-venv/bin/activate

export CUDACXX=/usr/local/cuda-12.4/bin/nvcc
export MAX_JOBS=1
export PATH=/usr/local/cuda-12.4/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda-12.4/lib64:$LD_LIBRARY_PATH

cd vllm

pip3 install -e .
And my current launch script is:
#!/bin/bash

. /mnt/no-backup/vllm-venv/bin/activate

export CUDA_VISIBLE_DEVICES=0,1
export RAY_memory_monitor_refresh_ms=0
export NCCL_CUMEM_ENABLE=0
export VLLM_SLEEP_WHEN_IDLE=1
export VLLM_ENABLE_CUDAGRAPH_GC=1
export VLLM_USE_FLASHINFER_SAMPLER=1

vllm serve /mnt/no-backup/models/Qwen3.5-27B-AWQ-BF16-INT4 --served-model-name=qwen3.5-27b \
--quantization compressed-tensors \
--max-model-len=170000 \
--max-num-seqs=8 \
--block-size 32 \
--max-num-batched-tokens=2048 \
--swap-space=0 \
--enable-prefix-caching \
--enable-auto-tool-choice \
--tool-call-parser qwen3_coder \
--reasoning-parser qwen3 \
--attention-backend FLASHINFER \
--speculative-config '{"method":"qwen3_next_mtp","num_speculative_tokens":5}' \
--tensor-parallel-size=2 \
-O3 \
--gpu-memory-utilization=0.9 \
--no-use-tqdm-on-load \
--host=0.0.0.0 --port=5000

deactivate
Hope this helps someone!

Upvote
697

Downvote

135
Go to comments
3

Share 

bluehost
•
Promoted

Start hosting with us and get a free domain for the 1st year✨

Learn More
bluehost.com

Sort by:
Best

Search Comments
Expand comment search
Comments Section

WithoutReason1729

MOD
•
1mo ago
Your post is getting popular and we just featured it on our Discord! Come check it out!
You've also been given a special flair for your contribution. We appreciate your post!
I am a bot and this action was performed automatically.

Medium_Chemist_4032
•
1mo ago

That's spectacular, on a dense 30b-ish dual-gpu split configuration. Never seen anything like it!

DistanceSolar1449
•
1mo ago
 Top 1% Commenter
It’s because he’s running attention at int4 (in order to take advantage of ampere hardware support for int4)
Attention quants better than SSM, but 4 bit attention is a brave/stupid move. Most people quant attention to Q8 for a reason. For example, unsloth Q4_K_XL quants attention qkv to Q8 and gate to Q6.
That model is gonna be really brain damaged at 4 bit attention.

jeffwadsworth
•
1mo ago
Yeah, I value quality over all other factors.

JohnTheNerd3
OP
•
1mo ago
•
Edited 1mo ago

the quality is surprising, actually - I urge you to try it before you mock it!
edit: the Q4_K_XL does not, in fact, have either of those. they are both set to Q5. https://huggingface.co/unsloth/Qwen3.5-27B-GGUF/tree/main?show_file_info=Qwen3.5-27B-UD-Q4_K_XL.gguf

DistanceSolar1449
•
1mo ago
 Top 1% Commenter
What’s the PPL? And/or KLD but even just PPL would tell us a lot in this case.
And quoting unsloth directly: “Quantizing any attn_* is especially sensitive for hybrid architectures, and so leaving them in higher precision works well”

JohnTheNerd3
OP
•
1mo ago
•
Edited 1mo ago

FWIW, I just looked at the unsloth quant for the 27b and it doesn't seem any of the layers you mentioned are actually at Q8. perhaps you're thinking of another model?

[deleted]
•
1mo ago

2 more replies

robertio1
•
22d ago
After a half an hour usage with opencode I confirm this BF16-INT4 quant is incredible high quality!
I gave a fairly complex playwright MCP task and it was solved in 1 minute.
Then new task: Classical Earth task:
"Create a Three.js-based procedural visualization of Earth using high-resolution satellite imagery (e.g., NASA Blue Marble), with real-time rotation, drag-to-rotate and scroll-to-zoom interaction, and WebGL PBR rendering. add visible floating clouds layer"

And then this prompt:
"make an python application: open my webcam show it, and recognise what number i show with my fingers. show it as large number and say it in english."
Was finalised in 2 minutes. with creating venv, installing pip packages, and run the perfect implementation.
Im so surprised on Quality and speed.

1 more reply

youcloudsofdoom
•
1mo ago
As someone in the process of putting together a dual 3090 rig, this looks like it's going to be VERY useful, thank you! 

DistanceSolar1449
•
1mo ago
 Top 1% Commenter
It’ll be semi useful. I don’t think some of his decisions are good. Using 4 bit attention is questionable, it’s gonna wreck model performance. Using nvlink is overkill, it won’t help the performance much at all (an all-reduce with hidden size = 5120 and BF16 activations across 128 collectives would be 1.3MB, which doesn’t come close to saturating PCIe).

Kamal965
•
1mo ago
I mean, it's not like he's going to remove NVLink if he doesn't need it for this specific model lol.

JohnTheNerd3
OP
•
1mo ago

my understanding is that the latency is more likely to improve things than the actual bandwidth. since P2P support is typically locked away by NVIDIA, the all-reduce operation would have to push the data via the CPU.
however, geohot did since release a hacked driver that might alleviate most performance benefits from using as such. I never bothered trying since I already had the hardware at that point.

u/Galileo-AI
•
Promoted

the open-source control plane for AI agents

Learn More
agentcontrol.dev

Collapse video player

0:00 / 0:00

TacGibs
•
1mo ago
FIY I got around 66 tok/s for the full precision 27B on 4 RTX 3090 (PCIe 4.0 4x), max context and MTP enabled with vLLM nightly.

Kamal965
•
1mo ago
Very impressive! But I really suggest FP8. There's no point in FP/BF16 unless it's, like, life or death, really. Keep KV at FP16

JohnTheNerd3
OP
•
1mo ago

I would actually strongly recommend against FP8 specifically - the 3090 doesn't support that in hardware!
I found that int8 works okay - but appears to be under-optimized in vLLM (at least since I checked last). I don't have numbers to show, other than my observation suggesting int4 performs insanely good on my 3090s. I think the quant I used is a perfect trade-off for the 3090 hardware (the full-precision layers are for linear attention, which itself doesn't take as much compute anyway).

Kamal965
•
1mo ago
^ this. INT8. My bad.

1 more reply

TacGibs
•
1mo ago
No HW support for FP8 on Ampere, so theoretically it'll be slower. I'll try it though. And I'm always keeping the KV at FP16 for hybrid attention models.

Kamal965
•
1mo ago
Ah, well, I meant 8-bit in general, my bad. You'd look for INT8 AWQ, as Ampere does INT8 and INT4.

2 more replies

mentallyburnt
•
1mo ago
Llama 3.1
What settings did you use for this?

xfalcox
•
1mo ago
This is amazing content. I have two servers with the A100 80GB and was considering the 35BA3B MoE due to high concurrency of users + low tolerance for latency, but this may be better as it gets better intelligence.

slava_smirnov
•
1mo ago
a100x2 at 1 vm here. feel free to share your experience

oxygen_addiction
•
1mo ago
 Top 1% Commenter
Really nice!
What is your overall VRAM usage at 170k context?

JohnTheNerd3
OP
•
1mo ago

yes.

JohnTheNerd3
OP
•
1mo ago

jokes aside, it basically takes up the entire cards. I think I have like 20MB free VRAM? I also run headless Linux just to make sure vLLM gets every bit of the VRAM, the OS VRAM usage is under 1MB.

3 more replies

u/Use-Paragon
•
Promoted

Users will never stop asking for more integrations, but integrations costs months of engineering (API research, building auth, error handling etc.). 29% of B2B SaaS engineering teams use an embedded iPaaS - to save 70% of the engineering, but should you? Read the detailed build vs. buy comparison.

Learn More
useparagon.com

overand
•
1mo ago
Good lord, the difference between that and my dual 3090 rig (no NVLink) with llama.cpp is shocking.Also, this isn't factoring in my current "IDK what's going on here" situation where the model takes a surprisingly long time to start responding after llama.cpp has announced that it's done with prompt processing. The comparison against Gemma3-27B is stark - I'll try to get some numbers. But, in terms of basic numbers, with one request, we look like this:
## Qwen3.5-27B-heretic-GGUF:Q4_K_M

prompt eval time = 831.24 ms / 781 tokens ( 1.06 ms per token, 939.56 tokens per second)
eval time = 14170.30 ms / 485 tokens ( 29.22 ms per token, 34.23 tokens per second)
total time = 15001.54 ms / 1266 tokens

sleepy_roger
•
1mo ago
Yep, this is why I grabbed an NVLink way back. People in the sub used to say it didn't make much of a difference but I saw a pretty significant difference, glad I paid the $200 back then.

munkiemagik
•
1mo ago
I know right, I am even looking at yours and thinking how the bleep are you getting 34 t/s.
Oh hang on you're using Q4_K_M, I was seeing around 24t/s on Q6_K_L.. What other parameters are you running in your llama-server command?

4 more replies

floppypancakes4u
•
1mo ago
Im literally trying to get a used mobo right now to setup dual 3090 as well.

nsmitherians
•
1mo ago
Where do you guys get GPUs from? I am paranoid about buying from Facebook marketplace (buying ones that are broken)

AdamTReineke
•
1mo ago
I got one off Marketplace and one off eBay. Both used EVGA 3090 FTW3.

4 more replies

klop2031
•
1mo ago
•
Edited 1mo ago
Whats your speed with 1 3090. Im getting like 20tps which sux
Ohh i see here that int4. Didnt realize this may quantize my own

1 more reply

raysar
•
1mo ago
with new small 3,5 model today maybe we can go faster with speculative decoding? but we need to find best tunning for that.

RnRau
•
1mo ago
It comes with speculative decoding builtin.

2 more replies

jslominski
•
1mo ago

 Top 1% Poster
I tried the same setup on my own 2× RTX 3090 machine, with each card capped at 280W and no NVLink, and this is genuinely impressive.
I’m seeing about 692 tok/s total throughput on an 8-request run, around 77 tok/s output throughput, and roughly 1,112 tok/s on a prefill-heavy test, very nice result indeed!
Here's another run:

JohnTheNerd3
OP
•
1mo ago

WOW I actually forgot to mention..... I cap at 260W............

3 more replies

jslominski
•
1mo ago

 Top 1% Poster

Codes as good as the UD 4bit version in my 2-3 tests I did.

ISLITASHEET
•
28d ago
Looks like the pr that you cherry picked from has been merged. Might want to update the post to direct future people back to upstream.

1 more reply

robertio1
•
22d ago
Hi.
Many thanks u/JohnTheNerd3,
i also has dual RTX 3090 so i was exited to try it out your advise.
Incredible speed increase compared to unslot Q3.5_27B_Q8_250k context. provided a quality code and works great with opencode. but it was slow 10 token/s.
Based on your excellent advise i tried VLLM from python (version 17.0) but failed with any MTP speculative config.
but today the Git issue solved: https://github.com/vllm-project/vllm/issues/36498#issuecomment-4030405785
So i compiled VLLM from source and this command is works for me:
vllm serve /adat/ai/models/Qwen3.5-27B-AWQ-BF16-INT4 --served-model-name=qwen3.5-27b \
--quantization compressed-tensors \
--max-model-len=170000 \
--max-num-seqs=8 \
--block-size 32 \
--max-num-batched-tokens=2048 \
--enable-prefix-caching \
--enable-auto-tool-choice \
--tool-call-parser qwen3_coder \
--reasoning-parser qwen3 \
--attention-backend FLASHINFER \
--speculative-config '{"method":"mtp","num_speculative_tokens":5}' \
--tensor-parallel-size=2 \
-O3 \
--gpu-memory-utilization=0.9 \
--no-use-tqdm-on-load \
--host=0.0.0.0 --port=1234
having 22t/s and max 103t/s but mostly 50-60t/s
Many many thanks. :)

1 more reply

ortegaalfredo
•
1mo ago

 Top 1% Poster
The trick is "don't use llama.cpp, lmstudio or ollama".
For a project so widespread and with so many contributors, there has to be something fundamentally wrong if every other project like sglang, vllm, tensor-rt are basically 20x faster. I just measured on my rig, it's more than 20 times faster. This is not just a "bug".
I bet there is some pressure from you know who, to slow it down and make it useless to serve multi-user loads.
I have no other explanation, 20X is too much difference.

desirew
•
1mo ago
Are those faster for single user usage though ?

ortegaalfredo
•
1mo ago

 Top 1% Poster
About the same or slightly faster. For single use I guess llama.cpp is OK but even for agents vllm already is much faster. I don't want to trash on their project, they are very easy to use and it have gguf that works 100% everywhere but, why they have to be so slow?

JohnTheNerd3
OP
•
28d ago

my understanding is that llama.cpp can actually be faster for decode on single-user usecases. there are a few reasons the speed difference is this ridiculous:
MTP support just isn't in llama.cpp yet. this makes an insane difference. doubling speed is common.
llama.cpp is mostly hobbyists and individual contributors, while vLLM and sglang are used by big corporations for LLM inference. this means there are people on payroll working to improve vLLM, since any compute savings actually result in savings in companies' bottom lines.
due to the above, vLLM actually has some custom handmade CUDA kernels that fuse operations. this is a truly incredible amount of effort, and requires expertise most people lack.
I don't think it's fair to compare the two this way. llama.cpp actually does a lot better in many cases (offloading, KV cache quantization, decode for single-user inference, VRAM efficiency) because these do not align with corporate interests and therefore very few people spend the time and effort on these aspects.
I use llama.cpp for many models, personally, because vLLM is not a good fit. always pick the right tool for the job!

Deathclaw1
•
1mo ago
To be fair, llama.cpp has a feature where it offloads some of the model layers to the ram instead of vram, making things slow sometimes, its also starts fast and has low requirements (lm studio and ollama both are using it).
Vllm on the other hand fits everything in the vram from my understanding, even memory (I think) so its better optimized than llama.cpp.
So yea vllm will be faster but it needs cuda and other things. Basically llama.cpp is meant for consumer grade hardware while vllm is for production and eats vram.

ortegaalfredo
•
1mo ago

 Top 1% Poster
I fit everything into VRAM in llama.cpp and it still is 20 times slower. 60 tok/s llama.cpp vs 1500 tok/s vllm, 40 queries.

tarruda
•
1mo ago
 Top 1% Commenter
That's probably because vLLM contains official implementation for qwen-next architecture.
Llama.cpp implementation comes community contributions and is probably not as optimized yet.

ortegaalfredo
•
1mo ago

 Top 1% Poster
Also because llama.cpp basically has a non-working tensor-parallel inference.

overand
•
28d ago
If the you-know-who is HF, and you're suggesting they're trying to make llama.cpp worse, why exactly are they partnering with GGML-org and llama.cpp's team?

1 more reply

Naz6uL
•
1mo ago
Unfortunately, without a GPU, my only option at the moment is to try it on my MBP with 128 GB RAM.

Double_Sherbert3326
•
1mo ago
Crazy humblebrag 

Middle-Advisor5783
•
1mo ago
I wonder does the code being generated work? Even deepseek r1 code doesn't work as expected. The one functional codes come from codex. And it is a a lot reliable and does whst you ask as you want. Others iust crap! Even claude  code cant do shiot about serious logical and big codebase.

JohnTheNerd3
OP
•
1mo ago

I certainly have not tested the resulting code - that was merely for a speed test. however, I do routinely use local models in my Claude Code (vLLM supports the Anthropic /messages endpoint and works as a drop-in replacement for the Claude Code client) and do get useful code output. just need to keep your expectations in check, it's a LLM running in my basement and will certainly require me to spell out a few things and take some debugging here and there.

Medium_Chemist_4032
•
1mo ago

Yeah, nothing beats Opus by faaar. However, I keep trying and trying to find best usecases for locally hosted LLMs and the actual list of useful things is growing.
Try most recent qwen3.5 models overall. I pointed one at a legacy app (lot's of code, lot's of never cleaned up dead ends) and to list certain aspect of the REST endpoint set and it nailed it. This wasn't a trivial task for sure.

1 more reply

Kamal965
•
1mo ago
It absolutely performs. Perhaps not quite as good as Opus or GPT 5.2, but those are, at the very least, trillion parameter models. I find it to be a more than satisfactory assistant in math, coding and data science.

Lifeisshort555
•
1mo ago
I'd rather run it slower at higher q. If I have a choice I do not go below 6. If you arent gpu poor you should do the same imo.

akazakou
•
1mo ago

MightyBigMinus
•
1mo ago

Spectrum1523
•
1mo ago
 Top 1% Commenter
that is fantastic. i need to try vllm. i only have one 3090 though, so I don't think I could actually run that quant.

NoFudge4700
•
1mo ago

That’s amazing! 27b is a dense model, right?

1 more reply

sleepy_roger
•
1mo ago
•
Edited 1mo ago
I can't get it to do things I'm able to do with GLM 4 32b... this is what I'm using -
Qwen3.5-27B-UD-Q8_K_XL.gguf
Temp 0.6, top_k 20, top_p 0.95, min-p 0.
Can anyone try this and see if it actually makes a reasonable clock?
Hey! Can you create an analog clock with HTML/CSS it should show the current time lets start at 10:00pm.

Include numerals, use CSS to animate the hands using transform rotate. Lets tween the animation between each second for the second hand and the minute hand using javascript to keep it in time. The hands should start in the center of the clock face extending towards the edge. Make the clock face a circle. Additionally lets lets make the numerals and the minute and hour hand black, lets make the minute hand red. This should also be responsive, responsive in the sense that when the screen dimensions are reduced the clock scales appropriately, so ensure you’re using transform origin and zoom with the CSS.

Return only html css and javascript.
This is what GLM 4 32B one shot with the same prompt, (was proving a point to someone)
https://codepen.io/loktar00/pen/jEroozp
I get weird results with qwen though which is pretty surprising... (thinking and using the recommended settings from unsloth) they're "close" but not great. The prompt isn't great but that was the point I was making to someone, yet GLM 4 from last March knocked it out of the park.

Klutzy-Snow8016
•
1mo ago
Qwen3.5-27B-FP8, from Qwen, using their recommended general purpose thinking sampler settings: https://codepen.io/exploding_battery/pen/jEMbyxy

1 more reply

[deleted]
•
1mo ago
•
Edited 6d ago
This post was deleted using Redact. The deletion may have been privacy-motivated, security-driven, opsec-related, or simply a personal decision by the author.
sink price juggle elderly whole ripe normal memory observation wild

sleepy_roger
•
1mo ago
Ok then it's definitely something with my settings I'm guessing. Thank you! I was thinking there's no way it couldn't do this.

[deleted]
•
1mo ago
•
Edited 6d ago
The original text here has been permanently wiped. Using Redact, the author deleted this post, possibly for reasons of privacy, security, or opsec.
quickest nutty rich childlike rhythm rain wrench connect dime cover

alitadrakes
•
1mo ago
Hello, may i dm you? I’m trying to run nvidia nemotron nano 12b v2 vl with same gpu as yours… gemini is running me in circles and cant find any solution to run it.

Appropriate-Lie-8812
•
1mo ago
What’s your average acceptance length in practice (and on what workload)?

JohnTheNerd3
OP
•
1mo ago

I didn't spend enough time with the model to be able to answer that - but I typically see above 3 for coding-related tasks. my main use case is a voice assistant, though, so I suspect it will not be very relatable regardless.

ghosthacked
•
1mo ago
Silly me, i have two 3090, one does comfyui, one does ollama/openwebui. I know now what i must do, i dont know if i have the strength...

ghosthacked
•
1mo ago
I know nothing about nvlink, i see em on ebay from 70$ to 600$ - wtf. halp.

JohnTheNerd3
OP
•
1mo ago

try geohot's P2P driver! it's meant for the 4090, but it just might work for the 3090 too. it might improve things enough not to need the additional hardware!

IrisColt
•
1mo ago
Does the code in the example video... work at all? Genuinely asking.

ab2377
•
1mo ago
llama.cpp
livin the dream

EatTFM
•
1mo ago
Is it just fast, or is it also good in quality? I reckon it is a general purpose model not ideal for coding, right?

sabotage3d
•
1mo ago
I am using a single 3090 on a UD Q5 K XL, getting around 30 t/s with llama.cpp. Are your settings transferable to llama.cpp?

moahmo88
•
1mo ago
Good job!

sgmv
•
1mo ago
Would you mind trying the two Q8 quants from unsloth, with and without the nvlink, if it's not too much trouble ? I have 2x 3090 without nvlink but using llama cpp at the moment. I can try vllm myself I guess. Need to evaluate if it's worth getting a nvlink bridge, can't even find one in my country.

EffectBrief1480
•
1mo ago
good

Sufficient-Rent6078
•
1mo ago
•
Edited 1mo ago
I can confirm that I'm hitting above 3000t/s prefill for a dual RTX-4090 setup on the current vllms nightly build with pretty much the same configuration. Decode is roughly in the 100-130 t/s range. I did not run any rigorous benchmarks, so take this with a grain of salt.
Edit: Having tried it out a bit more, the whole thing feels a bit too unstable, so I'm switching back to Qwen3-Coder-Next-GGUF:IQ4_XS and Qwen3.5-27B-GGUF:UD-Q6_K_XL for the time being.

JohnTheNerd3
OP
•
1mo ago

beware: the nightly is missing the tool call fix - you might get incorrect tool calls at times!
I'm curious, have you tried this driver? it might improve performance further! https://github.com/tinygrad/open-gpu-kernel-modules

4 more replies

nikos_m
•
1mo ago
this is really good!

Beautiful-Honeydew10
•
1mo ago
That’s some real useful performance you have there. Thanks for sharing the details of your setup.

H4UnT3R_CZ
•
1mo ago
nvlink has nothing to do with inference. During fine tuning it's utilised a lot. I had two 3090 without nvlink, one on pcie gen4 x4 and had on qwen3 42GB version around 60t/s and looked on pcie utilisation - even this wasnt utilised on 100%, avg. 30% during inference. x16 just few %. 
But now I switched to Github Pro, sold both 3090 and running on 5070Ti smaller LLMs if needed... Claude 4.6 is just saving lot of time for programming on my senior level.

3 more replies

Revolutionary_Loan13
•
1mo ago
Your asking for two 5090s.  One 5080... Best offer

amp804
•
1mo ago
What motherboard are you using? 

Tereadol
•
28d ago
Great work honestly!! I have the exact same setup, 2 3090 joined by NVLink and I am so far happy with the results, I am using a bit more GPU utilization to 0.95 in order to reach 180k context window.
I am seeing a lot of people mentioning to rather use the Q6 or Q8 version.... HOW??? those quantization do not fit on a 3090. I mean If you have 5090 I am happy for you guys, but this scenario is running under the constraints of 2 3090 with 24GB of VRAM.
I have tried myself for a Q5_K_M, that should theoretically fit with the tensor parallel and more importantly try to offload the KV cache to RAM, but no matter what I have tried, all my attempts have failed.
If you try to --kv-offloading-backend native you get a: ValueError: Connector OffloadingConnector does not support HMA but HMA is enabled. Please set --disable-hybrid-kv-cache-manager.
If you try to disable hybrid cache you get an
Hybrid KV cache manager is disabled for this hybrid model
ValueError: Hybrid KV cache manager is disabled but failed to convert the KV cache specs to one unified type.

Finally I tried with an LMCache server, but the moment vLLM detects the --kv-transfer-config it disables the hybrid cache manager resulting on the same error.
So in conclusion, and due to my limited experience with vLLM, to have the model running with a decent context all inside the GPU. Kudos!! and I have learn a lot on vLLM by playing around your script.
Thanks.

2 more replies

Extreme-Pass-4488
•
25d ago
Can You test https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilledplease? Pretty please???

naximus17061989
•
21d ago
I am new to setting up local llms and have a dual 3090 setup as well, but the best i am getting doe 27B model is 30 maybe 40token/s. Will try the scripts you shared, thanks

Tyr_56k
•
20d ago
•
Edited 20d ago
INT4... and MTP 5
for some speed is indeed important but without sacrificing the models toolcall-ability completely.
Btw; for a blackwell chip use NVFP4 for nativ calculation instead of AWQ. Not working correctly with blackwell for most anyways.
Floating-Point-sematic with Dual-Scaling instead of plain Integer-Rounding. Especially Qwen3-models reach 99%+ Recovery in NVFP4

bongkyo
•
17d ago
thank you!

throwawaysugaracc
•
14d ago
How would this compare to 8 bit quant? In terms of logic and coding

Equivalent-Home-223
•
9d ago
Thanks for this! I have tested the above in with a project I have ( redesign a project using Material UI) and the model ends up in a infinite loop while using RooCode:
Same set up ( 2x3090) only difference is i am using 90k context.
API Request Failed
Provider ended the request: terminatedDetails
Roo said
Now I'll create a comprehensive redesign plan document based on my analysis of the project.
Checkpoint
Provider Error
API Request FailedDetails
API Request...
$0.0000
Roo said
Now I'll create a comprehensive redesign plan document based on my analysis of the project.

robertio1
•
3d ago
u/JohnTheNerd3 Hi John,
cyankiwi/Qwen3.5-27B-AWQ-BF16-INT4 updated 2 days ago. Do you know why? Is there any benefit to update?

Help lead our community
Apply to be a moderator
DismissApply
Community Info Section

r/LocalLLaMA

Joined
LocalLlama
Subreddit to discuss locally hostable AI
Created Mar 10, 2023
Public1M
Llamas
20K
Weekly contributions

USER FLAIR

PlasmusAng
COMMUNITY BOOKMARKS
Wiki

Best LLMs Megathread

Best VLMs Megathread

Best TTS/STT Models
R/LOCALLLAMA RULES
1
Please search before asking

2
Off-Topic Posts

3
Low Effort Posts

4
Limit Self-Promotion

5
Follow Reddit's Content Policy

SOCIALS
AMA
MODERATORS

Message Mods

u/HOLUPREDICTIONS Sorcerer Supreme
Yo

u/AskGrok
Grok

u/ArcaneThoughts

u/Lissanro

u/townofsalemfangay

u/XMasterrrrLocalLLaMA Home Server Final Boss 😎
@TheAhmadOsman

u/rm-rf-rm llama.cpp

u/N8Karma

u/WithoutReason1729

u/No_Afternoon_4260 llama.cpp

View all moderators
INSTALLED APPS
Admin Tattler

Bot Bouncer

Reddit Rules
Privacy Policy
User Agreement

Your Privacy Choices
Accessibility

Reddit, Inc. © 2026. All rights reserved.

Collapse Navigation

Home

Popular

News

Explore

Start a community
GAMES ON REDDIT

Pocket Grids
Mini crosswords
407K monthly players
NEW

BattleBirds

Pipe Panic

romkerl

Discover More
MODERATION

Mod Queue

Mod Mail

r/Mod

Manage

r/ATATaekwondo

CUSTOM FEEDS

Create Custom Feed
RECENT

r/ClaudeAI

r/MiniMax_AI
COMMUNITIES

Manage Communities

r/AccidentalCamouflage

r/AccidentalRacism

r/ACT

r/Adhell

r/adventures

r/AdviceAnimals

r/Africa

r/AirMessage

r/ALVR

r/AMA

r/Amd

r/AmdOSX

r/AmItheAsshole

r/Android

r/androidapps

r/AndroidPreviews

r/AndroidQuestions

r/androidthemes

r/AnimalsBeingDerps

r/Animemes

r/announcements

r/antiassholedesign

r/antimeme

r/antiMLM

r/antivax

r/appreciatewatersheep

r/arabfunny

r/archlinux

r/Art

r/AskMen

r/AskReddit

r/askscience

r/assholedesign

r/ASU

r/ATATaekwondo

r/ATBGE

r/AteTheOnion

r/atheism

r/Atheist_Teens

r/audiophile

r/AVexchange

r/AwesomeCarMods

r/awesomewm

r/awfuleverything

r/aws

r/aww

r/AyyMD

r/backpacking

r/BackpackingDogs

r/Bad_Cop_No_Donut

r/badUIbattles

r/battlestations

r/bearsdoinghumanthings

r/beatMeatToIt

r/beatsaber

r/bedrocklinux

r/bestof

r/beta

r/BetterDiscord

r/BikiniBottomTwitter

r/Biohackers

r/birthofasub

r/black_humor

r/blackpeoplegifs

r/BlackPeopleTwitter

r/blessedimages

r/blog

r/blokada

r/blursedimages

r/BoJackHorseman

r/BoneAppleTea

r/books

r/boomershumor

r/BrandNewSentence

r/BreathingBuddies

r/buildapcforme

r/BulletBarry

r/cakeday

r/camping

r/CampingandHiking

r/CampingGear

r/Capitalism

r/cars

r/CatastrophicFailure

r/changemyview

r/characterarcs

r/chargetheyphone

r/China_Flu

r/ChoosingBeggars

r/chrome

r/CitiesSkylines

r/clevercomebacks

r/coaxedintoasnafu

r/college

r/ComedyCemetery

r/comedyheaven

r/comedyhomicide

r/comedynecromancy

r/ComedyNecrophilia

r/commandline

r/computers

r/confusing_perspective

r/conspiracy

r/coolgithubprojects

r/coolguides

r/Coronavirus

r/CoronavirusCA

r/CoronavirusUS

r/Corsair

r/CozyPlaces

r/cpp

r/cprogramming

r/creepy

r/creepypasta

r/cringe

r/cringepics

r/CryptoCurrency

r/cscareerquestions

r/csharp

r/csMajors

r/Cursed_Images

r/cursedcomments

r/cursor

r/CustomKeyboards

r/cybersecurity

r/Damnthatsinteresting

r/dankchristianmemes

r/dankmemes

r/darkjokes

r/darknet

r/dataisbeautiful

r/DebateAnAtheist

r/DecreasinglyVerbose

r/deepweb

r/DesignDesign

r/desktops

r/DesperateDesign

r/destiny2

r/DestinyFashion

r/DestinyTheGame

r/discordapp

r/DistroHopping

r/DIY

r/Documentaries

r/DogShowerThoughts

r/dogswithjobs

r/dontflinch

r/dontputyourdickinthat

r/Drugs

r/duckduckgo

r/EarthEnthusiasts

r/EarthPorn

r/eddyburback

r/edge

r/EDM

r/elementcollection

r/eliteexplorers

r/elonmusk

r/EndeavourOS

r/engrish

r/entitledparents

r/entitledparentsmemes

r/Entrepreneur

r/epidemic

r/ErgoMechKeyboards

r/europe

r/evilbuildings

r/exmuslim

r/ExperiencedDevs

r/explainlikeimfive

r/Eyebleach

r/facepalm

r/FakeButFunny

r/fakehistoryporn

r/FiftyFiftySFW

r/financialaid

r/FinancialCareers

r/financialindependence

r/FinancialPlanning

r/firefox

r/FirefoxCSS

r/FireFriends

r/Fitness

r/FiveM

r/flightsim

r/food

r/FoodPorn

r/forwardsfromgrandma

r/freebsd

r/freesoftware

r/FuckAds

r/funny

r/Futurology

r/gadgets

r/Galaxy_S20

r/galaxybuds

r/GalaxyS21

r/GalaxyS9

r/GalaxyWatch

r/GalaxyWatchActive2

r/Galimulator

r/Galimulatorgame

r/GameDeals

r/gamernews

r/gaming

r/Gamingcirclejerk

r/gatekeeping

r/GearTrade

r/GeniusDesign

r/GeorgiaOrGeorgia

r/GetMotivated

r/gifs

r/GlobalOffensive

r/gloriouspcgamingrace

r/gnu

r/GoCommitDie

r/gog

r/golang

r/googlehome

r/GooglePixel

r/googleplaydeals

r/greentext

r/GTAGE

r/GTAorRussia

r/gusjohnson

r/h3h3productions

r/hackernews

r/hacking

r/Hacking_Tutorials

RESOURCES

About Reddit

Advertise

Developer Platform

Reddit Pro
BETA

Help

Blog

Careers

Press

Best of Reddit

Reddit Rules

Privacy Policy

User Agreement

Your Privacy Choices

Accessibility
Reddit, Inc. © 2026. All rights reserved.
This will be a worker model we want to use for 50%+ of our requests at similar min 50-100tok <5s TTFT 8-16 concurrent requests.
lets look at modal options on hf\the web.

e.g. qwen3.5 coder 27b and reap variants, other similar <32b modals and quants+distills etc.
https://huggingface.co/cerebras/Kimi-Linear-REAP-35B-A3B-Instruct
and more.

min perf is comparable to gpt 5 mini \ claude haiku. reaperdoesntknow/Qwen3-1.7B-Coder-Distilled-SFT

Text Generation •

2B
•
Updated about 9 hours ago
•

1.89k
reaperdoesntknow/Qwen3-1.7B-Coder-Distilled-SFT-GGUF

Text Generation •

2B
•
Updated about 9 hours ago
•

742
12bitmisfit/Qwen3-Coder-30B-A3B-Instruct_Pruned_REAP-15B-A3B-GGUF

16B
•
Updated Oct 22, 2025
•

323•

8
RepublicOfKorokke/Qwen3-Coder-Next-REAP-48B-A3B-oQ4

Text Generation •

8B
•
Updated 2 days ago
•

247•

1
RepublicOfKorokke/Qwen3-Coder-Next-REAP-48B-A3B-oQ3

Text Generation •

6B
•
Updated 2 days ago
•

243
RepublicOfKorokke/Qwen3-Coder-Next-REAP-48B-A3B-oQ3.5

Text Generation •

7B
•
Updated 2 days ago
•

200•

1
lainlives/Qwen3-Coder-30B-A3B-Instruct_Pruned_REAP-15B-A3B-SafeTensors-Q4_K_M-GGUF

16B
•
Updated Jan 31
•

170
Firworks/Qwen3-Coder-REAP-25B-A3B-nvfp4

14B
•
Updated Dec 28, 2025
•

88•

1
lainlives/Qwen3-Coder-30B-A3B-Instruct_Pruned_REAP-15B-A3B-SafeTensors-Q6_K-GGUF

16B
•
Updated Jan 31
•

47
lainlives/Qwen3-Coder-30B-A3B-Instruct_Pruned_REAP-15B-A3B-SafeTensors-Q5_0-GGUF

16B
•
Updated Jan 31
•

36
lainlives/Qwen3-Coder-30B-A3B-Instruct_Pruned_REAP-15B-A3B-SafeTensors-Q8_0-GGUF

16B
•
Updated Jan 31
•

9
12bitmisfit/Qwen3-Coder-30B-A3B-Instruct_Pruned_REAP-15B-A3B-SafeTensors

16B
•
Updated Oct 22, 2025
•

8•

2
v3ss0n/Qwen3-Coder-REAP-25B-A3B-autoround-4bit

0.6B
•
Updated Nov 25, 2025
•

1•

3
sasa2000/Qwen3-Coder-REAP-25B-A3B-W4A16

0.6B
•
Updated Jan 10
•

1•

1 https://huggingface.co/cerebras/GLM-4.7-Flash-REAP-23B-A3B https://huggingface.co/reaperdoesntknow/Qwen3-1.7B-Coder-Distilled-SFT21

Flagstone8878/Qwen3.5-18B-REAP-A3B-Coding-GGUF

19B
•
Updated 27 days ago
•

6.53k•

9
mradermacher/qwen3.5-18b-a3b-reap-coding-heretic-v0-i1-GGUF

19B
•
Updated 21 days ago
•

6k•

1
Testnetair/qwen3.5-18b-a3b-reap-coding-heretic-v0-i1-GGUF

19B
•
Updated 4 days ago
•

4.46k•

1
mradermacher/qwen3.5-18b-a3b-reap-coding-heretic-v0-GGUF

19B
•
Updated 21 days ago
•

2.08k
reaperdoesntknow/Qwen3-1.7B-Coder-Distilled-SFT

Text Generation •

2B
•
Updated about 9 hours ago
•

1.89k
reaperdoesntknow/Qwen3-1.7B-Coder-Distilled-SFT-GGUF

Text Generation •

2B
•
Updated about 9 hours ago
•

742
Flagstone8878/Qwen3.5-18B-REAP-A3B-Coding

19B
•
Updated 28 days ago
•

388•

3
12bitmisfit/Qwen3-Coder-30B-A3B-Instruct_Pruned_REAP-15B-A3B-GGUF

16B
•
Updated Oct 22, 2025
•

323•

8
RepublicOfKorokke/Qwen3-Coder-Next-REAP-48B-A3B-oQ4

Text Generation •

8B
•
Updated 2 days ago
•

247•

1
RepublicOfKorokke/Qwen3-Coder-Next-REAP-48B-A3B-oQ3

Text Generation •

6B
•
Updated 2 days ago
•

243
RepublicOfKorokke/Qwen3-Coder-Next-REAP-48B-A3B-oQ3.5

Text Generation •

7B
•
Updated 2 days ago
•

200•

1
lainlives/Qwen3-Coder-30B-A3B-Instruct_Pruned_REAP-15B-A3B-SafeTensors-Q4_K_M-GGUF

16B
•
Updated Jan 31
•

170
Firworks/Qwen3-Coder-REAP-25B-A3B-nvfp4

14B
•
Updated Dec 28, 2025
•

88•

1
tvall43/qwen3.5-18b-a3b-reap-coding-heretic-v0

19B
•
Updated 27 days ago
•

57•

3
lainlives/Qwen3-Coder-30B-A3B-Instruct_Pruned_REAP-15B-A3B-SafeTensors-Q6_K-GGUF

16B
•
Updated Jan 31
•

47
lainlives/Qwen3-Coder-30B-A3B-Instruct_Pruned_REAP-15B-A3B-SafeTensors-Q5_0-GGUF

16B
•
Updated Jan 31
•

36
lainlives/Qwen3.5-18B-REAP-A3B-Coding-bnb-4bit

17B
•
Updated 13 days ago
•

12
lainlives/Qwen3-Coder-30B-A3B-Instruct_Pruned_REAP-15B-A3B-SafeTensors-Q8_0-GGUF

16B
•
Updated Jan 31
•

9
12bitmisfit/Qwen3-Coder-30B-A3B-Instruct_Pruned_REAP-15B-A3B-SafeTensors

16B
•
Updated Oct 22, 2025
•

8•

2
v3ss0n/Qwen3-Coder-REAP-25B-A3B-autoround-4bit

0.6B
•
Updated Nov 25, 2025
•

1•

3
sasa2000/Qwen3-Coder-REAP-25B-A3B-W4A16

0.6B
•
Updated Jan 10
•

1•

1Hugging Face

Models
158

Active filters: text-generation, min:3B, max:24B, en
Clear all
Jackrong/Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled-GGUF

Text Generation •

4B
•
Updated 17 days ago
•

202k•

82
Jackrong/Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-GGUF

Text Generation •

9B
•
Updated 17 days ago
•

202k•

217
Jackrong/Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled

Text Generation •

10B
•
Updated 25 days ago
•

97.1k•

50
LuffyTheFox/Qwen3.5-9B-Claude-4.6-Opus-Uncensored-Distilled-GGUF

Text Generation •

9B
•
Updated 14 days ago
•

44.7k•

84
mconcat/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-NVFP4

Text Generation •

22B
•
Updated 13 days ago
•

18.9k•

35
Jackrong/Qwen3.5-9B-Gemini-3.1-Pro-Reasoning-Distill-GGUF

Text Generation •

9B
•
Updated 22 days ago
•

16.2k•

23
tvall43/Qwen3.5-14B-A3B-Claude-4.6-Opus-Reasoning-Distilled-reap-gguf

Text Generation •

14B
•
Updated 23 days ago
•

14.4k•

12
LEONW24/Qwen3.5-9B-Uncensored

Text Generation •

10B
•
Updated 20 days ago
•

12.1k•

41
Jackrong/Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled

Text Generation •

5B
•
Updated 25 days ago
•

11.4k•

23
lukey03/Qwen3.5-9B-abliterated

Text Generation •

9B
•
Updated 29 days ago
•

10.7k•

43
sandeshrajx/Qwen3.5-24B-A3B-REAP-0.32-GGUF

Text Generation •

19B
•
Updated 25 days ago
•

8.8k•

9
mradermacher/Huihui-Qwen3.5-9B-abliterated-TIES-Hemlock-SFT-i1-GGUF

Text Generation •

9B
•
Updated 2 days ago
•

6.7k•

1
Jackrong/Qwen3.5-9B-Neo-GGUF

Text Generation •

9B
•
Updated 8 days ago
•

5.66k•

12
jc-builds/Qwen3.5-9B-Q4_K_M-GGUF

Text Generation •

9B
•
Updated 24 days ago
•

5.58k•

3
Andycurrent/Qwen3.5-4B-Uncensored-HauhauCS-Aggressive

Text Generation •

4B
•
Updated 19 days ago
•

5.56k•

4
mradermacher/Qwen3.5-9B-Writing-DPO-i1-GGUF

Text Generation •

9B
•
Updated 25 days ago
•

5.3k•

1
mradermacher/Huihui-Qwen3.5-9B-abliterated-Grimoire-SimPO-i1-GGUF

Text Generation •

9B
•
Updated 12 days ago
•

5.04k•

1
bigatuna/Qwen3.5-9b-Sushi-Coder-RL-GGUF

Text Generation •

9B
•
Updated about 16 hours ago
•

4.59k•

25
lukey03/Qwen3.5-9B-abliterated-MLX-8bit

Text Generation •

9B
•
Updated 29 days ago
•

4.42k•

5
mradermacher/Huihui-Qwen3.5-9B-abliterated-Grimoire-SFT-i1-GGUF

Text Generation •

9B
•
Updated 14 days ago
•

4.29k•

1
EganAI/qwen3.5-9b-terminal-merge

Text Generation •

9B
•
Updated 15 days ago
•

4.23k•

15
mconcat/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-NVFP4

Text Generation •

22B
•
Updated 6 days ago
•

3.98k•

7
Jackrong/MLX-Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-6bit

Text Generation •

9B
•
Updated 25 days ago
•

3.94k•

5
Jackrong/MLX-Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-8bit

Text Generation •

9B
•
Updated 25 days ago
•

3.24k•

8
MerlinSafety/Qwen3.5-4B-Safety-Thinking

Text Generation •

4B
•
Updated 29 days ago
•

3.21k•

12
danielcherubini/Qwen3.5-DeltaCoder-9B-GGUF

Text Generation •

9B
•
Updated about 2 hours ago
•

2.9k•

6
mradermacher/Huihui-Qwen3.5-9B-abliterated-Grimoire-DPO-i1-GGUF

Text Generation •

9B
•
Updated 11 days ago
•

2.87k
mssfj/Qwen3.5-9B-GPTQ-INT4

Text Generation •

9B
•
Updated 5 days ago
•

2.71k
AaryanK/Qwen3.5-9B-GGUF

Text Generation •

9B
•
Updated 30 days ago
•

2.7k•

2
AaryanK/Qwen3.5-4B-GGUF

Text Generation •

4B
•
Updated 30 days ago
•

2.15k•

2

System theme
TOS
Privacy
About
Careers

Models
Datasets
Spaces
Pricing
DocsHugging Face's logo
Hugging Face

Models
158

Active filters: text-generation, min:3B, max:24B, en
Clear all
danielcherubini/Qwen3.5-DeltaCoder-9B-GGUF
Text Generation
•
9B
•
Updated about 2 hours ago
•
2.9k
•
6
wkplhc/Qwen3.5-4B-NSFW-ARA-Heretic-Literotica-i1-GGUF
Text Generation
•
4B
•
Updated about 11 hours ago
•
53
bigatuna/Qwen3.5-9b-Sushi-Coder-RL-GGUF
Text Generation
•
9B
•
Updated about 16 hours ago
•
4.59k
•
25
bjk110/Qwen3.5-122B-A10B-abliterated-AWQ
Text Generation
•
21B
•
Updated about 23 hours ago
•
1
continuum-ai/qwen3.5-4b-code-forged-GGUF
Text Generation
•
4B
•
Updated 2 days ago
•
1.02k
•
1
mradermacher/Huihui-Qwen3.5-9B-abliterated-TIES-Hemlock-SFT-i1-GGUF
Text Generation
•
9B
•
Updated 2 days ago
•
6.7k
•
1
mradermacher/Huihui-Qwen3.5-9B-abliterated-TIES-Hemlock-SFT-GGUF
Text Generation
•
9B
•
Updated 2 days ago
•
1.53k
•
1
Nubinu/Qwen3.5-4B-MiniFantasy
Text Generation
•
5B
•
Updated 3 days ago
•
810
empulse/KiCAD-MCP-Qwen3.5-4B-GGUF
Text Generation
•
4B
•
Updated 3 days ago
•
602
•
1
Brooooooklyn/Qwen3.5-27B-UD-Q8_K_XL-mlx
Text Generation
•
9B
•
Updated 3 days ago
•
260
•
1
Brooooooklyn/Qwen3.5-27B-UD-Q6_K_XL-mlx
Text Generation
•
9B
•
Updated 3 days ago
•
130
•
2
Brooooooklyn/Qwen3.5-27B-UD-Q5_K_XL-mlx
Text Generation
•
8B
•
Updated 3 days ago
•
57
•
1
Brooooooklyn/Qwen3.5-27B-UD-Q4_K_XL-mlx
Text Generation
•
7B
•
Updated 3 days ago
•
119
•
1
Brooooooklyn/Qwen3.5-27B-UD-Q3_K_XL-mlx
Text Generation
•
6B
•
Updated 3 days ago
•
146
Brooooooklyn/Qwen3.5-27B-UD-Q2_K_XL-mlx
Text Generation
•
6B
•
Updated 3 days ago
•
152
Brooooooklyn/Qwen3.5-9B-UD-Q8_K_XL-mlx
Text Generation
•
3B
•
Updated 3 days ago
•
155
Brooooooklyn/Qwen3.5-9B-UD-Q6_K_XL-mlx
Text Generation
•
3B
•
Updated 3 days ago
•
86
Brooooooklyn/Qwen3.5-35B-A3B-UD-Q5_K_XL-mlx
Text Generation
•
8B
•
Updated 3 days ago
•
295
•
1
Brooooooklyn/Qwen3.5-35B-A3B-UD-Q4_K_XL-mlx
Text Generation
•
7B
•
Updated 3 days ago
•
277
•
3
Brooooooklyn/Qwen3.5-35B-A3B-UD-Q3_K_XL-mlx
Text Generation
•
6B
•
Updated 3 days ago
•
205
•
1
Brooooooklyn/Qwen3.5-35B-A3B-UD-Q2_K_XL-mlx
Text Generation
•
4B
•
Updated 3 days ago
•
212
Brooooooklyn/Qwen3.5-35B-A3B-UD-Q8_K_XL-mlx
Text Generation
•
10B
•
Updated 3 days ago
•
135
•
1
Brooooooklyn/Qwen3.5-35B-A3B-UD-Q6_K_XL-mlx
Text Generation
•
9B
•
Updated 3 days ago
•
134
•
2
Impulse2000/Qwen3.5-9B-Neo-heretic
Text Generation
•
9B
•
Updated 3 days ago
•
459
Hunterx/Qwen3.5-40B-RoughHouse-Claude-4.6-Opus-oQ4NearLossless
Text Generation
•
7B
•
Updated 4 days ago
•
633
•
7
Hunterx/Qwen3.5-40B-RoughHouse-Claude-4.6-Opus-oQ2BENCHMARKED
Text Generation
•
5B
•
Updated 4 days ago
•
327
continuum-ai/qwen3.5-4b-code-forged-defragged
Text Generation
•
4B
•
Updated 4 days ago
•
736
continuum-ai/qwen3.5-27b-code-forged-mlx-4bit
Text Generation
•
14B
•
Updated 4 days ago
•
391
icecee/Qwen3.5-9B-Opus-S1M
Text Generation
•
10B
•
Updated 4 days ago
•
364
•
1
groxaxo/Huihui-Qwen3.5-9B-abliterated-GPTQ-Pro-4bit-g64
Text Generation
•
9B
•
Updated 4 days ago
•
23
System theme
TOS
Privacy
About
Careers
Models
Datasets
Spaces
Pricing
Docs

Gemini is AI and can make mistakes.

I’m narrowing the model list by cutting out HF long-tail noise and keeping only options that look plausible for your latency and concurrency target on prosumer hardware.
It’s already pointing the same way: for 8–16 way concurrency with sub-5s TTFT, dense 27B is usually the wrong default and the real candidates are mostly ~3B-active MoE/hybrid families. I’ve got the official bases pinned down and I’m now separating those from community REAP/distill uploads that are basically just flashy quant dumps.

https://huggingface.co/caiovicentino1/models?sort=least_params https://huggingface.co/caiovicentino1/models?sort=least_params https://huggingface.co/danielcherubini/Qwen3.5-DeltaCoder-9B-GGUF https://huggingface.co/Drjkedwards/Recursive-Transformer-Model https://huggingface.co/caiovicentino1/models?sort=least_params https://huggingface.co/bigatuna/Qwen3.5-9b-Sushi-Coder-RL-GGUF perhaps can do our own fine tunes\quants\adaptres and other items over a base model too if needed im open o renting or purchasing addtl gpu but note:

current spend is 600$ a month + assumed 50$ on HW; our daily usage on just CC (1 out of 5 harnesses) is approx 100-400Mtok of constant work, we will need to optimally cost match to the subscriptions which provide near 0.005$ mtok pricing.but do have lower rate limtits both in concurrency and volume take al pooka t teh models I've shown, the dense 27-72bs being REAP or in other ways cut down to3 -9b size seems like the move. REAP\distills ar not flashy, read the benchmarks and evaluate. and factor int hat one guys advice + the advice of each repo + their strategies, it can be concatenated into one LLM strategy thats unified, factor in ALL of our conversation memories too 

Two practical filters have emerged: ignore the 1080 Ti for a modern vLLM path, and treat many flashy HF REAP/distill uploads as fit/memory hacks unless they have real evals. For your box, the serious worker candidates are the official 30–35B A3B/REAP class—especially Qwen3.5-35B-A3B and GLM-4.7-Flash-REAP—while bigger Coder-Next variants look too uncomfortable on dual 24GB once concurrent KV cache is counted.

0.005 per million tokens! there are ways to merge hte 1080ti\3090ti. thought, also vllm vs sglang for out case

I’m folding your linked repos into a cost/perf pass now, but the frame has shifted: this is a serving-strategy problem first. I’m checking whether the REAP/distill/pruned variants have enough real provenance and eval signal to justify worker traffic, and whether their model shape, quant, and runtime can actually beat your current effective token cost at sustained load.

───┼──────────┼──────────┼───────────┼───────────┼──────────┤
│ 2026-01  │ - glm-4.7                                                               │ 2,211,3… │  341,315 │ 105,496… │ 2,936,23… │ 3,044,28… │  $744.82 │
│          │ - haiku-4-5                                                             │          │          │          │           │           │          │
│          │ - opus-4-5                                                              │          │          │          │           │           │          │
│          │ - sonnet-4-5                                                            │          │          │          │           │           │          │
├──────────┼─────────────────────────────────────────────────────────────────────────┼──────────┼──────────┼──────────┼───────────┼───────────┼──────────┤
│ 2026-02  │ - MiniMax-M2.1                                                          │ 195,664… │ 1,848,2… │ 227,353… │ 7,406,48… │ 7,831,35… │ $2617.00 │
│          │ - MiniMax-M2.5                                                          │          │          │          │           │           │          │
│          │ - gemini-3-flash                                                        │          │          │          │           │           │          │
│          │ - glm-4.7                                                               │          │          │          │           │           │          │
│          │ - glm-5                                                                 │          │          │          │           │           │          │
│          │ - haiku-4-5                                                             │          │          │          │           │           │          │
│          │ - opus-4-6                                                              │          │          │          │           │           │          │
│          │ - sonnet-4-5                                                            │          │          │          │           │           │          │
│          │ - sonnet-4-6                                                            │          │          │          │           │           │          │
├──────────┼─────────────────────────────────────────────────────────────────────────┼──────────┼──────────┼──────────┼───────────┼───────────┼──────────┤
│ 2026-03  │ - MiniMax-M2.7                                                          │ 5,182,4… │ 2,535,0… │ 349,791… │ 7,894,98… │ 8,252,49… │ $3132.65 │
│          │ - haiku-4-5                                                             │          │          │          │           │           │          │
│          │ - opus-4-6                                                              │          │          │          │           │           │          │
│          │ - sonnet-4-6                                                            │          │          │          │           │           │          │
├──────────┼─────────────────────────────────────────────────────────────────────────┼──────────┼──────────┼──────────┼───────────┼───────────┼──────────┤
│ 2026-04  │ - MiniMax-M2.7                                                          │ 4,572,5… │   48,075 │ 8,958,7… │ 65,785,5… │ 79,364,9… │    $0.00 │
├──────────┼─────────────────────────────────────────────────────────────────────────┼──────────┼──────────┼──────────┼───────────┼───────────┼──────────┤
│ Total    │                                                                         │ 207,630… │ 4,772,6… │ 691,600… │ 18,303,4… │ 19,207,4… │ $6494.46 │
└──────────┴─────────────────────────────────────────────────────────────────────────┴──────────┴──────────┴──────────┴───────────┴───────────┴──────────┘
   ~/C/P/repos   main  $ 5󰃭 132✓   v22.22.2   v1.96.0-nightly  for 1 out of 5 harnesses.

The economics are becoming the hard gate now: at a true $0.005 per million tokens target, only extremely high

VPS options for 64GB RAM
·
13m 38s

Pro thinking
Quick answer
Exploring model and hosting options for user
Okay, the user seems to be asking for advice on AI models and hosting, particularly around options with home GPUs like a 3090ti. I need to look up the latest models and benchmarks, such as variants of Qwen3.5 or smaller models under 32b. I'll also consider server and GPU mesh alternatives. Let me find current information.
Gathering benchmarks and comparisons for models
I’ll need to
Looking for current models and performance
I should probably search for the latest information on current models and their performance, such as Qwen3.5 coder with a 27b variant. Let me look up this information to make sure I'm giving the most up-to-date and relevant details to the user about these models and their capabilities.
Searching the web for Qwen3.5 and related models
Looking for more precise model benchmarks
I should find more precise sources for benchmarks, maybe from the official Qwen blog. Comparing Qwen’s performance with other models would give a clearer picture. I'll search specifically for this kind of information to provide the most relevant and accurate comparison for the user.
Searching for official benchmarks of AI models
Searching for official Qwen benchmarks and hardware info
I should search for the official Qwen blog or documentation to find benchmarks and hardware requirements. That way, I can provide more precise technical details about the model's performance and the specs needed to run it efficiently. Let me find the official source for this information.
Searching for official Qwen blog and benchmarks
Searching for Qwen3.5 model card
I should search for the Qwen3.5 model card, which could provide useful technical details. It may not necessarily be from the official source, but I’ll still check for the most reliable information available on it. This should help clarify specs, performance, and other key details.
Searching for Qwen3.5 model card details
Looking for model and hardware support details
I need to check for official evaluation results on specific Qwen3 models like 3.5-27B and 3-Coder-30B-A3B-Instruct. I also want to find compatibility info for running them locally on GPUs, including hardware like the 3090ti and 1080Ti. I'll search for official vLLM support documentation and hardware compatibility.
Searching official docs for model and hardware support
Opening official model cards
I should open the official model cards to get clear details. Looking at those official sources should help clarify things like performance metrics and other specifics that will be useful here. This will guide me in providing more accurate information regarding the models.
Opening official model cards for sources
Exploring vLLM requirements and bf16
I need to look at the specific requirements for vLLM and analyze how bf16 fits into those. I'll search for relevant patterns in the official documentation, as that should help me understand if there are any compatibility issues or specific hardware needs I should consider.
Analyzing vLLM requirements and bf16 patterns
Looking up bf16 support in source code
I think it might be better to directly check the source code for bf16 support. If I look around where the term Bfloat16 appears in the source, I should be able to find the necessary lines regarding compatibility. I'll open the relevant sections to dig a bit deeper.
Searching for Bfloat16 support in source code
Searching for relevant phrase in the code
It seems I didn't quite find the exact lines I was aiming for. I should refine the search, maybe by looking for a specific phrase related to bf16 support. That way, I can directly target the relevant sections in the code and get the info I need more efficiently.
Finding missing targeted lines or related phrase
Looking for 3090Ti compute info
It looks like I should get some more specific information about the 3090Ti's compute capabilities. I could check out official NVIDIA pages, as they likely have accurate details. I’ll search their website to see if they provide the most up-to-date specs for that GPU model.
Searching for official NVIDIA 3090 Ti compute specs
Accessing official NVIDIA compute info
Looks like I can find the official compute capability information on NVIDIA's developer page. I'll open that source to gather reliable details. This should give me accurate and up-to-date specs for the GPU, especially the 3090Ti’s capabilities.
Verifying compute capability from NVIDIA developer resources
Searching for 1080 Ti legacy compute details
I need to find legacy compute capability info for the 1080 Ti. I'll look up the official developer sources to find the most accurate and reliable specifications for the GPU's performance capabilities. This should give me more context for the legacy hardware comparison.
Searching for 1080 Ti legacy developer resources
Searching for official model docs and benchmarks
I need to find official docs for GPT-5 mini, Claude Haiku, or similar models, like OpenRouter or Anthropic/OpenAI. Since the user uses these as a threshold for performance quality, I’ll either avoid comparing models directly or mention alternatives ranked by quality without making definitive claims. I’ll check out proper model cards and available third-party benchmarks.
Searching for official model cards for GLM-4.7-Flash
Searching for Qwen 3.5 model card
I should look for the official model card for Qwen 3.5, including its model overview and possibly benchmarks. I’ll focus on open information and any available resources, to make sure the user has accurate details without relying on proprietary sources.
Searching for Qwen3.5 model card and benchmarks
Searching for Qwen 3.5 benchmark results
I need to find benchmark results for Qwen 3.5, looking for open sources that provide some kind of performance analysis. I'll aim to gather details from around 100 benchmarks to give a broad overview without relying on any closed or proprietary sources.
Searching for Qwen3.5 benchmark result benchmarks
Looking for Qwen 3.5 benchmarks for 9B and 35B
I’m gathering official benchmark results around Qwen 3.5 for both the 9B and 35B models. I’ll focus on open sources that provide these specific details, aiming to find performance lines that accurately reflect the capabilities of these particular model sizes.
Searching for Qwen3.5 9B and 35B benchmarks
Searching for additional Qwen 3.5-27 benchmarks
It looks like I need to explore additional open benchmark results for Qwen 3.5-27, focusing on its performance in coding tasks. I'll aim to find more detailed performance lines that showcase its strengths and weaknesses in those areas, looking for relevant sources that approach this.
Exploring Qwen3.5-27 benchmarks and coding options
Searching for Qwen3-Coder 30B performance data
I’m considering checking for official performance benchmarks for the Qwen3-Coder 30B, especially focusing on coding tasks. I’ll look through official blog posts or model cards, especially from Huﬀman, for open lines around its performance. This will help clarify how the model handles coding scenarios effectively.
Searching for Qwen3-Coder 30B benchmark information
Looking for Qwen blog with benchmarks
I'm thinking I should check out the official Qwen blog to look for benchmarking details, especially related to Qwen3-Coder. I'd like to see if there’s any direct information on coding performance or other specifics in their latest updates, since it could give a clearer view of its capabilities.
Browsing for Qwen3-coder blog and benchmarks
Evaluating Qwen3.5, REAP models, and uncertainties
The Qwen blog doesn't mention the 30B version, but the official model card highlights strong performance. I might compare it to REAP variants and unofficial models like Flagstone Qwen3.5-18B-REAP. The user asked about similar models, but I should note sparse documentation for unofficial ones and keep the confidence low.
Searching Hugging Face for Qwen3.5-REAP model details
Caution with community models and distillations
I could explore community pages for a list of candidate models, like Jackrong 9B/27B/35B distillations. However, I need to be cautious as these distills likely aren't production-safe due to lack of official evaluation, chat template issues, and uncertainty around licensing and training provenance. I'll check model card notes.
Searching for distilled model card details and notes
Searching for Qwen3-Coder-Next model card
The user mentioned Qwen3-Coder-Next-REAP-48B-A3B quants, so I might need to search for the official Qwen3-Coder-Next model card. I’m wondering if such a model has an official release. I’ll search to find more details if available and see what comes up.
Searching for Qwen3-Coder-Next official model card
Looking for official Qwen3-Coder-Next card
I need to find the official Qwen3-Coder-Next model card. This will help me understand more about the model’s specifications and capabilities. I’ll see if I can access it directly so I can provide the user with the most accurate and reliable information.
Requesting Qwen3-Coder-Next card access
Assessing model and inference options for GPU worker nodes
I need to explore official inference frameworks and quantization options for models like Qwen3.5 27B or 35B with GPTQ Int4, considering VRAM and concurrency for a 3090Ti. The user seems to want a model suitable for 50%+ of requests with minimal response time. I'll recommend options that balance local and remote resources.
Exploring model size and performance impact for 27B vs 35B
I need to compare dense 27B vs active 35B A3B models and explore performance impacts from active parameters, such as inference and FLOPs. I'll estimate sizes and fit on the 3090Ti using model specs and available file sizes. I'll check for quantization info, specifically GPTQ Int4, to refine my search.
Searching model sizes and performance impacts for inference
Assessing model fit using file sizes
I might be able to infer whether the model fits based on file sizes from tree pages. To proceed, I'll open the Qwen3.5-35B-A3B-GPTQ Int4 model tree to check the details and estimate how well it would fit for the task at hand.
Inferring fit using file sizes and tree data
Looking for model size information
I need to check the bottom section, possibly around line 580, for any mention of "Model size." That should give me the specific details I’m looking for to assess if the model fits the requirements based on its size. Let's locate that and proceed accordingly.
Searching code for "Model size" reference
Estimating memory requirements for 3090Ti
I need sources for quant sizes/fit regarding 5090, but I’m mainly focused on whether the 3090Ti can fit 27B GPTQ int4 or 28B models, which might need around 15GB. I should check file sizes from the tree page and sum them up. Using a memory calculator could also help for assistance.
Searching for GPTQ model file sizes and fit
Searching for deployment compatibility and benchmarks
I need to find official and recent support for GLM REAP or Qwen3-Coder-Next with the vLLM version. I’ve got some of the information but still looking for a source on Kimi-Linear/REAP variant deployment compatibility and benchmarks. I’ll go ahead and search to find that.
Searching for Kimi-Linear REAP benchmarks and vLLM support
Comparing Qwen3.5 with GPT-5 mini/Claude Haiku
I’m comparing Qwen3.5-27B to GPT-5-mini and Claude Haiku, since official benchmarks show Qwen3.5-27B scores near GPT-5-mini. For code performance, Qwen3.5-27B beats GPT-5 mini on some tasks, but the user might care more about actual coding UX. I'll look at the blog and deployment details for more.
Evaluating model compatibility and hardware limitations for Qwen3.5 and 3090Ti
I’ll check if official vLLM supports models like Qwen3_next, Qwen3_5, Kimi_linear, and GLM4. Local single 3090Ti (24GB) won’t host Qwen3.5-27B-GPTQ-Int4 due to its 30.3GB size. So, I’ll need to search for smaller quantization models, especially for the 35B version or at least third-party optimizations.
Searching model support and quantization options for vLLM
Considering Qwen3-Coder and quantization options
I’ll mention the caution around 4-bit AWQ quantization, as it may cause a significant loss in quality, according to one third-party vendor. While using FP8 seems ideal, the 3090Ti doesn't support it. For a more reliable option, I might recommend standard 4-bit quantization, but with a note of caution based on vendor warnings. If considering distilled models, I'll also keep an eye on efficiency trade-offs like those from HumanEval.
Addressing experimental models and lack of rigorous evaluation
The user asked about this explicitly, so I’ll mention that the models are experimental due to the lack of formal cross-benchmark data and modified reasoning scaffolds. I'll cite open model cards that discuss their training approach. I'll clarify that there's limited official evaluation available, noting that most public cards share self-reported metrics instead.
Researching Qwen3 quantization and distillation options
Evaluating Qwen3-Coder-Next GPU and quantization options
I need to check if Qwen3-Coder-Next requires two GPUs, as the card suggests tensor parallel size 2 in vLLM. Full BF16 80B is too large for a 3090Ti, but maybe I can look into using REAP or quantization. The community-released 48B model might be relevant, so I'll check it out.
Searching for Qwen3-Coder-Next benchmarks and quantization
Reviewing model options for worker use case
It looks like the user wants help selecting a model for their worker use case, possibly to run on a local machine like a 3090 Ti, but they’re open to remote options as well. I'll focus on models with <32B parameters, Qwen3.5 Coder 27B, and REAP variants for their performance, taking care to compare them to GPT-5 Mini or Claude Haiku.
Searching for benchmarks and model comparisons
I should mention that there isn’t an exact apples-to-apples comparison with GPT-5 mini or Claude Haiku publicly available, and real benchmarking is needed. I’ll aim to ensure factual claims are properly cited, and I might need to search for more model-specific details from official Qwen sources, particularly for Qwen3-Coder-30B.
Reviewing worker model options and benchmarks
Looking for official benchmarks on Qwen3-Coder
I should check if the Qwen3-Coder blog includes comparisons against models like Claude Sonnet. While I can use search snippets, it’d be better to open the website directly for more precise information and benchmarks. Let me search and open it for a closer look.
Opening Qwen3-Coder blog for benchmarks and citations
Clarifying worker model and model references
I might mention that Qwen3-30B-A3B-Instruct-2507 is better for speed due to its non-thinking approach, while Qwen3's hybrid thinking could be useful but not ideal for this worker. Although I don’t need citations for some of the community models mentioned, I’ll note the lack of evaluations for some of them.
Searching for Qwen3 model cards and community distills
Evaluating model comparisons for GPT-5 mini and Claude Haiku
The user wants a comparison to GPT-5 mini and Claude Haiku. For GPT-5 mini, I can cite the Qwen3-27B benchmark which includes comparison data. For Claude Haiku, it's trickier, but I could use vendor documents if they provide benchmark numbers, especially for quality.
Clarifying model comparison and support for Qwen3 and Claude Haiku
I couldn’t find a reliable apples-to-apples public comparison for Claude Haiku in the sources I checked, so I won’t claim that. However, Qwen’s blog mentions its larger 480B model being comparable to Claude Sonnet 4. I can share that to give context. Also, mentioning vLLM support might help.
Looking into community benchmarks and model cards
I could focus on community sources for now. It might be worth checking if a model card includes benchmarks, so I’ll do that search. I could also check the RepublicOfKorokke to see if there’s relevant information there.
Searching for model comparisons and benchmark sources
Considering model details and sources
The community model results don’t offer much beyond basic information. I can mention the sizes for the Flagstone Qwen3.5-18B-REAP model, noting it fits on a 24 GB card at Q6/Q8 settings. I'll also clarify it as a community fine-tuned version of Qwen3.5-35B-A3B, no need for further searches unless necessary.
Focusing on authoritative sources and structuring the answer
I’ll stick to citations from authoritative sources for reliability. While snippets from sites like HF are okay for discussing model sizes and dates, most citations should come from official model cards, documentation, or reputable blogs. The final answer could include stack-ranking models to clarify throughput, size, and hardware options for the user.
Ranked shortlist for model recommendations
Here’s a ranked shortlist based on my analysis:
Best official worker under 32B: GLM-4.7-Flash-REAP-23B-A3B
Best coder-first worker: Qwen3-Coder-30B-A3B-Instruct for remote, 15B-A3B REAP for community
Best generalist worker: Qwen3-30B-A3B-Instruct-2507
Best fallback for dense tasks: Qwen3.5-27B
Best for small overflow: Qwen3.5-9B or Jackrong 9B for experiments
Avoid using Kimi-Linear-REAP-35B-A3B as primary unless you need long context. Qwen3-1.7B is too small for the task.
Determining what models fit on a 3090 Ti
On a 3090 Ti, the official 30B and 27B models, as well as the 35B-A3B, won’t fit due to their size. However, smaller models like the 9B class or community-compressed models (e.g., Flagstone 18B REAP GGUF or RepublicOfKorokke 48B-A3B oQ3) should work, though these are experimental. I could check model sizes for more precise citations.
Ranking and selecting AI models for tasks
Considering benchmarks, performance, and model fit
The Qwen3.5-27B dense model seems the closest open model that directly matches GPT-5 mini on coding benchmarks. For latency or concurrency, MoE models like the 30B may still perform better despite raw scores being lower. However, aligning production priorities like tool behavior and endpoint engineering matter — it's nuanced, so no citations needed.
Searching official sources for GPT-5 mini
Since the user mentioned GPT-5 mini, it seems safer to search for official OpenAI documentation to ensure accuracy when discussing or comparing the model. Even if the user isn’t asking about using OpenAI products, it's better to reference reliable sources for clarity. I'll search now.
Searching for official GPT-5 mini documentation
Clarifying GPT-5 mini and GPT-5.4 mini
While GPT-5 mini is a previous low-latency model, OpenAI now recommends GPT-5.4 mini for new high-volume, low-latency tasks. However, since the user mentioned their performance target should be comparable to GPT-5 mini or Claude Haiku, I'll focus on that in my response but add context about GPT-5.4 mini for clarity.
Considering Claude Haiku for context
Since the user mentioned Claude Haiku alongside GPT-5 mini, I could search for the latest benchmarks for Haiku, but I don't necessarily need to reference it explicitly. Instead, I could just mention, "I didn't verify primary-source benchmarks." The comparison is still important, so browsing for clarity seems like the best option.
The user wants to review the specified Hugging Face models—including various Qwen3.5 and Recursive Transformer models focused on smaller parameter sizes—and consider performing their own fine-tuning, quantization, adapter residual tuning, or other modifications on base models if needed. They are open to renting or purchasing additional GPUs. Their current monthly expenditure is about $600 plus approximately $50 for hardware, with daily usage on one compute cluster harness ranging from 100 to 400 million tokens of continuous workload. They aim to optimize costs to match subscription services offering roughly $0.005 per thousand tokens, despite those subscriptions having lower concurrency and volume limits. The user requests an evaluation and benchmarking of the referenced models, especially smaller dense or distilled variants trimmed from 27-72 billion parameter models down to 3-9 billion sizes (e.g., REAP and distills), integrating advice from various repos and community strategies into a unified large language model approach that also incorporates all prior conversation context.
The user wants to explore options to achieve a cost of $0.005 per million tokens, consider methods to combine their 1080ti and 3090ti GPUs, and evaluate the suitability of vLLM versus SGLang for their use case.
Searching for Claude Haiku benchmark information
The user wants to analyze and interpret a detailed usage and cost table for multiple AI models over several months, focusing on token consumption and related expenses for one out of five processing harnesses.

## Response:
4/1/2026, 4:16:47 AM

I’m cutting this into three pieces: official bases worth trusting, community REAP/distill variants that might be useful but are still risky, and the serving/runtime economics on your actual hardware. Then I’ll turn that into a concrete routing recommendation instead of a giant model dump.

The picture is getting cleaner. The official MoE bases are real contenders; the community REAP/distill zoo is mostly useful as an experiment pool, not as something I’d trust for 50%+ of production worker traffic without your own eval harness.

> **Searching for official model cards and documentation**
>
> [Qwen/Qwen3.5-27B](https://huggingface.co/Qwen/Qwen3.5-27B)
> [Cerebras/Kimi-Linear-REAP-35B-A3B-Instruct · Hugging ...](https://www.reddit.com/r/LocalLLaMA/comments/1or46rv/cerebraskimilinearreap35ba3binstruct_hugging_face/)
> [Qwen3.5 is the large language model series ...](https://github.com/QwenLM/Qwen3.5)
>
> **Searching for vLLM and SGLang documentation**
>
> [Supported Models - vLLM](https://docs.vllm.ai/en/latest/models/supported_models/)
> [Supported Models - SGLang](https://sgl-project-sglang-93.mintlify.app/models/supported-models)
> [SGLang Documentation — SGLang](https://sgl-project.github.io/)
> [PD Disaggregation - sgl-project/sglang](https://github.com/sgl-project/sglang/blob/main/docs/advanced_features/pd_disaggregation.md)
> [OpenAI Compatible Server - vLLM! - Read the Docs](https://nm-vllm.readthedocs.io/en/0.4.0/serving/openai_compatible_server.html)
> [Disaggregation | NVIDIA Dynamo Documentation](https://docs.nvidia.com/dynamo/dev/backends/sg-lang/disaggregation)
> [LLM distributed inference and PD disaggregation on AMD ...](https://rocm.docs.amd.com/projects/ai-developer-hub/en/latest/notebooks/inference/SGlang_PD_Disagg_On_AMD_GPU.html)
> [Qwen3-Coder-Next: The Complete 2026 Guide to Running ...](https://dev.to/sienna/qwen3-coder-next-the-complete-2026-guide-to-running-powerful-ai-coding-agents-locally-1k95)
> [vLLM server arguments | Red Hat AI Inference Server | 3.0](https://docs.redhat.com/en/documentation/red_hat_ai_inference_server/3.0/html-single/vllm_server_arguments/index)
> [SGLang HiCache: Fast Hierarchical KV Caching with Your ...](https://lmsys.org/blog/2025-09-10-sglang-hicache/)
> [Blown Away By Qwen 3.5 35b A3B : r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/comments/1re17th/blown_away_by_qwen_35_35b_a3b/)
>
> **Searching for OpenAI official documentation**
>
> [GPT-5 mini Model | OpenAI API](https://developers.openai.com/api/docs/models/gpt-5-mini)
> [Claude Haiku 4.5](https://www.anthropic.com/claude/haiku)
> [Introducing GPT-5.4 mini and nano](https://openai.com/index/introducing-gpt-5-4-mini-and-nano/)
> [Models overview - Claude API Docs](https://docs.anthropic.com/en/docs/about-claude/models)
> [Introducing GPT-5.4 mini and nano — our most capable ...](https://community.openai.com/t/introducing-gpt-5-4-mini-and-nano-our-most-capable-small-models-yet/1377015)
>
> **Searching for NVIDIA GPU compute capability information**
>
> [CUDA GPU Compute Capability](https://developer.nvidia.com/cuda/gpus)
> [Support Matrix — NVIDIA TensorRT](https://docs.nvidia.com/deeplearning/tensorrt/latest/getting-started/support-matrix.html)
> [3090 & 3090 Ti Graphics Cards | NVIDIA GeForce](https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3090-3090ti/)
> [INT4 support for Ampere - TensorRT](https://forums.developer.nvidia.com/t/int4-support-for-ampere/158966)
> [GeForce RTX 30 series](https://en.wikipedia.org/wiki/GeForce_RTX_30_series)
> [Support Matrix — TensorRT-LLM](https://nvidia.github.io/TensorRT-LLM/reference/support-matrix.html)
>
> **Finding specific model cards and related pages**
>
> [Qwen/Qwen3.5-27B · Hugging Face](https://huggingface.co/Qwen/Qwen3.5-27B)
> [GPT-5 mini Model | OpenAI API](https://developers.openai.com/api/docs/models/gpt-5-mini)
> [Claude Haiku 4.5 \ Anthropic](https://www.anthropic.com/claude/haiku)
> [Supported Models - vLLM](https://docs.vllm.ai/en/latest/models/supported_models/)
> [Supported Models - SGLang](https://sgl-project-sglang-93.mintlify.app/models/supported-models)
> [SGLang Documentation — SGLang](https://sgl-project.github.io/)
> [CUDA GPU Compute Capability | NVIDIA Developer](https://developer.nvidia.com/cuda/gpus)
>
> **Looking at patterns for 3090Ti and 1080Ti lines**
>
> I need to check out lines for both the 3090Ti and the 1080Ti and see if there's a pattern I can spot. I might compare their specs or pricing trends to understand the differences better. Let’s dive into these and analyze what stands out.
>
> **Finding patterns in 3090Ti and 1080Ti lines**
>
> [CUDA GPU Compute Capability | NVIDIA Developer](https://developer.nvidia.com/cuda/gpus)
> [Supported Models - vLLM](https://docs.vllm.ai/en/latest/models/supported_models/)
> [Supported Models - SGLang](https://sgl-project-sglang-93.mintlify.app/models/supported-models)
>
> **Looking at Qwen benchmark patterns**
>
> I think I need to check out Qwen benchmark lines within the model cards. I'll be looking for patterns there—especially for something like HumanEval. I'm curious if I can spot any consistent trends or comparisons that might help clarify performance insights across different models. Let's see how this goes!
>
> **Searching for Qwen benchmarks and HumanEval patterns**
>
> [Qwen/Qwen3-Coder-30B-A3B-Instruct · Hugging Face](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct)
>
> **Looking for Qwen3.5-35B-A3B model card**
>
> I think I might need the official model card for Qwen3.5-35B-A3B so I can compare it effectively. I’ll search for it and see if I can find the detailed info that would help me make a meaningful comparison against other models. It could give me exactly what I need!
>
> **Searching for Qwen3.5 and Qwen3 model cards**
>
> [Qwen/Qwen3.5-35B-A3B](https://huggingface.co/Qwen/Qwen3.5-35B-A3B)
> [Comparative Analysis: Qwen3 30B A3B Instruct 2507 vs. ...](https://blog.galaxy.ai/compare/qwen3-30b-a3b-instruct-2507-vs-qwen3-vl-30b-a3b-instruct)
> [Qwen3 30B A3B 2507 (Reasoning) vs ...](https://artificialanalysis.ai/models/comparisons/qwen3-30b-a3b-2507-reasoning-vs-qwen3-30b-a3b-2507)
> [Qwen3: Think Deeper, Act Faster](https://qwenlm.github.io/blog/qwen3/)
> [Qwen/Qwen3-30B-A3B-Instruct-2507 · Hugging Face](https://www.reddit.com/r/LocalLLaMA/comments/1mb9uy8/qwenqwen330ba3binstruct2507_hugging_face/)
>
> **Looking for Qwen3.5-35B-A3B details**
>
> I think I need to check out the Qwen3.5-35B-A3B details. I’m not sure exactly what I’ll find, but seeing the model’s overview might give me useful info. This could help me understand more about its features and performance, so I’ll check for a good source right now.
>
> **Searching for Qwen3.5-35B-A3B view**
>
> [Qwen/Qwen3.5-35B-A3B · Hugging Face](https://huggingface.co/Qwen/Qwen3.5-35B-A3B)
> [Introducing GPT-5.4 mini and nano | OpenAI](https://openai.com/index/introducing-gpt-5-4-mini-and-nano/)
> [Introducing Claude Haiku 4.5 \ Anthropic](https://www.anthropic.com/news/claude-haiku-4-5)
>
> **Looking up Qwen3.5-35 and Qwen3-30B benchmarks**
>
> I might need to find the benchmark information for Qwen3.5-35 and Qwen3-30B-2507 models to compare their performance. I’ll search for these benchmark lines and check where I can find reliable details on their results. This could be critical for understanding their strengths and weaknesses.
>
> **Searching for Qwen3.5-35 and Qwen3-30B benchmarks**
>
> [Qwen/Qwen3.5-35B-A3B · Hugging Face](https://huggingface.co/Qwen/Qwen3.5-35B-A3B)
>
> **Searching for official Qwen3.5-9B model details**
>
> [Qwen/Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B)
> [Qwen/Qwen3.5-9B · Hugging Face : r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/comments/1rirlyb/qwenqwen359b_hugging_face/)
> [Qwen3.5 is the large language model series ...](https://github.com/QwenLM/Qwen3.5)
> [Qwen3.5: Towards Native Multimodal Agents](https://qwen.ai/blog?id=qwen3.5)
>
> **Looking at Qwen3.5-9B and blog summaries**
>
> I should open the Qwen3.5-9B details to gather more insights. It might help to also check out any relevant blog posts for a summary of its performance and features. Getting a clear overview of these could offer some valuable context for comparison. Let’s dive in!
>
> **Opening Qwen 3.5-9B and summarizing blog**
>
> [Qwen/Qwen3.5-9B · Hugging Face](https://huggingface.co/Qwen/Qwen3.5-9B)
> [Qwen](https://qwen.ai/blog?id=qwen3.5)
>
> **Looking into community model evidence**
>
> I think we have enough info for now, but it might help to mention evidence from community model cards. I should search for specifics on Jackrong, Bigatuna, DeltaCoder, and REAP Smalls. These might provide additional insights that could strengthen the overall understanding of the models.
>
> **Searching for community model documentation and evidence**
>
> [Jackrong/Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled)
>
> **Looking for Qwen3-Coder blog and comparisons**
>
> I’m thinking it might be useful to find a blog on Qwen3-Coder, particularly focusing on performance comparisons. That could give a clearer picture of how it stacks up against similar models. I'll search for it and see if I can find some relevant insights from there.
>
> **Searching for Qwen3-Coder benchmarks and blog posts**
>
> [Qwen/Qwen3-Coder-30B-A3B-Instruct](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct)
> [Qwen3: Think Deeper, Act Faster](https://qwenlm.github.io/blog/qwen3/)
> [Finally got Qwen3-Coder-30B-A3B running well. What ...](https://www.reddit.com/r/LocalLLaMA/comments/1n5iiay/finally_got_qwen3coder30ba3b_running_well_what/)
> [Qwen3-Coder-Next: Pushing Small Hybrid Models](https://qwen.ai/blog?id=qwen3-coder-next)
> [Qwen3 Coder 30B A3B Instruct - API Pricing & Providers](https://openrouter.ai/qwen/qwen3-coder-30b-a3b-instruct)
> [qwen3-coder](https://lmstudio.ai/models/qwen3-coder)
> [Qwen3-Coder, An Open-Weight Agentic Coding Model](https://www.digitalocean.com/community/tutorials/qwen3-coder-agentic-coding-model)
> [Qwen3-Coder is the code version of ...](https://github.com/QwenLM/Qwen3-Coder)
> [Install Qwen3-Coder-30B Flash Locally with Agentic ...](https://www.youtube.com/watch?v=IaqzrByS8yA)
> [Qwen: Qwen3 Coder 30B A3B Instruct](https://designforonline.com/ai-models/qwen-qwen3-coder-30b-a3b-instruct/)
> [TDAD: Test-Driven Agentic Development - Reducing Code Regressions in AI Coding Agents via Graph-Based Impact Analysis](https://arxiv.org/abs/2603.17973)
>
> Thought for 1m 18s

You’re directionally right about the shape of the solution, but not about all of the candidates.

The main takeaway is this: for a **worker model** that handles **50%+ of requests**, targets roughly **50–100 tok/s**, keeps **TTFT under ~5s**, and serves **8–16 concurrent requests**, the winning class is **not** “dense 27B by default.” It is mostly **~3B-active MoE / hybrid models** with strong tool behavior, plus a small dense fallback tier. The official cards and docs support that framing: Qwen’s 30B-A3B coder model is only **3.3B activated parameters** with **262k native context**, and Qwen/Cerebras both explicitly ship these MoE/REAP variants for vLLM/SGLang deployment. [Hugging Face+4Hugging Face+4Hugging Face+4](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct)

My blunt recommendation:

**Primary local worker lane**  
Use **Qwen3-Coder-30B-A3B-Instruct** as the main coding-oriented worker candidate to beat first. It is the cleanest official open model in your target class: **30.5B total / 3.3B active**, **262,144 native context**, explicitly built for **agentic coding**, browser use, function calling, and OpenAI-compatible serving. [Hugging Face+2Hugging Face+2](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct)

**Primary general worker lane**  
Use **Qwen3-30B-A3B-Instruct-2507** as the non-thinking general worker candidate. Same **3.3B active** MoE profile and 262k native context, but better positioned as a general low-latency worker than a specialized coder-only lane. [Hugging Face](https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507)

**Strong “official compressed” contender**  
Use **GLM-4.7-Flash-REAP-23B-A3B** as the most serious REAP candidate in the set you showed. Unlike random community prunes, this one has an official card, explicit REAP description, deployment notes, and published benchmark deltas showing it stays close to the base while being **25% lighter**, with **23B total / 3B active**, **202,752 context**, and direct vLLM deployment guidance. [Hugging Face](https://huggingface.co/cerebras/GLM-4.7-Flash-REAP-23B-A3B)

**Long-context specialist, not default worker**  
Treat **Kimi-Linear-REAP-35B-A3B-Instruct** as a specialist, not your default workhorse. Its official card says **35B total / 3B active**, **1,048,576 context**, and near-base performance after **30% pruning**. That’s compelling for repository-scale or retrieval-heavy jobs, but the hybrid linear-attention path makes it more of a niche lane than the safest “50% of traffic” default. [Hugging Face+1](https://huggingface.co/cerebras/Kimi-Linear-REAP-35B-A3B-Instruct)

**Dense fallback**  
Keep **Qwen3.5-27B** as a quality fallback, not as the main cheap worker. Its own official benchmark table is very strong: **72.4 SWE-bench Verified**, **41.6 Terminal Bench 2**, **80.7 LiveCodeBench v6**. But dense 27B is the wrong first choice when your actual constraint is throughput-at-scale under prosumer hardware. [Hugging Face](https://huggingface.co/Qwen/Qwen3.5-27B)

**Do not trust as primary production worker without your own evals**  
Most of the community REAP/distill uploads you listed. Some may be useful, but they are usually missing one or more of: rigorous public evals, strong provenance, stable chat templates, tool-calling guarantees, or enough evidence beyond a model card claim. A good example: the Flagstone 18B REAP GGUF is popular and small enough to be tempting, but the page literally says **“No model card.”** That is not something I’d route 50% of prod traffic to. [Hugging Face](https://huggingface.co/Flagstone8878/Qwen3.5-18B-REAP-A3B-Coding-GGUF?utm_source=chatgpt.com)

On the smaller dense side, **Qwen3.5-9B** is more credible than most of the 9B community variants because it is official, has native long context, and its own benchmark table is surprisingly strong for size. But its coding numbers are still notably below the larger official coder/MoE options: **65.6 LiveCodeBench v6** and **29.2 OJBench** on the official card. That makes it a good overflow / cheap utility worker, not your core worker if the bar is “comparable to GPT-5 mini / Haiku class.” [Hugging Face](https://huggingface.co/Qwen/Qwen3.5-9B)

On the “comparable to GPT-5 mini / Claude Haiku” target:

That bar moved. OpenAI now says **for new low-latency, high-volume workloads, start with GPT-5.4 mini**, and OpenAI positions it as their strongest mini for coding/subagents. Anthropic positions **Claude Haiku 4.5** as its fastest/cost-efficient model, with **73.3% SWE-bench Verified** and subagent focus. So your target is not yesterday’s mini tier anymore; it is basically “can an open worker model feel competitive with today’s fast subagent class?” [Anthropic+3OpenAI Developers+3OpenAI+3](https://developers.openai.com/api/docs/models/gpt-5-mini)

That means:

*   **Qwen3.5-27B dense** is quality-credible.
*   **Qwen3-Coder-30B-A3B** is the best official open candidate for the **worker** role.
*   **GLM-4.7-Flash-REAP-23B-A3B** is the most credible “compressed REAP” challenger.
*   **Qwen3.5-9B / 4B** are secondary cheap lanes, not primary quality lanes. [Hugging Face+3Hugging Face+3Hugging Face+3](https://huggingface.co/Qwen/Qwen3.5-27B)

On your hardware:

Your **3090 Ti** is still the serious card. Your **1080 Ti** is not useless, but for a modern vLLM-first worker stack it is basically a sidecar, not a peer. NVIDIA’s official compute capability tables put **RTX 3090 Ti in CC 8.6** and **GTX 1080 Ti in CC 6.1**. That gap matters. The 3090 Ti is Ampere with far better support for the modern inference stack; the 1080 Ti is legacy Pascal. Mixing them into one clean modern serving path is usually more pain than value. Use the 1080 Ti only for side jobs, preprocess/offload experiments, or noncritical auxiliary inference. Do not architect your main worker lane around “3090 Ti + 1080 Ti mesh.” [NVIDIA Developer+1](https://developer.nvidia.com/cuda/gpus)

On runtime choice:

For your use case, **SGLang** has the more aggressive serving feature set on paper for scale work: RadixAttention prefix caching, prefill/decode disaggregation, continuous batching, quantization support, multi-LoRA batching, and router support around PD disaggregation. **vLLM** is still the safer baseline because it has the broadest deployment familiarity, OpenAI-compatible serving, strong throughput features, speculative decoding, chunked prefill, and clear support for Qwen3/Qwen3.5 families. [vLLM+4SGLang Documentation+4GitHub+4](https://sgl-project.github.io/)

My practical call:  
Start with **vLLM first**, because it is the lower-risk path for your first serious worker deployment. Then only move a lane to **SGLang** if your measured bottleneck is specifically around high concurrency, KV reuse, or prefill/decode separation. For your stack, “vLLM baseline, SGLang optimization pass later” is the sane order. [vLLM+2GitHub+2](https://docs.vllm.ai/en/stable/serving/openai_compatible_server/?utm_source=chatgpt.com)

On the community models you named:

I would bucket them like this.

**Worth testing, but not trusting by default**  
Jackrong distilled variants, Neo variants, Sushi-Coder-RL, DeltaCoder, REAP-pruned community merges. Their cards often describe training ideas or sample counts, but that is not enough. For example, Jackrong’s 9B distilled card says it is based on Claude 4.6 Opus CoT distillation, and v2 says it used **14,000 samples** with an emphasis on concise reasoning transfer. That makes it interesting. It does **not** make it production-proven. [Hugging Face+1](https://huggingface.co/Jackrong/Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled?utm_source=chatgpt.com)

**Useful because they are small / easy to fit**  
Flagstone 18B REAP GGUF, LM Studio / MLX / GGUF ports, Sushi-Coder RL quants. These are deployment conveniences or experiment candidates, not strategic truth. [Hugging Face+2Hugging Face+2](https://huggingface.co/bigatuna/Qwen3.5-9b-Sushi-Coder-RL-GGUF?utm_source=chatgpt.com)

Your cost target is the hard part.

A real target of **$0.005 per 1M tokens** is brutal. That is so low that the problem is not just model choice; it is a full **serving strategy** problem. OpenAI’s current small-model API pricing is still far above that for strong workers: **GPT-5.4 mini is $0.75 / 1M input and $4.50 / 1M output**. Claude Haiku 4.5 is **$1 / 1M input and $5 / 1M output**. So if you really want an effective cost floor near that level, you only get there with **local serving + very high utilization + aggressive prefix caching / batching / routing discipline**. [OpenAI+1](https://openai.com/index/introducing-gpt-5-4-mini-and-nano/)

So the unified strategy I’d use for you is:

1.  **Planner/judge lane stays cloud.**  
    Keep a stronger frontier model for planning, triage, final review, and escalation.
2.  **Main worker lane goes local MoE.**  
    First candidate: **Qwen3-Coder-30B-A3B-Instruct**.  
    Second candidate: **GLM-4.7-Flash-REAP-23B-A3B**.  
    Third candidate: **Qwen3-30B-A3B-Instruct-2507**.
3.  **Cheap overflow lane goes small dense.**  
    Official **Qwen3.5-9B** first.  
    Community 9B distills only after your own harness proves they win.
4.  **Specialist long-context lane is optional.**  
    **Kimi-Linear-REAP-35B-A3B** only if your traces show long-context retrieval/codebase navigation is the actual bottleneck.
5.  **Do not base architecture on the 1080 Ti.**  
    Base it on the 3090 Ti. Treat the 1080 Ti as gravy.
6.  **Benchmark by role, not by leaderboard alone.**  
    Your evaluation set should include:  
    coding agent tasks,  
    tool-call correctness,  
    patch regression rate,  
    repository navigation,  
    long-context repo comprehension,  
    and concurrency collapse behavior at 8/12/16 simultaneous requests.

The ranking I’d start with is:

**Best first production candidate:** Qwen3-Coder-30B-A3B-Instruct. [Hugging Face+1](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct)  
**Best official compressed alternative:** GLM-4.7-Flash-REAP-23B-A3B. [Hugging Face](https://huggingface.co/cerebras/GLM-4.7-Flash-REAP-23B-A3B)  
**Best general low-latency non-coder worker:** Qwen3-30B-A3B-Instruct-2507. [Hugging Face](https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507)  
**Best dense fallback quality lane:** Qwen3.5-27B. [Hugging Face](https://huggingface.co/Qwen/Qwen3.5-27B)  
**Best cheap official overflow lane:** Qwen3.5-9B. [Hugging Face](https://huggingface.co/Qwen/Qwen3.5-9B)  
**Best specialist long-context experiment:** Kimi-Linear-REAP-35B-A3B-Instruct. [Hugging Face+1](https://huggingface.co/cerebras/Kimi-Linear-REAP-35B-A3B-Instruct)

What I would **not** do:  
I would not route half your traffic to random HF REAP/distill uploads just because they compress a 27–72B class model down to a friendly size. Some may be good. But the public evidence is too uneven, and your workload is too large and too expensive to let vibes pick the worker core. [Hugging Face+1](https://huggingface.co/Flagstone8878/Qwen3.5-18B-REAP-A3B-Coding-GGUF?utm_source=chatgpt.com)

If you want, the next useful step is for me to turn this into a concrete bake-off matrix: **model × quant × runtime × expected fit on 3090 Ti × likely concurrency lane × pass/fail criteria for your harnesses**.

---

**Sources:**

- [Qwen/Qwen3-Coder-30B-A3B-Instruct · Hugging Face](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct)
- [GPT-5 mini Model | OpenAI API](https://developers.openai.com/api/docs/models/gpt-5-mini)
- [CUDA GPU Compute Capability | NVIDIA Developer](https://developer.nvidia.com/cuda/gpus)
- [SGLang Documentation — SGLang](https://sgl-project.github.io/)
- [OpenAI-Compatible Server - vLLM](https://docs.vllm.ai/en/stable/serving/openai_compatible_server/?utm_source=chatgpt.com)
- [Introducing GPT-5.4 mini and nano | OpenAI](https://openai.com/index/introducing-gpt-5-4-mini-and-nano/)

## Prompt:
4/1/2026, 4:26:00 AM

its a model that works in Claude Code though so must be highly skamrt , note 4.7\qwen3 are out of date (glm 5.1, qwen3.6 just released but only latest glm 4.7\qwen3.5 avail on hf afaik.) 9b performs better than 4.7 flash afaik though...  research more models and options again 24gb + 16gb + VAST.ai, + 16gb MacBook that can be used for hyper small task runs (e.g. 3 layer hw decision? minimization of gpu rentals? and subscription usage? dont worry about llm router for intelligence omni router I think is hte MVP we'll sue and eidt) plz also factor https://chatgpt.com/share/69cd00a0-4bbc-832c-b26c-4e94608de24b https://chatgpt.com/share/69cd00a0-4bbc-832c-b26c-4e94608de24b

## Response:
4/1/2026, 4:26:02 AM

I’m re-doing this with the newer model generation and with your actual deployment ladder in mind: 24 GB desktop GPU, 16 GB add-on GPU, 16 GB M1 Pro laptop, and burst capacity on Vast. The key question now is not just “best model,” it’s which models belong on each hardware tier so rentals only kick in when the local boxes genuinely lose.

A few corrections are already clear. “Works in Claude Code” does **not** prove frontier-level intelligence by itself; vLLM’s own docs say the hard requirement is mainly **strong tool calling plus the right parser/serving compatibility**. That still matters a lot, but it’s not the same thing as “safe to route half your traffic to it.” [vLLM](https://docs.vllm.ai/en/stable/serving/integrations/claude_code/)

> **Searching for latest Qwen3.6, GLM5.1, and Claude info**
>
> [Anthropic leaked 500,000 lines of its own source code](https://www.axios.com/2026/03/31/anthropic-leaked-source-code-ai)
> [Anthropic accidentally exposed part of Claude Code's internal source code](https://www.businessinsider.com/anthropic-leak-reveals-claude-code-internal-source-code-2026-3)
> [Anthropic gives Claude Code new 'auto mode' which lets it choose its own permissions](https://www.techradar.com/pro/anthropic-gives-claude-code-new-auto-mode-which-lets-it-choose-its-own-permissions)
> [Anthropic's Claude Code gets 'safer' auto mode](https://www.theverge.com/ai-artificial-intelligence/900201/anthropic-claude-code-auto-mode)
> [Qwen3](https://qwen.ai/blog?id=qwen3)
> [Use third-party and local models | AI Assistant](https://www.jetbrains.com/help/ai-assistant/use-custom-models.html)
> [GPU Pricing — Live Marketplace Rates](https://vast.ai/pricing?srsltid=AfmBOopGv7K80Zc8T8xNc3e5rzybm493n9fQvjM9JGHEI_z8I_d4po2V)
> [The Big LLM Architecture Comparison - Ahead of AI](https://magazine.sebastianraschka.com/p/the-big-llm-architecture-comparison)
> [OpenAI Compatible Providers](https://ai-sdk.dev/providers/openai-compatible-providers)
> [Model list](https://www.alibabacloud.com/help/en/model-studio/models)
> [Anthropic Claude models - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-claude.html)
> [RTX 3090 Cloud Pricing: Compare 5+ Providers (2026)](https://getdeploying.com/gpus/nvidia-rtx-3090)
> [China's AI Giants Unveil Qwen-3.5 and New Models in ...](https://www.indexbox.io/blog/chinas-ai-giants-unveil-qwen-35-and-new-models-in-2026-race/)
> [GLM-5: From Vibe Coding to Agentic Engineering](https://z.ai/blog/glm-5)
> [Claude Code - vLLM](https://docs.vllm.ai/en/stable/serving/integrations/claude_code/)
> [NVIDIA RTX 3090: Pricing, Specs, Best Uses & Where to ...](https://www.fluence.network/blog/nvidia-rtx-3090/)
> [How to Fine-Tune Qwen3-VL on Your Own Dataset](https://datature.io/blog/how-to-fine-tune-qwen3-vl-on-your-own-dataset)
> [zai-org/GLM-5](https://huggingface.co/zai-org/GLM-5)
> [shantoislamdev/claude-adapter](https://github.com/shantoislamdev/claude-adapter)
> [7 cheapest cloud GPU providers in 2026 | Blog](https://northflank.com/blog/cheapest-cloud-gpu-providers)
>
> **Searching for official open pages**
>
> [z.ai](https://z.ai/blog/glm-5)
> [zai-org/GLM-5 · Hugging Face](https://huggingface.co/zai-org/GLM-5)
> [Claude Code - vLLM](https://docs.vllm.ai/en/stable/serving/integrations/claude_code/)
> [Qwen](https://qwen.ai/blog?id=qwen3)
> [GPU Pricing — Live Marketplace Rates | Vast.ai](https://vast.ai/pricing?srsltid=AfmBOopGv7K80Zc8T8xNc3e5rzybm493n9fQvjM9JGHEI_z8I_d4po2V)
>
> **Searching for Qwen3.5 and Qwen3.6 resources**
>
> [Qwen3](https://qwen.ai/blog?id=qwen3)
> [Qwen/Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B)
> [ml-explore/mlx-lm: Run LLMs with MLX](https://github.com/ml-explore/mlx-lm)
> [SGLang vs vLLM: Complete LLM Inference Engine ...](https://localaimaster.com/blog/sglang-vs-vllm-comparison)
> [Blog](https://qwenlm.github.io/blog/)
> [MLX](https://opensource.apple.com/projects/mlx)
> [vLLM vs SGLang: Which Inference Engine Should You Use ...](https://www.yottalabs.ai/post/vllm-vs-sglang-which-inference-engine-should-you-use-in-2026)
> [Qwen3-Coder-Next: The Complete 2026 Guide to Running ...](https://dev.to/sienna/qwen3-coder-next-the-complete-2026-guide-to-running-powerful-ai-coding-agents-locally-1k95)
> [Explore large language models on Apple silicon with MLX ...](https://developer.apple.com/videos/play/wwdc2025/298/)
> [Qwen3-Coder-Next Complete 2026 Guide - Running AI ...](https://a2aprotocol.ai/blog/2026-qwen3-coder-next-complete-guide)
> [Qwen3.5-9B: Specifications and GPU VRAM Requirements](https://apxml.com/models/qwen35-9b)
> [MLX Guide](https://www.kubeflow.org/docs/components/trainer/user-guides/mlx/)
> [vLLM vs TensorRT-LLM vs SGLang: H100 Benchmarks ...](https://www.spheron.network/blog/vllm-vs-tensorrt-llm-vs-sglang-benchmarks)
> [Qwen3-Coder-Next Technical Report (Qwen Team ...](https://www.facebook.com/groups/3670562573177653/posts/4454529284780974/)
>
> **Searching for Qwen3.6 release details**
>
> [Qwen3](https://qwen.ai/blog?id=qwen3)
> [Qwen3: Think Deeper, Act Faster](https://qwenlm.github.io/blog/qwen3/)
> [Qwen/Qwen3-0.6B](https://huggingface.co/Qwen/Qwen3-0.6B)
> [Qwen Chat](https://chat.qwen.ai/)
>
> **Searching for Qwen3 versions and official access**
>
> [Qwen/Qwen3.5-9B · Hugging Face](https://huggingface.co/Qwen/Qwen3.5-9B)
> [GitHub - QwenLM/Qwen3.5: Qwen3.5 is the large language model series developed by Qwen team, Alibaba Cloud. · GitHub](https://github.com/QwenLM/Qwen3.5)
> [Qwen](https://qwen.ai/blog?id=qwen3-coder)
> [ChatGPT - LatentMAS vs TextMAS comparison](https://chatgpt.com/share/69cd00a0-4bbc-832c-b26c-4e94608de24b)
>
> **Identifying open lines in shared content from 1-43**
>
> [ChatGPT - LatentMAS vs TextMAS comparison](https://chatgpt.com/share/69cd00a0-4bbc-832c-b26c-4e94608de24b)
>
> **Searching for GLM-5.1 and Qwen3.6 model info**
>
> [Using GLM-5.1 in Coding Agent - Overview](https://docs.z.ai/devpack/using5.1)
> [zai-org/GLM-5 · Discussions](https://huggingface.co/zai-org/GLM-5/discussions)
> [Qwen: Qwen3.6 Plus Preview](https://developer.puter.com/ai/qwen/qwen3.6-plus-preview/)
> [Qwen3.6 Plus Preview (free) - API Pricing & Providers](https://openrouter.ai/qwen/qwen3.6-plus-preview%3Afree)
> [GLM-5.1 is available to ALL GLM Coding Plan users! from ...](https://www.reddit.com/r/accelerate/comments/1s7v7yb/glm51_is_available_to_all_glm_coding_plan_users/)
> [GLM-5.1 Online Test Scores 45.3 in Coding, Approaching ...](https://help.apiyi.com/en/glm-5-1-coding-plan-claude-opus-alternative-api-guide-en.html)
> [Qwen: Qwen3.6 Plus Preview (free) Review](https://designforonline.com/ai-models/qwen-qwen3-6-plus-preview-free/)
> [GLM Coding Plan](https://z.ai/subscribe)
> [Now you can access to latest Qwen Model for free in ...](https://www.facebook.com/groups/AIUGM/posts/4396559203958374/)
> [GLM-5.1 is available to ALL GLM Coding Plan users!](https://x.com/Zai_org/status/2037490078126084514)
> [Ali Qwen 3.6 Plus Preview Edition Lands on OpenRouter ...](https://www.aibase.com/news/26708)
> [GLM-5.1 Now Available to All GLM Coding Plan Users](https://www.binance.com/en/square/post/306053280448577)
> [Qwen: Qwen3.6 Plus Preview (free)](https://writingmate.ai/models/qwen/qwen3.6-plus-preview)
> [Zhipu: GLM-5.1 is now available to all Coding Plan users](https://www.odaily.news/en/newsflash/474256)
>
> **Searching for Qwen3.5 and Qwen3-Coder benchmarks**
>
> [Qwen/Qwen3.5-27B - Hugging Face](https://huggingface.co/Qwen/Qwen3.5-27B)
> [Pricing | OpenAI API](https://developers.openai.com/api/docs/pricing/)
> [Introducing Claude Haiku 4.5](https://www.anthropic.com/news/claude-haiku-4-5)
> [API Pricing](https://openai.com/api/pricing/)
> [Pricing - Claude API Docs](https://platform.claude.com/docs/en/about-claude/pricing)
> [r/LocalLLaMA - Qwen/Qwen3.5-35B-A3B · Hugging Face](https://www.reddit.com/r/LocalLLaMA/comments/1rdlbvc/qwenqwen3535ba3b_hugging_face/)
> [Anthropic Claude API Pricing 2026](https://www.silicondata.com/use-cases/anthropic-claude-api-pricing-2026/)
> [GPT 5.4 Complete Guide 2026: Features, Pricing ...](https://www.nxcode.io/resources/news/gpt-5-4-complete-guide-features-pricing-models-2026)
> [Claude API Pricing 2026: Full Anthropic Cost Breakdown](https://www.metacto.com/blogs/anthropic-api-pricing-a-full-breakdown-of-costs-and-integration)
>
> **Searching for open Qwen model versions**
>
> [Qwen/Qwen3.5-27B · Hugging Face](https://huggingface.co/Qwen/Qwen3.5-27B)
> [Introducing Claude Haiku 4.5 \ Anthropic](https://www.anthropic.com/news/claude-haiku-4-5)
> [Introducing GPT-5.4 mini and nano | OpenAI](https://openai.com/index/introducing-gpt-5-4-mini-and-nano/)
> [Pricing - Claude API Docs](https://platform.claude.com/docs/en/about-claude/pricing)
> [Overview - Overview - Z.AI DEVELOPER DOCUMENT](https://docs.z.ai/devpack/overview)
>
> **Searching for qwen3-coder 30b parameters and details**
>
> [Qwen/Qwen3-Coder-30B-A3B-Instruct · Hugging Face](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct)
>
> Thought for 1m 19s

You’re right on two important corrections.

First, **GLM-5.1 and Qwen3.6 are newer than the open-weight GLM-5 / Qwen3.5 cards I cited before**. I found official Z.ai docs confirming **GLM-5.1 is now supported in their Coding Agent and can be mapped into Claude Code-style model slots**, and their dev docs explicitly recommend **GLM-5.1 for complex tasks while keeping GLM-4.7 for routine tasks to conserve quota**. [Z.AI+1](https://docs.z.ai/devpack/using5.1)

Second, I could not verify an official **open-weight** Qwen3.6 release. What I _could_ verify is that **Qwen3.6 Plus Preview** is showing up as a recent hosted/API model in third-party provider listings, but I did **not** find an official Hugging Face open-weight card for it. So for now I’d treat Qwen3.6 as **API-preview / hosted-first**, not part of the dependable open-weight local stack yet. [Puter+1](https://developer.puter.com/ai/qwen/qwen3.6-plus-preview/?utm_source=chatgpt.com)

Also, your shared ChatGPT link did not expose the conversation content to the browser tool, so I could not reliably incorporate the actual text from that share page. I only got the shell/login page, not the conversation body. [ChatGPT](https://chatgpt.com/share/69cd00a0-4bbc-832c-b26c-4e94608de24b)

Here’s the cleaned-up conclusion.

What “works in Claude Code” actually proves
-------------------------------------------

It proves **serving compatibility + tool-calling competence**, not necessarily frontier raw intelligence. vLLM’s Claude Code integration docs are explicit: Claude Code can use any model served through vLLM **if** it has strong tool calling and the proper parser / OpenAI-compatible interface. That matters a lot for usefulness, but it is not enough evidence by itself to trust a model for half your fleet traffic. [vLLM](https://docs.vllm.ai/en/stable/serving/integrations/claude_code/)

Best model strategy for your actual hardware ladder
---------------------------------------------------

Your useful tiers are:

*   **Tier 1 local GPU:** 3090 Ti 24 GB
*   **Tier 1.5 sidecar / aux:** 16 GB GPU
*   **Tier 2 laptop:** 16 GB M1 Pro via MLX for tiny jobs only
*   **Tier 3 burst:** Vast.ai

That implies a **3-layer execution plan**, but not the way most people do it.

### Layer A: always-on cheap local worker

This should be your default for the highest-volume, lower-risk subagent tasks.

The most credible open-weight candidate here is **Qwen3.5-9B**. Its official card says it is built for **high-throughput inference with minimal latency and cost overhead**, supports **262k native context** and can extend past 1M, and its benchmark table is much stronger than a typical 9B: **82.5 MMLU-Pro, 81.7 GPQA Diamond, 65.6 LiveCodeBench v6, 29.2 OJBench, 66.1 BFCL-V4, 79.1 TAU2-Bench**. [Hugging Face](https://huggingface.co/Qwen/Qwen3.5-9B)

Bluntly: yes, **Qwen3.5-9B is a real contender**, and on your hardware it makes more sense than many heavier “looks smarter on paper” options because it is the one most likely to stay cheap, responsive, and concurrency-friendly locally. [Hugging Face](https://huggingface.co/Qwen/Qwen3.5-9B)

I would use this lane for:  
repo search, file summarization, lightweight edits, grep/triage, log reading, issue drafting, scaffold generation, routine refactors, context condensation.

### Layer B: local “serious worker” / promoted worker

This is where you put the strongest open model that still has a realistic shot of being useful with your local+burst plan.

The best official candidate is still **Qwen3-Coder-30B-A3B-Instruct**. Its official card says **30.5B total / 3.3B activated**, **262,144 native context**, non-thinking default, and it explicitly emphasizes **tool calling** and **agentic coding**. It also says local apps including **MLX-LM, llama.cpp, Ollama, and KTransformers** support Qwen3 locally, though for serious serving you’d still use vLLM or SGLang. [Hugging Face+1](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8?utm_source=chatgpt.com)

Why this one still matters:  
3.3B active is exactly the kind of shape you want for “smart enough worker, cheap enough to serve.” It is the best fit for your stated goal better than dense 27B if the KPI is **real throughput and concurrency**, not just single-request cleverness. [Hugging Face+1](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8?utm_source=chatgpt.com)

### Layer C: API / burst / premium lane

This is where the newer hosted models matter.

*   **GLM-5.1**: use for harder coding / complex tasks if you’re leveraging their plan or burst APIs. Official Z.ai docs position it as the newer model for complex work and still recommend GLM-4.7 for routine tasks to save quota. [Z.AI+1](https://docs.z.ai/devpack/overview)
*   **Qwen3.6 Plus Preview**: interesting, but I would treat it as **experimental hosted lane only** until official open-weight or fuller documentation lands. [Puter+1](https://developer.puter.com/ai/qwen/qwen3.6-plus-preview/?utm_source=chatgpt.com)
*   **Claude Haiku 4.5 / GPT-5.4 mini** remain your true external baselines for what a “fast smart worker” feels like. Anthropic positions Haiku 4.5 as near-frontier at much higher speed and lower cost, and OpenAI positions GPT-5.4 mini specifically for **coding, computer use, and subagents**. [Anthropic+1](https://www.anthropic.com/news/claude-haiku-4-5)

Your 24 GB + 16 GB + 16 GB MacBook plan
---------------------------------------

### 3090 Ti 24 GB

This should host either:

*   **Qwen3.5-9B** as the permanent default worker, or
*   a more ambitious promoted worker like **Qwen3-Coder-30B-A3B** when you actually need it and the quant/runtime fit is acceptable.

### Extra 16 GB GPU

Do **not** architect around combining the 24 GB and 16 GB card as if they were a clean unified serving target. In practice, mismatched-memory consumer multi-GPU setups are annoying and fragile. Use the 16 GB card for:

*   secondary worker,
*   embedding/reranking,
*   vision side jobs,
*   draft model / speculative model experiments,
*   background preprocessing,
*   or a cheap second inference lane.

That is much saner than trying to pretend the 16 GB card magically upgrades the 24 GB card into a clean 40 GB production box.

### 16 GB M1 Pro MacBook

This is not a main worker node. It is a **micro-task node**. MLX-LM officially supports generation, chat, quantization, and even fine-tuning on Apple silicon, including quantized models and distributed inference/fine-tuning primitives. That makes it useful for:

*   tiny utility models,
*   summarizers,
*   commit-message writers,
*   filename/classifier tasks,
*   tiny code transforms,
*   low-stakes background helpers. [GitHub](https://github.com/ml-explore/mlx-lm)

It is not your serious coding worker. It is your “never waste rented GPU money on toy subtasks” box.

Rent minimization strategy
--------------------------

This is the part that matters most economically.

Use rentals only when **both** of these are true:

1.  the task needs a stronger worker than your always-on local lane, and
2.  the job batch is large enough that spinning up burst GPU time is cheaper than pushing it to premium API/subscription quota.

Vast says pricing is live-market, per-second billed, and supports on-demand, interruptible, and reserved options. Their marketplace positioning is exactly what you want for burst compute. [Vast AI+1](https://vast.ai/pricing?srsltid=AfmBOopGv7K80Zc8T8xNc3e5rzybm493n9fQvjM9JGHEI_z8I_d4po2V)

So the correct policy is:

*   **Default**: run Qwen3.5-9B locally.
*   **Escalate locally**: use a stronger local worker only if it still fits and keeps latency acceptable.
*   **Burst to Vast**: only for batch windows, hard repo jobs, long-context jobs, or temporary concurrency spikes.
*   **Use subscription/API premium models**: only for planner/judge/final-review or when the failure cost of a weaker model is higher than the token cost.

That is how you minimize both rental spend and subscription burn.

What I’d actually deploy
------------------------

### Default local worker

**Qwen3.5-9B**  
because the official numbers are strong enough, and it is the best fit for your “most requests, fast enough, cheap enough” lane. [Hugging Face](https://huggingface.co/Qwen/Qwen3.5-9B)

### Stronger local / burst worker

**Qwen3-Coder-30B-A3B-Instruct**  
because 3.3B active and coder/tooling emphasis is exactly the right shape for an agent worker. [Hugging Face+1](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8?utm_source=chatgpt.com)

### Hosted premium coding lane

**GLM-5.1**  
because it is current in Z.ai’s coding stack and explicitly supported in their Claude Code-style workflow docs. [Z.AI+1](https://docs.z.ai/devpack/using5.1)

### Experimental hosted lane

**Qwen3.6 Plus Preview**  
because it is new and promising, but I do not yet have enough official open-weight evidence to recommend building local infra assumptions around it. [Puter+1](https://developer.puter.com/ai/qwen/qwen3.6-plus-preview/?utm_source=chatgpt.com)

### Benchmark baselines you should keep in mind

**Claude Haiku 4.5**: $1 / 1M input, $5 / 1M output, positioned as near-frontier fast coding/subagent model. [Anthropic](https://www.anthropic.com/news/claude-haiku-4-5)  
**GPT-5.4 mini**: $0.75 / 1M input, $4.50 / 1M output, explicitly framed for coding, computer use, and subagents. [OpenAI](https://openai.com/index/introducing-gpt-5-4-mini-and-nano/)

vLLM vs SGLang for you
----------------------

My answer is still:

*   **vLLM first**
*   **SGLang second if profiling proves it wins for your traffic shape**

Reason: you care about Claude Code compatibility and operational simplicity first. vLLM already has the documented Claude Code integration path. Qwen3.5’s official repo also explicitly shows both **SGLang** and **vLLM** deployment support. [vLLM+1](https://docs.vllm.ai/en/stable/serving/integrations/claude_code/)

So:

*   bring up the first serious worker on **vLLM**
*   compare against **SGLang** only after you have real traces from your workload

Do not prematurely optimize the runtime before you’ve proven which model actually wins your eval set.

My updated ranking for your situation
-------------------------------------

For **high-volume worker traffic**:

1.  **Qwen3.5-9B** local default
2.  **Qwen3-Coder-30B-A3B-Instruct** promoted local / burst worker
3.  **GLM-5.1** hosted premium worker
4.  **Qwen3.6 Plus Preview** experimental hosted lane
5.  **Qwen3.5-27B** quality-heavy dense fallback, not default worker

That last point matters. The official Qwen3.5-27B numbers are very good, including **72.4 SWE-bench Verified**, **41.6 Terminal Bench 2**, **80.7 LiveCodeBench v6**, and competitive comparisons against GPT-5 mini in several rows. But dense 27B is still a worse _economic default_ than the best sparse/active-parameter worker shapes when your real problem is serving volume. [Hugging Face](https://huggingface.co/Qwen/Qwen3.5-27B)

If you want, the next thing I should do is turn this into a **tiered execution matrix**:

**task class → model tier → hardware tier → escalation rule → rent/no-rent decision**

That would be the most useful artifact for actually wiring this into your MVP.

---

**Sources:**

- [Using GLM-5.1 in Coding Agent - Overview - Z.AI DEVELOPER DOCUMENT](https://docs.z.ai/devpack/using5.1)
- [Qwen: Qwen3.6 Plus Preview](https://developer.puter.com/ai/qwen/qwen3.6-plus-preview/?utm_source=chatgpt.com)
- [ChatGPT - LatentMAS vs TextMAS comparison](https://chatgpt.com/share/69cd00a0-4bbc-832c-b26c-4e94608de24b)
- [Qwen/Qwen3.5-9B · Hugging Face](https://huggingface.co/Qwen/Qwen3.5-9B)
- [Introducing Claude Haiku 4.5 \ Anthropic](https://www.anthropic.com/news/claude-haiku-4-5)
- [GitHub - ml-explore/mlx-lm: Run LLMs with MLX · GitHub](https://github.com/ml-explore/mlx-lm)
- [GPU Pricing — Live Marketplace Rates | Vast.ai](https://vast.ai/pricing?srsltid=AfmBOopGv7K80Zc8T8xNc3e5rzybm493n9fQvjM9JGHEI_z8I_d4po2V)
- [Introducing GPT-5.4 mini and nano | OpenAI](https://openai.com/index/introducing-gpt-5-4-mini-and-nano/)
- [Claude Code - vLLM](https://docs.vllm.ai/en/stable/serving/integrations/claude_code/)

## Prompt:
4/1/2026, 4:28:52 AM

https://huggingface.co/Jackrong/Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled-GGUF what about qwen 4bs? 
I thought active params affected training time only, not runtime memory active params?

## Response:
4/1/2026, 4:28:53 AM

I’m checking two things separately: whether these 4B-class Qwen distills are actually credible worker candidates, and the exact “active params vs runtime memory” distinction so I don’t hand-wave it. The second one is where a lot of people mix up FLOPs, weight residency, and KV/cache costs.

> **Searching for runtime memory and parameter details**
>
> [Jackrong/Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled-GGUF · Hugging Face](https://huggingface.co/Jackrong/Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled-GGUF)
>
> **Opening specific lines with parameters**
>
> [Qwen/Qwen3.5-4B · Hugging Face](https://huggingface.co/Qwen/Qwen3.5-4B)
>
> Thought for 14s

Yeah — **Qwen 4B-class models are absolutely worth looking at**, but I would separate **official Qwen3.5-4B** from **community 4B distills like Jackrong’s**.

The official **Qwen3.5-4B** card says it is a **4B-parameter** model with a long **262,144-token native context**, and Qwen explicitly markets Qwen3.5’s hybrid architecture as aiming for **high-throughput inference with minimal latency and cost overhead**. Its own benchmark table is not bad for the size either: **79.1 MMLU-Pro** and **52.9 SuperGPQA** on the card you can actually inspect. [Hugging Face+1](https://huggingface.co/Qwen/Qwen3.5-4B)

The specific Jackrong model you linked is more of an **interesting experiment than a safe default worker**. Its card says it is a **LoRA/SFT distill on top of Qwen3.5-4B**, trained on Claude/Opus-style reasoning datasets, with only two benchmark numbers shown on-page: **GPQA Diamond 33.82 → 38.88** and **ARC-Challenge 64.59 → 66.38** versus baseline. The same card also explicitly says it is a **“test version”** intended for **learning, demonstration, academic research, and technical exploration**, not a hardened production artifact. [Hugging Face](https://huggingface.co/Jackrong/Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled-GGUF)

So my blunt take is: **official Qwen3.5-4B = yes, real candidate for cheap local worker duty; Jackrong Qwen3.5-4B Opus-distilled = maybe, but only after your own evals**. The Jackrong GGUF sizes are tiny — roughly **2.7 GB for Q4\_K\_M** and **4.48 GB for Q8\_0** according to the page — so it is very easy to test on your MacBook or spare GPU, which makes it a good experiment lane even if it should not be trusted by default. [Hugging Face](https://huggingface.co/Jackrong/Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled-GGUF)

On your second question: **active parameters absolutely affect runtime compute, but they do not magically erase runtime memory costs**.

For MoE models like **Qwen3-Coder-30B-A3B** or **Qwen3-30B-A3B-Instruct-2507**, the card says they have **30.5B total parameters but only 3.3B activated** at inference time, with **128 experts and 8 activated experts**. That means the **per-token compute/FLOPs** are closer to a ~3.3B-active model than a dense 30B model, which is a huge runtime win. [Hugging Face+1](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8)

But **weight memory is still mostly about the full model that must be resident**, plus runtime state like **KV cache**, activations, and framework overhead. In other words:

*   **Activated params** mostly cut **compute per token**.
*   They do **not** reduce total model storage to only 3.3B worth of weights in the usual serving setup.
*   Runtime memory is still driven by **full weights + KV cache + overhead**, not just active-param count. [Hugging Face+1](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8)

That is why a **30.5B total / 3.3B active** MoE can be much faster than a dense 30B in practice, while still being much heavier to _fit_ than a true dense 4B or 9B. The active-param number is not “training only”; it matters at inference, just mainly on the **compute path**, not as a full replacement for the memory footprint. [Hugging Face+1](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8)

So for your setup, the sane interpretation is:

*   **4B dense**: tiny, cheap, easy to keep always-on, good for low-risk tasks. [Hugging Face+1](https://huggingface.co/Qwen/Qwen3.5-4B)
*   **9B dense**: probably the stronger always-on local default if quality matters more. [Hugging Face](https://huggingface.co/Qwen/Qwen3.5-4B)
*   **30B-A3B MoE**: stronger worker shape, but still a much heavier serving target than the “3.3B active” number alone makes it sound. [Hugging Face+1](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8)

If you want the clean next step, I’d compare **official Qwen3.5-4B**, **official Qwen3.5-9B**, and **Jackrong 4B distilled** as a cheap-worker bakeoff, then treat the 30B-A3B line as the promoted worker tier.

---

**Sources:**

- [Qwen/Qwen3.5-4B · Hugging Face](https://huggingface.co/Qwen/Qwen3.5-4B)

## Prompt:
4/1/2026, 4:29:46 AM

we dont need hardened production artifacts, experiments that prove valuable improvements or provide components we cant take to create our own superset eexperiemnt are also wnated

## Response:
4/1/2026, 4:29:49 AM

That changes the filter a lot. If the goal includes harvesting useful deltas, training recipes, prompts, adapters, or quant choices for your own superset experiments, then “production-safe” is the wrong bar — the right bar is whether a variant shows a **real, measurable edge** you can isolate and reproduce.

> **Browsing niche models and refining guidance with citations**
>
> [Jackrong/Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled-GGUF · Hugging Face](https://huggingface.co/Jackrong/Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled-GGUF)
>
> **Affirming experiment-friendly answers with benchmark citations**
>
> [Qwen/Qwen3.5-4B · Hugging Face](https://huggingface.co/Qwen/Qwen3.5-4B)
>
> Thought for 19s

Good. Then the filter changes from **“is this safe to deploy?”** to **“does this contain a reusable edge?”**

That makes a lot more of the weird HF variants worth touching.

The right way to think about them is:

**not**  
“Should we trust this model?”

**but**  
“What signal does this model carry that we can extract, reproduce, or surpass?”

For the Jackrong 4B you linked, the useful signals are pretty explicit on the card:

*   it is a **LoRA/SFT distill on top of Qwen3.5-4B**
*   it uses **response-only training**
*   it enforces a **strict `<think> ... </think>` scaffold**
*   it claims a more compressed, less repetitive reasoning style
*   it reports modest benchmark lifts over the base on **GPQA Diamond** and **ARC-Challenge**. [Hugging Face+1](https://huggingface.co/Jackrong/Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled-GGUF)

That means the value is not necessarily “this is your worker model.”  
The value may be:

1.  a useful **reasoning scaffold**
2.  a useful **distillation dataset mix**
3.  a useful **training objective**
4.  a useful **prompt format / output discipline**
5.  a useful **small-model teacher-transfer recipe**
6.  a useful **quant target** for your hardware tiers. [Hugging Face](https://huggingface.co/Jackrong/Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled-GGUF)

So yes: in your case, **community experimental models are absolutely in scope**. But they should be treated as one of three things:

### 1\. Direct worker candidates

These are models that might already be good enough to run real traffic.

For that, official **Qwen3.5-4B** and especially **Qwen3.5-9B** are still stronger baselines because they have better-documented architecture/serving support, long native context, and real published benchmark tables. Qwen explicitly positions Qwen3.5 as an **efficient hybrid architecture** for **high-throughput inference with minimal latency and cost overhead**, and the official 4B card includes direct vLLM/SGLang serving recipes and tool-call parser examples. [Hugging Face+1](https://huggingface.co/Qwen/Qwen3.5-4B)

### 2\. Experimental deltas to mine

This is where things like Jackrong’s 4B distill shine.

Even if the model itself is not your final answer, it may still be worth testing because it bakes in:

*   a particular teacher style
*   a particular data source blend
*   a particular “thinking compression” behavior
*   a particular response-only masking strategy
*   a particular small-model post-training profile. [Hugging Face](https://huggingface.co/Jackrong/Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled-GGUF)

That is exactly the sort of thing you can steal the _idea_ from and roll into your own superset experiments.

### 3\. Components for your own stack

Some variants are mainly useful as ingredients:

*   training data
*   adapter ideas
*   formatting ideas
*   benchmark targets
*   quantization targets
*   serving configurations

That can matter more than the released checkpoint itself.

So if your goal is “find useful ingredients,” I would broaden the search and evaluate models on **what they teach you**, not just on whether you’d ship them untouched.

What I would do with the 4B/9B class specifically
-------------------------------------------------

I’d treat the small-model lane as a structured experiment family:

### Baseline family

*   official **Qwen3.5-4B**
*   official **Qwen3.5-9B** [Hugging Face+1](https://huggingface.co/Qwen/Qwen3.5-4B)

### Distill family

*   Jackrong 4B Claude/Opus distill
*   similar 9B distills/merges that have at least some training description or benchmark claims. [Hugging Face](https://huggingface.co/Jackrong/Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled-GGUF)

### What you test for

Not just benchmark scores. Test:

*   tool-call correctness
*   patch success rate
*   diff quality
*   verbosity control
*   “gets unstuck” behavior
*   repetition / looping
*   context discipline
*   speed per watt / per dollar
*   behavior at 4-way, 8-way, 16-way concurrency
*   failure mode shape

That is where experimental models sometimes punch above their benchmark numbers.

The specific “superset experiment” opportunities I see
------------------------------------------------------

For the Jackrong-style models, the reusable pieces look like:

### A. Structured reasoning style compression

The card explicitly says the model is trying to reduce Qwen3.5’s tendency toward repetitive reasoning by distilling a more direct structured scaffold. That’s not trivial. Even if the benchmark gains are small, a real reduction in useless deliberation could be extremely valuable for agent workers. [Hugging Face](https://huggingface.co/Jackrong/Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled-GGUF)

### B. Response-only training on reasoning blocks

The card describes **train\_on\_responses\_only** with masked instructions and strict output structure. That is a concrete recipe you can copy into your own post-training experiments. [Hugging Face](https://huggingface.co/Jackrong/Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled-GGUF)

### C. Tiny checkpoint economics

The GGUF sizes on that model are tiny:

*   ~**2.71 GB** for Q4\_K\_M
*   ~**4.48 GB** for Q8\_0. [Hugging Face](https://huggingface.co/Jackrong/Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled-GGUF)

That matters because it makes these models almost free to test across your hardware ladder:

*   MacBook MLX / CPU-ish experiments
*   spare 16 GB GPU
*   local parallel bakeoffs
*   cheap Vast rentals only when needed

### D. Teacher-style transfer hypotheses

You’re explicitly interested in “components we can take to create our own superset experiment.” A model like this is useful because it encodes a very specific hypothesis:

> Can a small Qwen base inherit a more effective reasoning cadence and decomposition style from a much stronger teacher?

That is exactly the kind of hypothesis worth testing and recombining.

My revised stance for your use case
-----------------------------------

You should absolutely include:

*   official baselines
*   community distills
*   weird merges
*   pruned REAP variants
*   quant variants
*   RL-tuned coder variants

But score them in **two different columns**:

### Column 1: shipping fitness

Would I actually route real worker traffic to it?

### Column 2: research value

Did it demonstrate:

*   better style
*   better tool use
*   better brevity
*   better coding instincts
*   better data recipe
*   better quant fit
*   better training trick
*   better scaffolding behavior

A model can fail Column 1 and still be a huge win in Column 2.

On your active-params point, one more clean version
---------------------------------------------------

Your intuition was half right.

*   **Active params do matter at runtime**, because they reduce how much of the model is _used per token_.
*   But **full model residency still matters for memory** in normal serving.
*   So active params are not “training only,” but they are also not a free pass that turns a 30B model into 3B memory-wise. Qwen’s own coder card explicitly says **30.5B total, 3.3B activated, 128 experts, 8 activated experts**. That is a runtime compute story, not “the rest disappears from memory.” [Hugging Face+1](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8)

Bottom line
-----------

Given your actual goal, I would stop excluding models just because they are not hardened.

I would instead bucket candidates like this:

*   **official baselines** to anchor truth
*   **experimental distills/merges** to mine deltas
*   **MoE/pruned variants** to study fit/compute tradeoffs
*   **small quants** to study hardware economics
*   **teacher-transfer variants** to study post-training recipes

That is the right mindset for building your own superset.

The next most useful thing is probably a **candidate matrix** with columns like:

**model | base | recipe type | claimed edge | hardware fit | eval confidence | research value | likely reusable components**

That would make the experiment pool much cleaner.

---

**Sources:**

- [Jackrong/Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled-GGUF · Hugging Face](https://huggingface.co/Jackrong/Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled-GGUF)

## Prompt:
4/1/2026, 4:31:07 AM

review more of the 3-12b sized models as of 2026

## Response:
4/1/2026, 4:31:09 AM

I’m widening the net beyond “official Qwen only” and looking at the serious 3–12B candidates from 2026 that could matter for your worker lane, including official bases, credible distills, and any small-model lines with real eval signal rather than just download counts.

> **Browsing Hugging Face for 2026 coding models**
>
> [Arena Leaderboard - a Hugging Face Space by lmarena-ai](https://huggingface.co/spaces/lmarena-ai/arena-leaderboard)
> [Start of 2026 what's the best open coding model?](https://www.reddit.com/r/LocalLLaMA/comments/1q82ae8/start_of_2026_whats_the_best_open_coding_model/)
>
> **Refining search for targeted model details**
>
> I should look up specific models like Qwen 4B and 8B, Zeta-2, OmniCoder, and others to get more targeted information. I'll focus on finding official sources if possible and refine my search to include more details on models like Qwen 3.5, Zed Zeta, OmniCoder 9B, MiniMax, and any relevant sources.
>
> **Searching for official Qwen, OmniCoder, and Zeta models**
>
> [Qwen/Qwen3.5-4B](https://huggingface.co/Qwen/Qwen3.5-4B)
>
> **Refining search to include Qwen 4B and others**
>
> I should search for official benchmarks for Qwen 4B, possibly including 3B to 12B variants. I'll look into NVIDIA Nano 4B and Seed-Coder 8B for comparison. I’ll focus on official sources and may use snippets from current search results as references. Time to gather more detailed info!
>
> **Searching for Qwen4B and 3-12B model benchmarks**
>
> [ByteDance-Seed/Seed-Coder-8B-Base](https://huggingface.co/ByteDance-Seed/Seed-Coder-8B-Base)
> [Help with my questions. very new at this - Intermediate](https://discuss.huggingface.co/t/help-with-my-questions-very-new-at-this/173415)
>
> Thought for 29s

Here’s the tighter 2026 view of the **3B–12B** band, focusing on models that are actually worth your time for worker-lane experiments.

Best bets
---------

**Qwen3.5-9B** is still the cleanest overall starting point in this size class. It is an official March 2026 release, explicitly compatible with Transformers, vLLM, SGLang, and KTransformers, and it has the best balance of “small enough to run cheaply” and “serious enough to matter.” [Hugging Face](https://huggingface.co/Qwen/Qwen3.5-9B?utm_source=chatgpt.com)

**Qwen3.5-4B** is the smaller sibling worth testing when you care more about always-on cheap throughput than absolute capability. It is also an official March 2026 release with the same serving-stack compatibility story. [Hugging Face](https://huggingface.co/Qwen/Qwen3.5-4B?utm_source=chatgpt.com)

For **pure code-edit / IDE-assist workflows**, **zeta-2** is worth attention. It is not a general worker in the same way Qwen is; it is a specialized **next-edit suggestion** model fine-tuned from **Seed-Coder-8B-Base**. That makes it interesting for editor-native code rewrite flows, not as a broad agent default. [Hugging Face+1](https://huggingface.co/zed-industries/zeta-2?utm_source=chatgpt.com)

For **agentic coding experiments**, **OmniCoder-9B** and especially **OmniCoder-2-9B** are real candidates, not just random merges. OmniCoder-9B is a Qwen3.5-9B-based coding agent model trained on 425k+ agentic coding trajectories, while OmniCoder-2-9B is presented as a ground-up rebuild to address issues reported in v1. That makes OmniCoder-2-9B more interesting than v1 for you. [Hugging Face+1](https://huggingface.co/Tesslate/OmniCoder-9B?utm_source=chatgpt.com)

For **new 2026 small-model experiments**, **NVIDIA Nemotron-3 Nano 4B** is one of the few genuinely fresh official entries. NVIDIA positions it as an edge-ready small model for agentic use, local assistants, automation, and coding languages, and released BF16, FP8, and GGUF variants in March 2026. [Hugging Face+2Hugging Face+2](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-4B-FP8?utm_source=chatgpt.com)

Models I’d prioritize by role
-----------------------------

If you want one **default small worker baseline**, start with **Qwen3.5-9B**. It is the safest anchor for comparison in this band. [Hugging Face](https://huggingface.co/Qwen/Qwen3.5-9B?utm_source=chatgpt.com)

If you want the **smallest plausible real worker**, test **Qwen3.5-4B** and **Nemotron-3 Nano 4B** side by side. Qwen is the safer general-purpose baseline; Nemotron is the more interesting fresh architecture/recipe experiment. [Hugging Face+1](https://huggingface.co/Qwen/Qwen3.5-4B?utm_source=chatgpt.com)

If you want a **code-specialist side lane**, test **OmniCoder-2-9B** and **zeta-2**. OmniCoder is the more agentic/general coding candidate; zeta-2 is the more edit-prediction-native candidate. [Hugging Face+1](https://huggingface.co/Tesslate/OmniCoder-2-9B?utm_source=chatgpt.com)

If you want **research-value distills**, keep looking at the **Jackrong 4B/9B Qwen3.5 Claude-4.6 Opus distilled** family, but treat them as experiments to mine, not truth anchors. The 9B distilled card explicitly says it is a CoT-distilled Qwen3.5-9B variant. [Hugging Face](https://huggingface.co/Jackrong/Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-GGUF?utm_source=chatgpt.com)

What I think is overrated
-------------------------

I would not treat every popular 9B community upload as equally serious. Download counts are noisy. Some are mostly style merges, some are uncensored forks, some are thin post-trains with weak eval evidence. They may still be useful, but they should be tested against official baselines, not assumed to beat them.

I also would not over-index on **Qwen3-4B-Thinking-2507** for worker use unless your evals show it helps. It is an older 2025 reasoning-focused variant, and there is at least some public discussion indicating structured-output/instruction-following issues in quantized use. That does not kill it, but it makes it less attractive as a clean 2026 worker default than Qwen3.5-4B. [Hugging Face+1](https://huggingface.co/Qwen/Qwen3-4B-Thinking-2507?utm_source=chatgpt.com)

What still matters from older 8B code lines
-------------------------------------------

**Seed-Coder-8B** is older, but still relevant as a base or ancestry line. ByteDance’s card says Seed-Coder-8B-Base achieved SOTA among roughly 8B open models on several coding benchmarks at release, and its collection includes Base, Instruct, and Reasoning variants. That makes it useful both directly and as lineage for things like zeta-2. [Hugging Face+2Hugging Face+2](https://huggingface.co/ByteDance-Seed/Seed-Coder-8B-Base?utm_source=chatgpt.com)

Practical shortlist for you
---------------------------

If I were narrowing this to a first-pass bakeoff for your setup, I’d use:

**General worker anchors**

*   Qwen3.5-9B [Hugging Face](https://huggingface.co/Qwen/Qwen3.5-9B?utm_source=chatgpt.com)
*   Qwen3.5-4B [Hugging Face](https://huggingface.co/Qwen/Qwen3.5-4B?utm_source=chatgpt.com)
*   NVIDIA Nemotron-3 Nano 4B [Hugging Face](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16?utm_source=chatgpt.com)

**Code/agent experiments**

*   OmniCoder-2-9B [Hugging Face](https://huggingface.co/Tesslate/OmniCoder-2-9B?utm_source=chatgpt.com)
*   zeta-2 [Hugging Face](https://huggingface.co/zed-industries/zeta-2?utm_source=chatgpt.com)
*   Seed-Coder-8B-Instruct or Reasoning as ancestry/control [Hugging Face+1](https://huggingface.co/ByteDance-Seed/Seed-Coder-8B-Instruct?utm_source=chatgpt.com)

**Distill/mining experiments**

*   Jackrong Qwen3.5-9B Claude-4.6 Opus Distilled [Hugging Face](https://huggingface.co/Jackrong/Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-GGUF?utm_source=chatgpt.com)
*   Jackrong Qwen3.5-4B Claude-4.6 Opus Distilled, from your earlier link, as the tiny experimental lane

My blunt ranking
----------------

For your goals, today:

1.  **Qwen3.5-9B** — best overall 3B–12B anchor
2.  **Qwen3.5-4B** — best cheap baseline
3.  **OmniCoder-2-9B** — best interesting coding-agent experiment
4.  **Nemotron-3 Nano 4B** — best fresh 2026 small-model experiment
5.  **zeta-2** — best niche code-edit specialist
6.  **Jackrong 4B/9B distills** — best mining targets, not best truth anchors

The main thing I’d watch for is whether **OmniCoder-2-9B** or a good **Qwen3.5-9B distill** beats base Qwen3.5-9B on your actual agent tasks without becoming unstable. There are already public discussion signals that OmniCoder v1 had quality issues, which is exactly why v2 exists. [Hugging Face+1](https://huggingface.co/Tesslate/OmniCoder-2-9B?utm_source=chatgpt.com)

The next useful step is a sharper pass specifically on **coding-capable 3B–12B models** only, with a matrix for **base model, recipe, context length, fit on 24 GB / 16 GB / MLX, and what kind of task each is actually good for**.

---

**Sources:**

- [Qwen/Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B?utm_source=chatgpt.com)

## Prompt:
4/1/2026, 4:41:54 AM

perhaps cover specialized ones for other roles too + slms https://huggingface.co/ByteDance-Seed/Stable-DiffCoder-8B-Instruct https://huggingface.co/Jackrong/Qwen3.5-0.8B-Claude-4.6-Opus-Reasoning-Distilled-GGUF

## Response:
4/1/2026, 4:41:56 AM

I’m broadening this from “worker coding models” to a small-model role map: cheap coders, edit specialists, tiny reasoning distills, and the non-coding helper lanes like triage, summarization, classification, and routing. That’s the right frame if you want a layered local stack instead of forcing one model to do everything.

> **Browsing specialized models and SLMs for various roles**
>
> [ByteDance-Seed/Stable-DiffCoder-8B-Instruct · Hugging Face](https://huggingface.co/ByteDance-Seed/Stable-DiffCoder-8B-Instruct)
>
> **Searching for lines in Jackrong card lower down**
>
> [Jackrong/Qwen3.5-0.8B-Claude-4.6-Opus-Reasoning-Distilled-GGUF · Hugging Face](https://huggingface.co/Jackrong/Qwen3.5-0.8B-Claude-4.6-Opus-Reasoning-Distilled-GGUF)
>
> **Searching for Qwen benchmarks and Jackrong details**
>
> [Jackrong/Qwen3.5-0.8B-Claude-4.6-Opus-Reasoning-Distilled-GGUF · Hugging Face](https://huggingface.co/Jackrong/Qwen3.5-0.8B-Claude-4.6-Opus-Reasoning-Distilled-GGUF)
>
> **Exploring specialized models for roles and embeddings**
>
> The user is asking about covering specialized models for different roles, possibly looking for small models under 1B parameters, like SLMs. I should check for models like Qwen, Nemotron, or SmolLM3 for reranking/embedding or triage purposes. I’ll scan for the latest available models that match these needs.
>
> **Searching for small specialized models and rerankers**
>
> [🎆 AI 2026 — The 9 trends that will EXPLODE this year! 🚀💥](https://huggingface.co/blog/RDTvlokip/the-9-trends-that-will-explode-this-year)
> [How to find a model benchmark-first or task-first](https://discuss.huggingface.co/t/how-to-find-a-model-benchmark-first-or-task-first/72882)
>
> **Focusing on specialized models and citations**
>
> The user asked about specialized models for certain roles, especially those around 0.8B or smaller. I should mention those, along with the 12B+ models, and focus on models' roles. I’ll also make sure each section is properly cited with the relevant information, especially about model size and official lines.
>
> **Analyzing roles, model sizes, and citation requirements**
>
> [Jackrong/Qwen3.5-0.8B-Claude-4.6-Opus-Reasoning-Distilled-GGUF · Hugging Face](https://huggingface.co/Jackrong/Qwen3.5-0.8B-Claude-4.6-Opus-Reasoning-Distilled-GGUF)
>
> Thought for 49s

Yes — once you broaden from “one default worker” to **role-specific small models**, the landscape gets more interesting.

My read is:

**Best general small-worker anchors**  
Use **Qwen3.5-9B** and **Qwen3.5-4B** as your truth baselines. Both are official 2026 releases, both are explicitly positioned around an **efficient hybrid architecture** for **high-throughput inference with minimal latency and cost overhead**, both expose **tool-call parser** support in SGLang/vLLM examples, and both target **262,144-token** serving configs in their own cards. Qwen’s published benchmark table also shows the 9B materially ahead of the 4B on most reasoning/instruction rows, while the 4B stays surprisingly competitive for the size. [Hugging Face+5Hugging Face+5Hugging Face+5](https://huggingface.co/Qwen/Qwen3.5-9B)

**Best code-edit specialist**  
**Stable-DiffCoder-8B-Instruct** is worth real attention, because it is not “just another 8B coder.” ByteDance explicitly frames it as a **code diffusion** model, built on the Seed-Coder line, with any-order modeling that improves **structured code handling for editing and reasoning**. On its own card it beats a lot of nearby ~8B AR baselines across several coding benchmarks; for example, it posts **54.8 BigCodeBench (Full)** and **31.8 BigCodeBench (Hard)**, ahead of Seed-Coder-8B-Instruct, Qwen2.5-Coder-7B-Instruct, and OpenCoder-8B-Instruct in the table shown there. The catch is context: its listed context length is only **8192**, so this is an edit/generation specialist, not your long-context repo worker. [Hugging Face](https://huggingface.co/ByteDance-Seed/Stable-DiffCoder-8B-Instruct)

**Best code-edit prediction niche**  
**zeta-2** is even narrower and more specialized. Its card says it is a **code edit prediction / next-edit suggestion** model finetuned from **Seed-Coder-8B-Base**, designed to take code context, edit history, and an editable region around the cursor and predict the rewritten content for that region. That makes it attractive for IDE-native rewrite/autocomplete flows, but not as a general tool-using agent. [Hugging Face](https://huggingface.co/zed-industries/zeta-2)

**Best “agentic coding 9B” experiment**  
**OmniCoder-2-9B** is one of the more credible community-ish 9B experiments because the card is unusually explicit about what changed. It says v2 is a **ground-up rebuild** to fix v1’s repetition and loop problems, switches to **assistant-only** training, and claims better stability in agentic loops. Its own table claims **25.8 Terminal-Bench 2.0** versus **14.6** for base Qwen3.5-9B, while GPQA stays roughly on par. I would not treat those self-reported numbers as gospel, but this is exactly the kind of model that is worth testing for your “mine useful deltas” objective. [Hugging Face](https://huggingface.co/Tesslate/OmniCoder-2-9B)

**Best official SLM lane**  
For actual **SLM** coverage, **NVIDIA Nemotron-3 Nano 4B** is one of the cleaner official 2026 entries. NVIDIA explicitly calls it a **small language model (SLM)**, says it was trained from scratch, and positions it as a unified model for **reasoning and non-reasoning tasks**. The use-case section is unusually concrete: edge-ready agentic AI, gaming NPCs, local voice assistants, IoT automation, and English/coding-language use. It also has explicit **vLLM** support in the card, including a custom reasoning parser requirement. [Hugging Face+2Hugging Face+2](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16)

**Best ultra-tiny research lane**  
The **Jackrong Qwen3.5-0.8B Claude-4.6 Opus distilled GGUF** is not something I would trust as a core worker, but it is exactly the sort of experiment worth mining. The card says it is a LoRA/SFT distill on top of the **Qwen3.5-0.8B dense architecture**, uses **response-only** training with `train_on_responses_only`, enforces a strict `<think> ... </think>` format, and is built from a tiny filtered reasoning set of **2,516 samples**. It is also tiny enough to be almost free to test: the listed GGUF sizes are about **503 MB for Q4\_K\_M** and **812 MB for Q8\_0**. The card also flatly says it is a **test version** for learning/demonstration and research/technical exploration, which in your case is a plus, not a disqualifier. [Hugging Face+3Hugging Face+3Hugging Face+3](https://huggingface.co/Jackrong/Qwen3.5-0.8B-Claude-4.6-Opus-Reasoning-Distilled-GGUF)

So if I map these into **roles**, I’d do it like this:

**Main cheap local worker:** Qwen3.5-9B.  
Best all-around small anchor. Tool-use capable, long context, strong official baseline. [Hugging Face+1](https://huggingface.co/Qwen/Qwen3.5-9B)

**Always-on cheaper fallback / overflow worker:** Qwen3.5-4B.  
Same serving story, same long-context path, cheaper and weaker but still real. [Hugging Face+1](https://huggingface.co/Qwen/Qwen3.5-4B)

**Code editing / patching specialist:** Stable-DiffCoder-8B-Instruct.  
Especially interesting when you care about structured edits more than long-context tool-agent work. [Hugging Face](https://huggingface.co/ByteDance-Seed/Stable-DiffCoder-8B-Instruct)

**IDE next-edit model:** zeta-2.  
Useful for editor-native prediction, not broad agent work. [Hugging Face](https://huggingface.co/zed-industries/zeta-2)

**Aggressive coding-agent experiment:** OmniCoder-2-9B.  
Good candidate when you specifically want to test whether assistant-only training and anti-loop recipe changes improve real agent behavior. [Hugging Face](https://huggingface.co/Tesslate/OmniCoder-2-9B)

**Edge / SLM / local device lane:** Nemotron-3 Nano 4B.  
This is the one I’d test for small-device agentic helper roles. [Hugging Face+1](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16)

**Micro-task / micro-reasoning lab rat:** Jackrong 0.8B distilled.  
Good for research, prompt-format mining, scaffold mining, maybe tiny summarizer/router experiments. Not a serious general worker. [Hugging Face+2Hugging Face+2](https://huggingface.co/Jackrong/Qwen3.5-0.8B-Claude-4.6-Opus-Reasoning-Distilled-GGUF)

The blunt bottom line:

*   If you want **small generalists**, start with **Qwen3.5-9B** and **4B**. [Hugging Face+1](https://huggingface.co/Qwen/Qwen3.5-9B)
*   If you want **specialized coding/editing**, **Stable-DiffCoder-8B** and **zeta-2** are more interesting than another random Qwen merge. [Hugging Face+1](https://huggingface.co/ByteDance-Seed/Stable-DiffCoder-8B-Instruct)
*   If you want **agent-loop behavior experiments**, **OmniCoder-2-9B** is a better target than most anonymous HF uploads because its card actually explains the training delta. [Hugging Face](https://huggingface.co/Tesslate/OmniCoder-2-9B)
*   If you want **SLMs and micro-models**, **Nemotron-3 Nano 4B** is the serious official one, and **Jackrong 0.8B** is the cheap weird one to mine for ideas. [Hugging Face+1](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16)

The next pass that would be most useful is a **role matrix** across your hardware tiers:

**role → recommended model(s) → 24 GB GPU / 16 GB GPU / M1 Pro fit → why it belongs there → what metric decides promotion or rejection**.

---

**Sources:**

- [Qwen/Qwen3.5-9B · Hugging Face](https://huggingface.co/Qwen/Qwen3.5-9B)

## Prompt:
4/1/2026, 4:45:49 AM

 🍎
LOOKING FOR HOSTING LLMS ON YOUR MAC? CLICK HERE →
💻
LOOKING TO RUN THIS ON A PC WITH NPU? CLICK HERE →
▓█████ ▓█████  ██▓      █████▒██░ ██  ▒█████    ██████ ▄▄▄█████▓ ██▓     ██▓     ███▄ ▄███▓
▒██    ▒██   ▀ ▓██▒    ▓██   ▒▓██░ ██▒▒██▒  ██▒▒██    ▒ ▓  ██▒ ▓▒▓██▒    ▓██▒    ▓██▒▀█▀ ██▒
▒▓██▄   ▒███   ▓██░    ▒████ ░▒██▀▀██░▒██░  ██▒▒▓██▄    ▒ ▓██░ ▒░▓██░    ▓██░    ▓██    ▓██░
▒██  ▀█▄ ▒▓█  ▄ ▒██▄    ░▓█▒  ░░▓█ ░██ ▒██   ██░ ▒   ██▒░ ▓██▓ ░ ▒██▄    ▒██▄    ▒██    ▒██ 
░██▄▄▄▄██░▒████▒░██████▒░▒█░   ░▓█▒░██▓░ ████▓▒░▒██████▒▒  ▒██▒ ░ ░██████▒░██████▒▒██▒   ░██▒
 ▓█   ▓██▒░ ▒░ ░░ ▒░▓  ░ ▒ ░    ▒ ░░▒░▒░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒░▓  ░░ ▒░▓  ░░ ▒░   ░  ░
GPU Memory Calculator for Self-Hosted LLM Inference
› HARDWARE CONFIGURATION
GPU Model:

Number of GPUs:

VRAM per GPU (GB):

System Overhead (GB):

› MODEL CONFIGURATION
Model Input Method:

Common Model

Parameters

Memory
Select Model:

Quantization:

Context Input Method:

Preset

Custom
Context Length:

KV Cache Overhead (%):

Use arrow keys to adjust
» CALCULATE CONFIGURATION «
═══ CALCULATION RESULTS ═══
How is this calculated?
Max Concurrent Requests:
1.37
Total VRAM Available:
24.0 GB
Model Memory Required:
4.0 GB
KV Cache per Request:
13.11 GB
Available for Inference:
18.0 GB
Effective Context Window:
16,384 tokens
═══ PERFORMANCE ESTIMATION ═══
How is this calculated?
Expected Speed:
182.59 tokens/sec
Time for 100 tokens:
0.5 seconds
Performance Rating:
🟢 Excellent
Performance Tips:

• Performance should be smooth for most use cases
› CALCULATION NOTES
• Model memory includes weights and activation overhead
• KV cache grows linearly with context length and batch size
• System overhead includes OS, drivers, and framework memory
• Quantization reduces precision but may impact model quality
• Professional GPUs (A100, H100) have better memory bandwidth
• Multiple GPUs require tensor parallelism for large models
Copyright © 2026 Eran Sandler
Fork on GitHubwould we have c context issue thats too low?

## Response:
4/1/2026, 4:45:51 AM

> Thought for 8s

Yes — **for many agent/code workloads, 16,384 effective context can be too low**.

The key thing in that calculator output is not the model weight size. It is the **KV cache per request**:

*   model memory: **4.0 GB**
*   available for inference: **18.0 GB**
*   KV cache per request: **13.11 GB**
*   effective context: **16,384**
*   max concurrent requests: **1.37**

That means the bottleneck is **runtime context memory**, not weights.

Why this matters:

A small quantized model can fit easily, but once you ask for:

*   long repo context
*   lots of pasted files
*   tool traces
*   XML / agent scaffolding
*   multiple turns kept live
*   concurrency >1

the **KV cache explodes**.

For your use case, **16k context is often not enough** if the model is acting as:

*   a repo-aware coding worker
*   a Claude Code style tool-user
*   a long-running subagent
*   anything that ingests large file sets or verbose tool outputs

It is usually okay for:

*   short edit tasks
*   narrow bugfixes
*   summarization of one file or one result
*   classification / routing / triage
*   very scoped helper agents

It is usually **not okay** for:

*   medium-large repo understanding
*   multi-file refactors
*   long tool-use chains
*   broad patch planning
*   “read all this code and act” tasks

The bigger problem in your screenshot is actually this:

**1.37 concurrent requests** is effectively **one real request**.

So even if raw speed says ~182 tok/s, that config is telling you:

*   good single-request speed
*   poor concurrency headroom
*   limited working context

That is a classic trap with small local setups: **tokens/sec looks good, but the usable worker capacity is weak**.

The practical interpretation for your stack:

*   **4B / tiny models on 24 GB**: great for short-context utility workers
*   **not enough by themselves** for your main high-context coding worker role if capped around 16k effective context
*   they belong in a lower tier of your routing stack, not the main deep-context lane

For your workload, I’d think of context tiers like this:

*   **8k–16k**: microtasks only
*   **16k–32k**: usable for many scoped coding tasks, still limited
*   **64k+**: where repo-aware worker behavior starts feeling much less cramped
*   **128k+**: where long-running agent/tool flows become much more comfortable

So yes, **that shown config likely has a context issue for your intended primary worker role**.

The raw fix options are:

1.  **Use the tiny model only for short-context roles**
2.  **Lower concurrency expectations**
3.  **Use a model/runtime/quant with lower KV pressure**
4.  **Push long-context jobs to a stronger local/burst tier**
5.  **Aggressively compress context before handing work to that model**

The right takeaway is not “4B is bad.”  
It is:

**4B is good for cheap narrow workers, but not as your main deep-context coding agent if 16k is the real effective window.**

If you want, I can break down **which of the 0.8B / 4B / 9B / 8B-specialist models belong in the “16k-safe utility worker” tier versus the “needs 32k–128k to be worth using” tier**.

## Prompt:
4/1/2026, 4:51:12 AM

use as price gauge 
Lightning.AI Logo
Request demo
Compute costs
Tiers
Compare features
FAQs
Get 80 free GPU hours monthly.
Then pay-as-you-go.
Start on the free tier with 80* free GPU hours. Pay as you go for more hours. Upgrade for enterprise features like bring your own cloud, use your AWS/GCP credits, SOC2, HIPAA, and 24/7 support.

Run 1 Studio free 24/7**. No credit card. No commitments.
*Prices vary
**Free Studios run 24/7 but require restart every 4 hours. No restrictions in Pro or higher.
CPU
1 GPU
2 GPU
4 GPU
8 GPU
Clusters
Name
GPUs
VRAM*
Cost/GPU/hr*
Cost/GPU/hr* (interruptible)
Free hours monthly**
T4
1
16 GB
$0.19
$0.51
﹘
$0.61
75
L4
1
24 GB
$0.48
$0.49
﹘
$0.59
31
L40S
1
48 GB
$2.89
$1.52
﹘
$1.83
5
RTXP 6000
1
96 GB
$2.89
$0.84
﹘
$1.01
2
A100
1
40 GB
$1.29
-
10
A100
1
80 GB
$2.71
$3.06
﹘
$3.67
5
H100
1
80 GB
$1.99
-
5
H200
1
141 GB
$3.50
-
3
*VRAM and price per GPU. Billed by the second.
**Free GPU hrs with 15 monthly free credits.
Access the world's best clouds from one place.
AWS
AWS
GCP
GCP
Lightning cloud
Lightning
Lambda labs
Lambda
Nebius
Nebius
NScale
NScale
Voltage park
Voltage
Lightning on your private cloud.
Use AWS/GCP commits, keep data private in your VPC. Run a secure, customized AI platform, without managing infrastructure.

Use cloud credits
Maximize AWS/GCP commitments.
Fully customizable
Build your dream AI platform - zero infra management.
SOC2 · HIPAA
Enterprise-grade security for your data.
Start Small, Scale Big
From solo projects to enterprise AI, choose a plan that grows with you.
Academic pricing

Free
$0
Students, researchers, hobbyists
Choose Free

15 monthly credits
Key features

1 free active Studio (4 hour restarts)
32 core CPU Studios
Single GPUs (L40S, A100, H100, H200...)
80% off on interruptible (spot)
Up to 2 concurrent GPUs
Persistent storage (50 GB limit)
15 req/min to our model APIs
120,000 tok/min to our model APIs
Connect any local IDE or SSH
Unlimited background execution
Multiplayer live collaboration
Use private and public models
Access optimized Studios
Automate with our SDK
Pay as you go
Pro
Monthly
Annual
$50
-60%
$20
per month
(billed annually)
Developers, researchers, scientists
Choose Pro

240 annual credits
Everything in Free, plus:

1 active Studio (no restarts)
64 core CPU
Multi-GPU (T4, L4, L40S)
Multi-node training (6 GPUs max)
Up to 6 concurrent GPUs
Persistent storage (200 GB limit)
20 req/min to our model APIs
120,000 tok/min to our model APIs
Connect public, private S3 buckets
Distributed data prep (up to 4 machines)
Reserve machines for jobs
Pay as you go for more credits
Teams
Monthly
Annual
$140
-15%
$119
/user, per month
(billed annually)
Research labs, small teams
Choose Teams

600 annual credits
Everything in Pro, plus:

1 active Studio (no restarts)
96 core CPU
Full-node A100, H100, H200
Multi-node training (12 GPUs max)
Up to 12 concurrent GPUs
Persistent storage (2 TB limit)
30 req/min to our model APIs
150,000 tok/min to our model APIs
Use via AWS marketplace
Real-time cost controls
Spending limits
Enterprise
Custom
Enterprise-grade AI
Request a quote

Custom credits
Everything in Teams, plus:

Use your cloud credits (AWS, GCP)
Priority GPU Access (Lightning Cloud)
Full-node B200s
Unlimited multi-node training
Unlimited concurrent GPUs
Deploy in your own VPC
Custom resource tagging
Custom rate limits for our model APIs
Enterprise AI Hub add-on
99.95% uptime SLA
SOC 2 (type 2) compliance
SAML/SSO
Bring your own images
Dedicated Slack support channel
Dedicated machine learning engineer
Role-based access controls
You have to try it to believe it.
350,000+ builders love Lightning AI
Prototype 6× faster
"Instead of taking 36 hours to know if this model works, we knew by the end of the day."

Sam, Researcher
MIT Sustainable Design Lab
Experiment at lightning speed
"We validated our hypothesis in just 4 weeks for under $10k. It would've taken us at least 70% longer if we did not have the Lightning platform!"

Malcolm, co-founder
OctAI
Debug together
"When it came time for our experts to collaborate on common experiments we ran into the “it works on my machine” problem. With Lightning, we saved hours per week."

Robin Cole, Researcher
EarthDaily Analytics
Change GPUs in seconds
"The experience of changing from CPU to GPU was mindblowing. It’s extremely quick and I didn’t even need to think about copying or mounting my files."

Irina, ML Engineer
Lightning User
No environment setup
"The environment management is so much better with Lightning AI; like an environment already provisioned for a workspace is a really good model."

Jacqueline, Sr. ML Engineer
Aeira
Compare features
Startup and academic pricing available. Annual pricing available.
Get in touch.
Free
Pro
Teams
Enterprise
Free
Students, researchers, hobbyists
Choose Free
Compute
Free active CPU Studios
1
Free active CPU Studio session limit
4 hours
Max inactive Studios
Unlimited
Free credits
15 monthly
Additional CPU/GPU credits
Pay-as-you-go
Max CPUs per Studio
32
Max GPUs per Studio
1
T4, L4, L40S session limit
Unlimited
A100, H100, H200 session limit
4 hours
Max concurrent GPUs
2
Cloud providers
All
Interruptible instances
Change Studio between CPU and GPUs
Reserve machines for jobs
-
Use without an AWS or GCP account
Basic cloud cost management
Organization level cloud cost management
-
Use your own AWS or GCP account
-
Set up a custom machine
-
Studio runtime
Ready-to-code (no CUDA setup, etc...)
Setup once, reuse any time
Code from the browser
Connect local IDE (VSCode, PyCharm, ...)
Notebooks on the browser
Sudo access
Terminal access
Connect via SSH
Background execution limit
Unlimited
Monitor system metrics real-time
Studio auto sleep
Customize auto sleep behavior
-
Auto switch to CPU when inactive
-
Build templates with Base Studios
1
Advanced configuration for Base Studios
-
Custom resource tagging
-
Bring your own images
-
Connect internal pip/conda mirrors
-
Data
Visualize/explore datasets
Upload data
Connect S3, GCS and R2 buckets
-
Create cloud-agnostic folders
High-performance storage (EFS/Filestore)
-
Free storage
10 GB
Persistent storage limit
50 GB
Additional storage
Pay-as-you-go
Collaboration
Multiplayer live collaboration
Private shared file system
Publish public Studios
Publish private Studios
Control data access
Create organizations
Auto join
-
Credits Auto-Reload
Teamspaces
Unlimited
Seat price
$0
AI workflows
Public models
Private models
Community templates
Pretrain, finetune models
Multi-node training (max GPUs)
-
Foundation model auto-babysitting
Distributed data prep
Distributed data prep (max CPU machines)
-
Host and share AI apps
Share public app links
Deploy no-code model endpoints
Deploy full control model endpoints
Access Studio plugins
Build your own Quests
-
Add your own plugins
-
Design your own ML platform
-
Enterprise AI Hub add-on
-
Model APIs req/min
15
Model APIs tok/min
120,000
Security
Secrets
End-to-end data encryption
SAML/SSO
-
Use your own AWS account
-
Lightning in your VPC
-
KMS Encryption
-
Lightning on prem
-
Role-based access controls
-
SOC2 (type 2) compliance
-
Bring your own encryption keys
-
Audit logs
-
Bring your own images
-
Connect to internal pip/conda mirrors
-
Support
Learn AI and deep learning
PyTorch Lightning support
Platform support
Uptime SLA
-
Expert model performance tuning
-
Get a custom gen AI model trained, deployed
-
AI strategy design
-
FAQs
What do you mean by running 24/7?
You can create unlimited Studios. At any one time, you can run one (CPU) Studio for free. If you want to run more at the same time, you must use your free credits or buy more credits.

Do you offer a trial?
Yes! The free tier is truly free! You can run 1 Studio for free and get 15 free credits per month. 15 free credits gets you ~80 GPU hours per month on interruptible machines. Prices may vary

Why do you need my phone number?
To prevent abuse of the platform.

How do the 15 free credits per month work?
Every month, we give you 15 free Lightning credits. If you don't use them, they expire. Use the credits to run additional Studios or for GPU hours.

When do free credits expire?
Free credits expire every month. Make sure to use them up!

When do purchased Lightning credits expire?
After 12 months.

How do I use AWS/GCP credits?
Upgrade to the enterprise tier to use your AWS/GCP credits.

Which cloud providers does Lightning support?
Currently AWS and GCP. Azure support is coming soon.

## Response:
4/1/2026, 4:51:13 AM

I’m using the Lightning page as a rough market check, not as truth for your exact deployment economics. The useful part is how their on-demand GPU prices bracket the value of your local 24 GB box and the “only rent when necessary” threshold.

> **Searching for official lightning pricing page**
>
> [Lightning AI](https://lightning.ai/pricing)
>
> **Searching for Lightning AI pricing information**
>
> [Lightning AI | Idea to AI product, ⚡️ fast.](https://lightning.ai/)
> [Lightning AI Pricing & Plans (March 2026)](https://www.saasworthy.com/product/lightning-ai/pricing)
> [Lightning AI Features, Pricing, Reviews & Overview (2026)](https://www.venkatsoftware.com/lightning-ai)
> [Top Serverless GPU Clouds for 2026](https://www.runpod.io/articles/guides/top-serverless-gpu-clouds)
> [Where Can I Get Free GPU Cloud Trials in 2026](https://www.gmicloud.ai/blog/where-can-i-get-free-gpu-cloud-trials-in-2026-a-complete-guide)
> [GPUs | Nvidia GPU power from the cloud - Katapult](https://katapult.io/products/gpus/)
> [NVIDIA H100 Pricing (March 2026): Cheapest Cloud GPU ...](https://www.thundercompute.com/blog/nvidia-h100-pricing)
>
> Thought for 11s

As a **price gauge**, Lightning is useful.

Not because it is the cheapest, but because it gives you a clean “what does a managed GPU hour cost right now?” reference point.

From the pricing page snippets surfaced in search, Lightning is showing roughly:

*   **T4 16 GB:** **$0.19/hr**
*   **L4 24 GB:** **$0.48/hr**
*   **L40S 48 GB:** **$2.89/hr**
*   **A100 40 GB:** **$1.29/hr**
*   **A100 80 GB:** **$2.71/hr**
*   **H100 80 GB:** **$1.99/hr**
*   **H200 141 GB:** **$3.50/hr**  
    and they say usage is **billed by the second** with free monthly credits on some tiers. [Lightning AI+1](https://lightning.ai/pricing/?utm_source=chatgpt.com)

That gives you a decent benchmark for your decision thresholds.

What this means for your setup
------------------------------

Your **3090 Ti 24 GB at home** should be treated as your default “free once sunk-cost is ignored” GPU. So every time you consider renting something, the real question is:

**Is this job worth more than the equivalent of an L4/A100 hour?**

Because Lightning’s numbers imply:

*   24 GB-class managed GPU time is around **L4 @ ~$0.48/hr**
*   40 GB-class serious burst is around **A100 40 GB @ ~$1.29/hr**
*   80 GB-class comfortable burst is around **$2–$2.7/hr** depending on H100/A100 80 GB. [Lightning AI+1](https://lightning.ai/pricing/?utm_source=chatgpt.com)

So your rough rental policy should be:

*   **Do not rent** just to run tiny 0.8B/4B/9B workers.
*   **Maybe rent** when you need a real 24 GB+ clean environment for batch experiments and don’t want to tie up your home box.
*   **Definitely rent** when context/KV/concurrency pressure means your local 24 GB card is the bottleneck, especially for bigger worker tiers.

On your context question with this pricing in mind
--------------------------------------------------

Yes, the context issue is still real.

If your local configuration is effectively landing near **16k useful context**, that is often too cramped for a primary code agent. In that case, using a cheap local 4B/9B worker for:

*   triage
*   summarization
*   small scoped edits
*   classification
*   routing
*   log reading

makes sense.

But for:

*   long repo context
*   multi-file edits
*   long tool traces
*   Claude Code-like iterative sessions
*   wider concurrent worker usage

you will hit the KV wall before you hit “model intelligence” limits.

That is exactly where a rented **40–80 GB** card becomes rational, because the point is not just “bigger model,” it is **more context + more concurrency + less KV pain**.

Practical price ladder
----------------------

Using Lightning as the market gauge, I’d think in these buckets:

### Local only

Use your home 24 GB GPU for:

*   official Qwen3.5-4B / 9B
*   0.8B / 4B distills
*   edit specialists like DiffCoder / zeta
*   cheap always-on worker lanes

No reason to rent for these unless you need temporary parallelism.

### Rent only when context or concurrency justifies it

A rented **A100 40 GB at ~$1.29/hr** or **H100 80 GB at ~$1.99/hr** is not that expensive if it saves real subscription burn or lets you run jobs your local stack simply cannot handle. [Lightning AI+1](https://lightning.ai/pricing/?utm_source=chatgpt.com)

At those prices:

*   a **4-hour burst** on A100 40 GB is about **$5.16**
*   a **4-hour burst** on H100 80 GB is about **$7.96**

That is cheap enough that you should not contort your whole architecture to avoid ever renting.

### Do not overuse managed cloud for things your MacBook or spare GPU can do

The **Jackrong 0.8B** or even many 4B-class experiments are so small that renting L4/A100 time for them is wasteful unless you are doing batched evals at scale. The 0.8B GGUF variants are sub-GB to ~1 GB scale, so they belong on:

*   MacBook MLX / local CPU-ish experiments
*   spare 16 GB GPU
*   sidecar lanes

not on premium rented GPUs.

Clean takeaway
--------------

Using Lightning as a price anchor, your architecture should be:

*   **MacBook / spare 16 GB / cheap local lanes** for 0.8B–4B experiments and tiny utility roles
*   **3090 Ti 24 GB** for your real always-on local worker lane
*   **burst 40–80 GB rentals** only for jobs where local context/concurrency becomes the limiting factor

So yes:

*   **16k-ish effective context is too low for your main deep code-agent lane**
*   but it is totally fine for a lot of specialized small-model roles
*   and Lightning’s pricing shows that jumping to a burst A100/H100 for the hard jobs is not financially insane at all. [Lightning AI+1](https://lightning.ai/pricing/?utm_source=chatgpt.com)

If you want, I’ll turn this into a **hardware-tier × model-size × max sensible role** chart using your 24 GB GPU, 16 GB GPU, and 16 GB MacBook.

---

**Sources:**

- [Lightning AI - Pricing](https://lightning.ai/pricing/?utm_source=chatgpt.com)

## Prompt:
4/1/2026, 4:52:49 AM

Do not rent just to run tiny 0.8B/4B/9B workers.
Maybe rent when you need a real 24 GB+ clean environment for batch experiments and don’t want to tie up your home box. we would onlyy rent to run models that are tiny as far as I can tell, and ones that can handle 4-16 concur reqs

## Response:
4/1/2026, 4:52:52 AM

You’re right — if the goal of renting is **throughput and concurrency**, not “fit a giant model,” then renting tiny models can make perfect sense. The real decision boundary is whether a rented GPU gives you materially better **4–16 request concurrency at acceptable context**, not whether the model itself is small.

> **Searching web for concurrency details and pricing**
>
> [Lightning AI - Pricing](https://lightning.ai/pricing/)
> [vLLM](https://docs.vllm.ai/en/latest/)
> [SGLang Documentation — SGLang](https://sgl-project.github.io/)
> [Qwen/Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B)
> [Adaptive Batching and number of concurrent requests ...](https://github.com/vllm-project/vllm/issues/10269)
> [vLLM Dynamic Batching - Runpod](https://www.answeroverflow.com/m/1371876938913677483)
> [PagedAttention vs Continuous Batching vs vLLM vs SGLang](https://python.plainenglish.io/pagedattention-vs-continuous-batching-vs-vllm-vs-sglang-a-practical-breakdown-4c19cc9e21c0)
> [Qwen/Qwen3.5-9B · Hugging Face : r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/comments/1rirlyb/qwenqwen359b_hugging_face/)
> [SGLang](https://docs.liquid.ai/deployment/gpu-inference/sglang)
> [SGLang documentation - SGLang](https://sgl-project-sglang-93.mintlify.app/introduction)
> [NVIDIA H100 Pricing (March 2026): Cheapest Cloud GPU ...](https://www.thundercompute.com/blog/nvidia-h100-pricing)
>
> Thought for 13s

Yes — in **your** case, renting tiny models can make total sense.

My earlier line was too blunt for your workload.

If the goal is **4–16 concurrent requests** with decent context and predictable latency, then the reason to rent is not “fit a huge model.” It is:

*   get a **clean GPU with more usable VRAM headroom**
*   preserve your **home 24 GB box**
*   get better **concurrency / batching behavior**
*   avoid the point where local KV cache and context pressure wreck throughput

That is exactly the kind of job where renting a “small-model server” is rational.

Lightning’s public pricing is actually a decent sanity check for this. Their page shows roughly **L4 24 GB at $0.48/hr**, **A100 40 GB at $1.29/hr**, and **H100 80 GB at $1.99/hr**. [Lightning AI+1](https://lightning.ai/pricing/?utm_source=chatgpt.com)

So the real question is not:

“Should I rent for a tiny model?”

It is:

“Does renting an L4/A100/H100 let this tiny model handle concurrency and context materially better than my home setup?”

For your use case, that answer is often **yes**.

Why tiny-model rentals can be the right move
--------------------------------------------

A model like **Qwen3.5-9B** officially supports a **262,144-token default context**, and Qwen explicitly warns that if you hit OOM you may need to reduce context, while also saying they advise keeping at least **128K** to preserve complex-task behavior. [Hugging Face+1](https://huggingface.co/Qwen/Qwen3.5-9B?utm_source=chatgpt.com)

That means the real issue is not whether a 9B model is “small.” The issue is whether your hardware can support the **context + KV cache + concurrency** you want.

And both **vLLM** and **SGLang** are built around exactly this serving problem:

*   vLLM emphasizes **continuous batching** to keep replicas saturated and maximize GPU utilization. [vLLM+1](https://docs.vllm.ai/en/stable/examples/offline_inference/batch_llm_inference/?utm_source=chatgpt.com)
*   SGLang explicitly advertises **continuous batching**, **prefill-decode disaggregation**, and **RadixAttention/prefix caching** for **high-throughput, low-latency** inference under many concurrent requests. [SGLang Documentation+2SGLang Documentation+2](https://sgl-project.github.io/?utm_source=chatgpt.com)

So if you want **4–16 simultaneous requests**, renting a GPU for a **9B or 4B** model is not weird at all. It can be the smart move because you are renting **serving headroom**, not just parameter capacity.

Where my earlier advice should be corrected
-------------------------------------------

Instead of:

> do not rent just to run tiny 0.8B/4B/9B workers

The better rule is:

> **do not rent tiny models for single-user, low-context work that your local hardware already handles well.**

But for:

*   **4–16 concurrent requests**
*   higher context
*   steady batch load
*   shared prefixes / common system prompts
*   agent workers with repeated tool scaffolding

renting small models is completely reasonable.

What I’d actually do
--------------------

### Rent 4B/9B-class models when:

*   you want **server-style concurrency**
*   you want **32K–128K+ usable context**, not a cramped local fallback
*   you want to test **batch economics**
*   you do not want to tie up the 3090 Ti
*   you want cleaner measurements than a mixed home box

### Do not rent them when:

*   it is one or two requests at a time
*   context is short
*   the MacBook / spare GPU / 3090 Ti can already handle it
*   the experiment is mostly about recipe quality rather than throughput behavior

The more important distinction
------------------------------

For you, rentals are not mainly for “big smart model” experiments.

They are for:

*   **throughput experiments**
*   **context experiments**
*   **concurrency experiments**
*   **serving stack experiments**
*   **cost-per-successful-task experiments**

That is different, and it makes tiny-model rentals valid.

My current recommendation
-------------------------

Use the tiers like this:

*   **Local Mac / spare 16 GB / 3090 Ti** for model-quality experiments, recipe mining, tiny jobs, and baseline evals
*   **Rent L4 / A100 / H100** when the experiment is about **4–16 concurrent requests**, **higher context**, or **serving efficiency**

With Lightning-like pricing, that means:

*   **L4** is your cheap concurrency/context test bed
*   **A100 40 GB** is your more serious “can this 9B worker actually breathe under real load?” tier
*   **H100 80 GB** is for when you want a strong upper bound on what the same small model can do when memory pressure is no longer the main problem [Lightning AI+1](https://lightning.ai/pricing/?utm_source=chatgpt.com)

So yes: **you may absolutely want to rent 0.8B/4B/9B models** — not because they are too large, but because your real bottleneck is likely **context + concurrency + clean batching**, not model fit.

---

**Sources:**

- [Lightning AI - Pricing](https://lightning.ai/pricing/?utm_source=chatgpt.com)
- [Qwen/Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B?utm_source=chatgpt.com)
- [Batch LLM Inference - vLLM](https://docs.vllm.ai/en/stable/examples/offline_inference/batch_llm_inference/?utm_source=chatgpt.com)
- [SGLang Documentation — SGLang](https://sgl-project.github.io/?utm_source=chatgpt.com)



---
Powered by [ChatGPT Exporter](https://www.chatgptexporter.com)