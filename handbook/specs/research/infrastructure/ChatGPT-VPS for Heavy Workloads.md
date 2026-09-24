# VPS for Heavy Workloads

**User:**   
**Created:** 4/1/2026 4:02:47  
**Updated:** 4/20/2026 17:32:39  
**Exported:** 4/20/2026 17:32:40  
**Link:** [https://chatgpt.com/c/69ccfb57-6488-8327-922b-bcd94ffb8142](https://chatgpt.com/c/69ccfb57-6488-8327-922b-bcd94ffb8142)  

## Prompt:
4/1/2026, 4:02:46 AM

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

## Response:
4/1/2026, 4:02:48 AM

I’m narrowing the model list by cutting out HF long-tail noise and keeping only options that look plausible for your latency and concurrency target on prosumer hardware.

It’s already pointing the same way: for 8–16 way concurrency with sub-5s TTFT, dense 27B is usually the wrong default and the real candidates are mostly ~3B-active MoE/hybrid families. I’ve got the official bases pinned down and I’m now separating those from community REAP/distill uploads that are basically just flashy quant dumps.

## Prompt:
4/1/2026, 4:14:24 AM

https://huggingface.co/caiovicentino1/models?sort=least_params https://huggingface.co/caiovicentino1/models?sort=least_params https://huggingface.co/danielcherubini/Qwen3.5-DeltaCoder-9B-GGUF https://huggingface.co/Drjkedwards/Recursive-Transformer-Model https://huggingface.co/caiovicentino1/models?sort=least_params https://huggingface.co/bigatuna/Qwen3.5-9b-Sushi-Coder-RL-GGUF perhaps can do our own fine tunes\quants\adaptres and other items over a base model too if needed im open o renting or purchasing addtl gpu but note:

current spend is 600$ a month + assumed 50$ on HW; our daily usage on just CC (1 out of 5 harnesses) is approx 100-400Mtok of constant work, we will need to optimally cost match to the subscriptions which provide near 0.005$ mtok pricing.but do have lower rate limtits both in concurrency and volume take al pooka t teh models I've shown, the dense 27-72bs being REAP or in other ways cut down to3 -9b size seems like the move. REAP\distills ar not flashy, read the benchmarks and evaluate. and factor int hat one guys advice + the advice of each repo + their strategies, it can be concatenated into one LLM strategy thats unified, factor in ALL of our conversation memories too

## Response:
4/1/2026, 4:14:26 AM

Two practical filters have emerged: ignore the 1080 Ti for a modern vLLM path, and treat many flashy HF REAP/distill uploads as fit/memory hacks unless they have real evals. For your box, the serious worker candidates are the official 30–35B A3B/REAP class—especially Qwen3.5-35B-A3B and GLM-4.7-Flash-REAP—while bigger Coder-Next variants look too uncomfortable on dual 24GB once concurrent KV cache is counted.

## Prompt:
4/1/2026, 4:15:11 AM

0.005 per million tokens! there are ways to merge hte 1080ti\3090ti. thought, also vllm vs sglang for out case

## Response:
4/1/2026, 4:15:12 AM

I’m folding your linked repos into a cost/perf pass now, but the frame has shifted: this is a serving-strategy problem first. I’m checking whether the REAP/distill/pruned variants have enough real provenance and eval signal to justify worker traffic, and whether their model shape, quant, and runtime can actually beat your current effective token cost at sustained load.

## Prompt:
4/1/2026, 4:16:08 AM

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

## Response:
4/1/2026, 4:16:10 AM

The economics are becoming the hard gate now: at a true $0.005 per million tokens target, only extremely high utilization on hardware you already own even has a shot. I’m comparing the specific repos and runtimes on throughput-per-dollar, plus whether the 3090 Ti + 1080 Ti idea helps or just poisons the worker stack.

I’m at the point where this splits into clear buckets: official models with real benchmark tables, community finetunes with at least some reproducible evidence, and interesting-but-not-production-credible experiments. Given your volume, the answer is shaping into a routed worker stack by request class, not one “best” model.

At this point the cheap-worker lane is basically down to 3B-active A3B/REAP models, with a small 9B dense tier as the lower-friction single-GPU fallback. I’m just sanity-checking whether any “near-lossless” prune/quant repos hold up beyond benchmark theater.

> ****
>
> The user wants to analyze and interpret a detailed usage and cost table for multiple AI models over several months, focusing on token consumption and related expenses for one out of five processing harnesses.
>
> **Synthesizing cost-effective LLM strategy**
>
> The user’s spending is around $600/month plus $50 for hardware, with daily usage of 100-400 million tokens. They’re interested in cost-efficient subscriptions with
>
> **Remembering**
>
> Looking back at our past interactions
>
> **Searching for REAP benchmarks and docs**
>
> To gather the right info, I should search for official documentation and
>
> **Analyzing power, throughput, and model requirements for Qwen3.5**
>
> [Models](https://huggingface.co/models?other=quantization)
>
> **Calculating throughput and power requirements for token processing**
>
> [caiovicentino1 (caio vicentino)](https://huggingface.co/caiovicentino1/models?sort=least_params)
>
> **Inspecting benchmark details**
>
> I’ll search for relevant benchmark info
>
> **Analyzing token throughput and compute power requirements**
>
> [danielcherubini/Qwen3.5-DeltaCoder-9B-GGUF · Hugging Face](https://huggingface.co/danielcherubini/Qwen3.5-DeltaCoder-9B-GGUF)
>
> **Analyzing throughput and power requirements for token systems**
>
> [bigatuna/Qwen3.5-9b-Sushi-Coder-RL-GGUF · Hugging Face](https://huggingface.co/bigatuna/Qwen3.5-9b-Sushi-Coder-RL-GGUF)
>
> **Analyzing token throughput and compute cost efficiency**
>
> [danielcherubini/Qwen3.5-DeltaCoder-9B-GGUF · Hugging Face](https://huggingface.co/danielcherubini/Qwen3.5-DeltaCoder-9B-GGUF)
>
> **Looking for additional benchmarks**
>
> I think I might need more information from the "Reaper" page, possibly a comparison or benchmark for
>
> **Calculating token throughput and power requirements**
>
> [reaperdoesntknow/Qwen3-1.7B-Coder-Distilled-SFT · Hugging Face](https://huggingface.co/reaperdoesntknow/Qwen3-1.7B-Coder-Distilled-SFT)
>
> **Searching for benchmarks and model details**
>
> I need to find benchmarks related to
>
> **Searching for Qwen3.5 models and related information**
>
> [bigatuna/Qwen3.5-9b-Sushi-Coder-RL-GGUF](https://huggingface.co/bigatuna/Qwen3.5-9b-Sushi-Coder-RL-GGUF)
>
> **Analyzing power and throughput for large-scale token processing**
>
> [Qwen/Qwen3.5-9B · Hugging Face](https://huggingface.co/Qwen/Qwen3.5-9B)
>
> **Calculating token output and hardware requirements**
>
> [Jackrong/Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2 · Hugging Face](https://huggingface.co/Jackrong/Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2)
>
> **Analyzing token throughput and compute power requirements**
>
>
> **Confirming image citation and next steps**
>
> It looks like I can directly cite these image references since they are from open sources. I'll just ensure clarity by verifying the source information. As for the Bigatuna results,
>
> **Estimating token throughput and system requirements**
>
> [bigatuna/Qwen3.5-9b-Sushi-Coder-RL-GGUF · Hugging Face](https://huggingface.co/bigatuna/Qwen3.5-9b-Sushi-Coder-RL-GGUF)
>
> **Searching power and throughput requirements for Qwen3.5**
>
> [Supported Models - vLLM](https://docs.vllm.ai/en/latest/models/supported_models/)
> [Oxen-AI/sglang-qwen3.5: SGLang is a high-performance ...](https://github.com/Oxen-AI/sglang-qwen3.5)
> [REAP: One-Shot Pruning for Trillion-Parameter Mixture-of- ...](https://www.cerebras.ai/blog/reap)
> [SGLang - Qwen](https://qwen.readthedocs.io/en/latest/deployment/sglang.html)
> [Speculative decoding — Tutorials for AI developers 12.0](https://rocm.docs.amd.com/projects/ai-developer-hub/en/latest/notebooks/inference/speculative_decoding_deep_dive.html)
> [Supported Models - SGLang](https://sgl-project-sglang-93.mintlify.app/models/supported-models)
> [vLLM vs SGLang vs MAX — Who's the fastest? - Erik Steiger](https://ersteiger.com/posts/vllm-vs-max/)
> [cerebras/Step-3.5-Flash-REAP-121B-A11B](https://huggingface.co/cerebras/Step-3.5-Flash-REAP-121B-A11B)
> [Serve the Qwen3.5 Vision-Language Model with SGLang](https://frontend.modal.com/docs/examples/sglang_vlm)
> [Compared performance of vLLM vs SGLang on 2 Nvidia ...](https://www.reddit.com/r/LocalLLaMA/comments/1jjl45h/compared_performance_of_vllm_vs_sglang_on_2/)
> [Cerebras - Meet REAP: the Reaper for redundant experts.](https://www.linkedin.com/posts/cerebras-systems_meet-reap-the-reaper-for-redundant-experts-activity-7384995428871884800-jq6h)
> [SGLang Documentation — SGLang](https://sgl-project.github.io/)
> [[Help Needed] Building vLLM dependencies inside ...](https://forums.developer.nvidia.com/t/help-needed-building-vllm-dependencies-inside-sglang-official-image-for-eagle-3-speculative-decoding/353485)
>
> **Analyzing power and throughput for token processing**
>
> [Supported Models - vLLM](https://docs.vllm.ai/en/latest/models/supported_models/)
> [Supported Models - SGLang](https://sgl-project-sglang-93.mintlify.app/models/supported-models)
> [SGLang Documentation — SGLang](https://sgl-project.github.io/)
> [SGLang - Qwen](https://qwen.readthedocs.io/en/latest/deployment/sglang.html)
> [Cerebras](https://www.cerebras.ai/blog/reap)
>
> **Looking into vLLM support and SGLang docs**
>
> I should check for vLLM-supported models,
>
> **Analyzing throughput and power for large-scale token processing**
>
> [Supported Models - vLLM](https://docs.vllm.ai/en/latest/models/supported_models/)
> [Supported Models - SGLang](https://sgl-project-sglang-93.mintlify.app/models/supported-models)
> [SGLang Documentation — SGLang](https://sgl-project.github.io/)
>
> **Analyzing token throughput and hardware requirements**
>
> [Supported Models - vLLM](https://docs.vllm.ai/en/latest/models/supported_models/)
>
> **Looking up SGLang features and decoding**
>
> I should search for specific information on SGLang's speculative decoding and features, as well as any details on quantization. It might help to open separate documentation pages for these topics so I can get a clearer understanding of how they work before I dive into anything else.
>
> **Searching for SGLang documentation on decoding and optimization**
>
>
> **Analyzing token throughput and compute power requirements**
>
> [Speculative Decoding — SGLang](https://docs.sglang.io/advanced_features/speculative_decoding.html)
>
> **Inspecting SGLang components**
>
> I need to check out the relevant lines related to SGLang's PD, KV cache, and parsers. These are likely important details to understand. I think using the search function or opening specific files or sections will help pinpoint the key elements for further inspection.
>
> **Calculating token throughput and power requirements**
>
> [Quantized KV Cache — SGLang](https://docs.sglang.io/advanced_features/quantized_kv_cache.html)
>
> **Opening SGLang PD page**
>
> I should look closely at the S
>
> **Analyzing power and throughput for token processing**
>
> [PD Disaggregation — SGLang](https://docs.sglang.io/advanced_features/pd_disaggregation.html)
>
> **Checking vLLM docs for reasoning tools and quantization**
>
> I
>
> **Searching vLLM documentation for Qwen3 optimizations**
>
> [qwen3_reasoning_parser - vLLM](https://docs.vllm.ai/en/stable/api/vllm/reasoning/qwen3_reasoning_parser/)
>
> **Searching compute costs and throughput for Qwen models**
>
> [Qwen/Qwen3.5-35B-A3B](https://huggingface.co/Qwen/Qwen3.5-35B-A3B)
>
> **Inspecting 35B model details**
>
> I should look at the 35
>
> **Calculating power and throughput for high token output**
>
> [Qwen/Qwen3.5-35B-A3B · Hugging Face](https://huggingface.co/Qwen/Qwen3.5-35B-A3B)
>
> **Considering benchmarks and model performance**
>
> It seems
>
> **Searching GPU requirements for CUDA compute scalability**
>
> [GPU - vLLM](https://docs.vllm.ai/en/stable/getting_started/installation/gpu/)
> [SGLang Custom Build Environment](https://github.com/flox/sglang-dev)
>
> **Searching for official NVIDIA CC info**
>
> I might need to check out the official
>
> **Searching CUDA compute capability for NVIDIA GPUs**
>
> [CUDA GPU Compute Capability](https://developer.nvidia.com/cuda/gpus)
> [3090 & 3090 Ti Graphics Cards | NVIDIA GeForce](https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3090-3090ti/)
> [TensorRT with Tensorflow Evaluation on 1080Ti](https://forums.developer.nvidia.com/t/tensorrt-with-tensorflow-evaluation-on-1080ti/83902)
> [List of Nvidia graphics processing units](https://en.wikipedia.org/wiki/List_of_Nvidia_graphics_processing_units)
> [GPU Recommendation for XGBoost with MATLAB R2022b](https://www.mathworks.com/matlabcentral/answers/2176435-gpu-recommendation-for-xgboost-with-matlab-r2022b)
> [NVIDIA GPU Compute Capability - Lei Mao's Log Book](https://leimao.github.io/blog/NVIDIA-GPU-Compute-Capability/)
> [Nvidia's GPUs have been considered some of the best on ...](https://www.facebook.com/SlashGear/posts/nvidias-gpus-have-been-considered-some-of-the-best-on-the-market-including-the-t/1644622073890858/)
>
> **Exploring NVIDIA compute cap details**
>
> I might want to check out lines from the official NVIDIA compute cap search page
>
> **Estimating computational requirements for high token throughput**
>
> [CUDA GPU Compute Capability | NVIDIA Developer](https://developer.nvidia.com/cuda/gpus)
> [GPU - vLLM](https://docs.vllm.ai/en/v0.10.1/getting_started/installation/gpu.html)
>
> **Clarifying 3090 Ti BF16 support**
>
> It seems we might not need detailed hardware-specific info for the
>
> **Estimating power and throughput for large-scale token usage**
>
>
> **Analyzing power and throughput requirements for token processing**
>
> [caiovicentino1/Qwen3.5-9B-Claude-Opus-PolarQuant-Q5 · Hugging Face](https://huggingface.co/caiovicentino1/Qwen3.5-9B-Claude-Opus-PolarQuant-Q5)
>
> **Searching compute requirements for high throughput models**
>
> [nvidia/Nemotron-Cascade-2-30B-A3B](https://huggingface.co/nvidia/Nemotron-Cascade-2-30B-A3B)
>
> **Calculating power, throughput, and cost for computation**
>
> [zai-org/GLM-4.7-Flash · Hugging Face](https://huggingface.co/zai-org/GLM-4.7-Flash)
>
> **Exploring GLM-4.7 and Kimi base benchmarks**
>
> I need to dive deeper into the GLM-4.7 and Kimi base benchmarks. The website gives enough information, but Kimi base might not
>
> **Evaluating power, throughput, and token processing at scale**
>
>
> **Continuing analysis and refining GPU rental search**
>
> To fully answer the user's question, I need to dive
>
> **Searching benchmarks for Qwen3.5 model performance**
>
> [pszemraj/LocalLLaMA-posts · Datasets at Hugging Face](https://huggingface.co/datasets/pszemraj/LocalLLaMA-posts)
>
> **Checking rental GPU pricing**
>
> The search results are not giving me much. It might be better to go directly to the pages I already have and check there. I do need to find current rental GPU pricing though, so I’ll go ahead and search for that specifically to
>
> **Calculating GPU costs for large-scale token processing**
>
> [Pricing](https://www.runpod.io/pricing)
> [Rent RTX 3090 GPUs on Vast.ai for $0.13/hr](https://vast.ai/pricing/gpu/RTX-3090?srsltid=AfmBOooZYWpcbWpBsL-Z1ljhEL2oW_70J1vUEEE9yn9gsO7WQrHi1y4u)
> [AI Cloud Pricing | GPU Compute & AI Infrastructure](https://lambda.ai/pricing)
> [TensorDock GPU Pricing - Real-time Availability - GPUPerHour](https://gpuperhour.com/providers/tensordock)
> [GPU Cloud Pricing Comparison 2026: Every Major ...](https://www.spheron.network/blog/gpu-cloud-pricing-comparison-2026/)
> [TensorDock GPU Pricing: Compare 10+ GPUs](https://computeprices.com/providers/tensordock)
> [RTX 3090 Cloud Pricing: Compare 5+ Providers (2026)](https://getdeploying.com/gpus/nvidia-rtx-3090)
> [Runpod GPU pricing: A complete breakdown and platform ...](https://northflank.com/blog/runpod-gpu-pricing)
> [NVIDIA RTX 3090 GPU Price Comparison](https://gpus.io/en/gpus/rtx3090)
> [IO vs Lamdba Labs and alternatives: Comparing GPU ...](https://io.net/blog/io-vs-lamdba-labs-and-alternatives-comparing-gpu-cloud-pricing-and-features)
> [GPU Cloud](https://www.tensordock.com/cloud-gpus.html)
>
> **Gathering current GPU prices**
>
> I’m thinking about searching for the current prices of GPUs like the 3090, 4090, or 5090, especially used ones, since the user might be considering purchasing. While I could check official retail prices for new models, second-hand prices are often more relevant
>
> **Analyzing token throughput for computational resources**
>
> [Flagstone8878/Qwen3.5-18B-REAP-A3B-Coding · Hugging Face](https://huggingface.co/Flagstone8878/Qwen3.5-18B-REAP-A3B-Coding)
>
> **Estimating performance and power requirements for token throughput**
>
> [12bitmisfit/Qwen3-Coder-30B-A3B-Instruct_Pruned_REAP-15B-A3B-GGUF · Hugging Face](https://huggingface.co/12bitmisfit/Qwen3-Coder-30B-A3B-Instruct_Pruned_REAP-15B-A3B-GGUF)
>
> **Searching GPU compute requirements for SGLang throughput**
>
>
> **Addressing GPU compatibility and options**
>
> It seems the 1080 Ti isn't viable for
>
> **Searching for Qwen model benchmarks and power usage**
>
> [Qwen/Qwen3-Coder-Next](https://huggingface.co/Qwen/Qwen3-Coder-Next)
>
> **Calculating token throughput and power requirements**
>
> [Qwen/Qwen3-Coder-Next · Hugging Face](https://huggingface.co/Qwen/Qwen3-Coder-Next)
>
> **Searching benchmarks for Qwen3-Coder-Next performance**
>
> [Qwen3-Coder-Next Technical Report](https://arxiv.org/html/2603.00729v1)
> [SWE-bench Leaderboards](https://www.swebench.com/)
> [Qwen/Qwen3-Coder-Next](https://huggingface.co/Qwen/Qwen3-Coder-Next)
> [Qwen3-Coder-Next: Pushing Small Hybrid Models](https://qwen.ai/blog?id=qwen3-coder-next)
> [Qwen3.5-35B-A3B hits 37.8% on SWE-bench Verified Hard](https://www.reddit.com/r/LocalLLaMA/comments/1rkdlqi/qwen3535ba3b_hits_378_on_swebench_verified_hard/)
> [Qwen3-Coder-Next Technical Report (Qwen Team ...](https://www.facebook.com/groups/3670562573177653/posts/4454529284780974/)
> [Qwen3-Coder-Next Technical Report](https://alphaxiv.org/overview/2603.00729v1)
> [Qwen3-Coder-Next API](https://www.together.ai/models/qwen3-coder-next)
> [Qwen3-Coder-Next: The Complete 2026 Guide to Running ...](https://dev.to/sienna/qwen3-coder-next-the-complete-2026-guide-to-running-powerful-ai-coding-agents-locally-1k95)
> [Qwen3‑Coder‑Next: A 3B‑Active Beast for Local Coding ...](https://medium.com/data-science-in-your-pocket/qwen3-coder-next-a-3b-active-beast-for-local-coding-agents-84ea4233f152)
> [Qwen3-Coder: Agentic Coding in the World](https://qwenlm.github.io/blog/qwen3-coder/)
> [Qwen3-Coder-Next: How to Run Locally](https://unsloth.ai/docs/models/qwen3-coder-next)
> [SWE-rebench Leaderboard](https://swe-rebench.com/)
> [How to Access and Use Qwen3-Coder-Next?](https://www.analyticsvidhya.com/blog/2026/02/qwen3-coder-next/)
>
> **Evaluating token throughput and power requirements for rigs**
>
> [Qwen](https://qwen.ai/blog?id=qwen3-coder-next)
> [SWE-rebench Leaderboard](https://swe-rebench.com/)
>
> **Reviewing relevant benchmark details**
>
> It looks like SWE-rebench didn’t provide the
>
> **Analyzing throughput and power requirements for token processing**
>
> [cerebras/GLM-4.7-Flash-REAP-23B-A3B · Hugging Face](https://huggingface.co/cerebras/GLM-4.7-Flash-REAP-23B-A3B)
>
> **Estimating power and hardware requirements for token throughput**
>
> [cerebras/Kimi-Linear-REAP-35B-A3B-Instruct · Hugging Face](https://huggingface.co/cerebras/Kimi-Linear-REAP-35B-A3B-Instruct)
>
> **Considering pricing and cost calculations**
>
> I was thinking about searching for current GPT-5 mini or Claude Haiku API pricing, since the user mentioned a target cost of $0.005/mtok. But maybe instead of directly comparing pricing, I could calculate costs based on popular usage metrics, like 100-400M tokens/day, and rental prices. I’ll also need throughput assumptions for more precise
>
> **Analyzing throughput and power requirements for token handling**
>
> [caiovicentino1/Qwen3.5-9B-PolarQuant-Q5 · Hugging Face](https://huggingface.co/caiovicentino1/Qwen3.5-9B-PolarQuant-Q5)
>
> **Analyzing token throughput and compute requirements for models**
>
> [caiovicentino1/Qwen3.5-9B-Claude-Opus-PolarQuant-Q5 · Hugging Face](https://huggingface.co/caiovicentino1/Qwen3.5-9B-Claude-Opus-PolarQuant-Q5)
>
> **Searching power and throughput requirements for token handling**
>
> [zai-org/GLM-4.7-Flash](https://huggingface.co/zai-org/GLM-4.7-Flash)
>
> **Evaluating model benchmarks**
>
> I believe
>
> **Calculating power and throughput for AI rigs**
>
> [bigatuna/Qwen3.5-9b-Sushi-Coder-RL-GGUF · Hugging Face](https://huggingface.co/bigatuna/Qwen3.5-9b-Sushi-Coder-RL-GGUF)
>
> **Analyzing throughput and power requirements for token processing**
>
> [reaperdoesntknow/Qwen3-1.7B-Coder-Distilled-SFT · Hugging Face](https://huggingface.co/reaperdoesntknow/Qwen3-1.7B-Coder-Distilled-SFT)
>
> **Inspecting Qwen3.5-DeltaCoder lines**
>
> I
>
> **Analyzing tokens per second and hardware requirements**
>
> [danielcherubini/Qwen3.5-DeltaCoder-9B-GGUF · Hugging Face](https://huggingface.co/danielcherubini/Qwen3.5-DeltaCoder-9B-GGUF)
>
> **Analyzing token throughput and power requirements for rigs**
>
> [GPU Pricing](https://www.runpod.io/gpu-pricing)
> [GPU Cloud — TensorDock](https://www.tensordock.com/cloud-gpus.html)
>
> **Analyzing power and throughput requirements for token processing**
>
> [GPU Pricing](https://www.runpod.io/gpu-pricing)
>
> **Searching for information on prefix caching and decoders**
>
> [Disaggregated Prefilling (experimental) - vLLM](https://docs.vllm.ai/en/latest/features/disagg_prefill/)
>
> **Searching for efficiency and compute optimization techniques**
>
>
> **Reviewing sources and focusing on official docs**
>
> The
>
> **Remembering**
>
> Looking back at our past interactions
>
> **Optimizing worker selection for various tiers**
>
> For bulk tasks, starting with the Jackrong 9B v2 is a solid base, then compare it to DeltaCoder v1.1-DPO and Sushi-Coder-RL. For premium tasks, consider GLM-4.7-Flash-REAP-23B-A3B or Qwen3-Coder-30B-A3B. For rare intensive cases, opt for API overflow/quality fallback. Ensure solid task data distillation.
>
> **Calculating token throughput and compute requirements**
>
> [SWE-rebench Leaderboard](https://swe-rebench.com/)
>
> **Refining focus for GPU worker model and approach**
>
> I couldn’t find the Qwen3-Coder-30B row, but there’s good data around line 216. Now, I should search more on GLM-4.7 Flash vs GPT-5 mini, which I already have a snippet for. This worker model should be isolated from self-hosted services. Also, handling KV cache carefully is key.
>
> **Analyzing power and throughput requirements for token processing**
>
> [Qwen/Qwen3.5-27B · Hugging Face](https://huggingface.co/Qwen/Qwen3.5-27B)
>
> **Searching power and throughput for GPU configurations**
>
> [CUDA GPU Compute Capability](https://developer.nvidia.com/cuda/gpus)
> [3090 & 3090 Ti Graphics Cards | NVIDIA GeForce](https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3090-3090ti/)
> [CUDA](https://en.wikipedia.org/wiki/CUDA)
> [V1.10 fails to detect my Nvidia 1080 Ti - Topaz Community](https://community.topazlabs.com/t/v1-10-fails-to-detect-my-nvidia-1080-ti/99969)
> [CUDA Toolkit 13.2 - Release Notes](https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html)
>
> **Searching compute capability for VLLM performance**
>
> [FP8 W8A8 - vLLM](https://docs.vllm.ai/en/stable/features/quantization/fp8/)
>
> **Evaluating SGLang references**
>
> I
>
> **Calculating power and throughput for token generation**
>
> [Jackrong/Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled · Hugging Face](https://huggingface.co/Jackrong/Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled)
>
> **Reviewing documentation and performance comparisons**
>
> I could cite some references from previous documents and check DeltaCoder's
>
> **Searching for information on SGLang performance and specs**
>
> [SGLang Documentation — SGLang](https://sgl-project.github.io/)
> [Speculative Decoding (EAGLE / EAGLE3) - sglang-jax](https://github.com/sgl-project/sglang-jax/blob/main/docs/features/speculative_decoding.md)
> [Efficient LLM Serving with MTP: DeepSeek V3 and SGLang ...](https://rocm.blogs.amd.com/software-tools-optimization/mtp/README.html)
> [SGLang: An Efficient Open-Source Framework for Large- ...](https://qingkeai.online/upload/pdf/20250713/SGLang.pdf)
> [Tool Calling - vLLM](https://docs.vllm.ai/en/latest/features/tool_calling/)
> [SGLang v0.4: Zero-Overhead Batch Scheduler, Cache- ...](https://lmsys.org/blog/2024-12-04-sglang-v0-4/)
> [Qwen3-Coder-Next: The Complete 2026 Guide to Running ...](https://dev.to/sienna/qwen3-coder-next-the-complete-2026-guide-to-running-powerful-ai-coding-agents-locally-1k95)
> [SGLang: Efficient Execution of Structured Language Model ...](https://proceedings.neurips.cc/paper_files/paper/2024/file/724be4472168f31ba1c9ac630f15dec8-Paper-Conference.pdf)
> [Tool Calling - SGLang](https://sgl-project-sglang-93.mintlify.app/advanced/tool-calling)
> [From KV Cache to Zero Overhead Scheduling](https://www.linkedin.com/pulse/from-kv-cache-zero-overhead-scheduling-understanding-sglangs-zhao-oc7nc)
> [SGLang - Qwen](https://qwen.readthedocs.io/en/latest/deployment/sglang.html)
> [Part 1: Shared Prefix, KV Cache, and RadixAttention](https://medium.com/%40dharamendra1314.kumar/sglang-learning-series-part-1-shared-prefix-kv-cache-and-radixattention-d7a847d20b1f)
> [SGLang Speculative Decoding Tutorial: How to Deploy ...](https://company.hpc-ai.com/blog/sglang-speculative-decoding-tutorial)
> [GLM-4.7 with SGLang](https://openlm.ai/glm-4.7/)
>
> **Searching benchmarks for speculative decoding and rig performance**
>
> [SGLang Documentation — SGLang](https://sgl-project.github.io/)
>
> **Searching for EAGLE-3 decoding performance details**
>
>
> **Searching power and throughput for token handling calculations**
>
> [SGLang Documentation — SGLang](https://sgl-project.github.io/)
>
> **Analyzing token throughput and power requirements**
>
> [Qwen/Qwen3.5-27B · Hugging Face](https://huggingface.co/Qwen/Qwen3.5-27B)
>
> **Estimating power and throughput for token processing systems**
>
> [Jackrong/Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2 · Hugging Face](https://huggingface.co/Jackrong/Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2)
> [danielcherubini/Qwen3.5-DeltaCoder-9B-GGUF · Hugging Face](https://huggingface.co/danielcherubini/Qwen3.5-DeltaCoder-9B-GGUF)
>
> **Analyzing token throughput and compute costs**
>
>
> **Analyzing power and throughput for high-scale compute**
>
> [Qwen/Qwen3-Coder-Next · Hugging Face](https://huggingface.co/Qwen/Qwen3-Coder-Next)
>
> **Searching power and throughput for AI models**
>
> [zai-org/GLM-4.7-Flash](https://huggingface.co/zai-org/GLM-4.7-Flash)
>
> **Inspecting sources for Qwen3.5-27B and SGLang details**
>
> I think I can use the benchmark specifics from
>
> **Searching SGLang documentation for performance and optimization**
>
>
> **Searching SGLang cache and attention documentation**
>
> [Quantized KV Cache - SGLang](https://sgl-project-sglang-93.mintlify.app/optimization/quantized-kv-cache)
> [PD Disaggregation - sgl-project/sglang](https://github.com/sgl-project/sglang/blob/main/docs/advanced_features/pd_disaggregation.md)
> [SGLang Documentation — SGLang](https://sgl-project.github.io/)
> [Disaggregation | NVIDIA Dynamo Documentation](https://docs.nvidia.com/dynamo/dev/backends/sg-lang/disaggregation)
> [Quantized KV Cache - vLLM](https://docs.vllm.ai/en/v0.9.2/features/quantization/quantized_kvcache.html)
> [Model inference with Prefill-Decode disaggregation](https://dstack.ai/blog/pd-disaggregation/)
> [Part 1: Shared Prefix, KV Cache, and RadixAttention](https://medium.com/%40dharamendra1314.kumar/sglang-learning-series-part-1-shared-prefix-kv-cache-and-radixattention-d7a847d20b1f)
> [Unleashing AMD Instinct™ MI300X GPUs for LLM Serving](https://rocm.blogs.amd.com/software-tools-optimization/disaggregation/README.html)
> [Fast and Expressive LLM Inference with RadixAttention ...](https://lmsys.org/blog/2024-01-17-sglang/)
> [SGLang Deployment & Inference Guide](https://unsloth.ai/docs/basics/inference-and-deployment/sglang-guide)
> [RadixAttention and Multi-Turn Inference on GPU Cloud ...](https://www.spheron.network/blog/sglang-production-deployment-guide/)
> [Nexus: Proactive Intra-GPU Disaggregation of Prefill and ...](https://arxiv.org/html/2507.06608v5)
> [SGLang · Hugging Face](https://huggingface.co/docs/inference-endpoints/engines/sglang)
> [Disaggregated Prefill/Decode using SGlang and nixl (Dual ...](https://forums.developer.nvidia.com/t/disaggregated-prefill-decode-using-sglang-and-nixl-dual-nvidia-rtx-pro-6000-blackwell/361316)
> [Serving SGLang: Launch a Production-Style Server](https://learnopencv.com/sglang-a-production-server/)
>
> **Evaluating user’s token spend and harness data**
>
> I might want to review vLLM docs on prefill or speculative decoding, but I already have some references. The user gave a table that lists token usage, though the numbers are hard to read due to truncation. I'll focus on their daily usage estimate (100
>
> **Searching compute requirements for SGLang on NVIDIA GPUs**
>
> [SGLang](https://docs.nvidia.com/deeplearning/frameworks/pdf/SGLang-Release-Notes.pdf)
> [[Bug] [sgl-kernel] nvidia DGX (sm121a) cannot use FA4 in ...](https://github.com/sgl-project/sglang/issues/20363)
> [SGLang](https://docs.clarifai.com/compute/toolkits/sglang/)
> [Attention Backends - Mini-SGLang](https://www.mintlify.com/sgl-project/mini-sglang/configuration/attention-backends)
> [Build SGLang from source on Blackwell Pro 6000/ DGX ...](https://forums.developer.nvidia.com/t/build-sglang-from-source-on-blackwell-pro-6000-dgx-spark/360785)
> [Installation - Mini-SGLang](https://mintlify.com/sgl-project/mini-sglang/installation)
> [MiniMax M2.1 Model SGLang Deployment Guide](https://huggingface.co/MiniMaxAI/MiniMax-M2.1/blob/refs%2Fpr%2F16/docs/sglang_deploy_guide.md)
> [How to Install and Use SGLang](https://www.gpu-mart.com/blog/how-to-install-and-use-sglang)
> [SGLang Documentation — SGLang](https://sgl-project.github.io/)
> [SGLang: The Complete Guide to High-Performance LLM ...](https://inference.net/content/sglang-complete-guide)
> [SGLang: Fast Serving Framework for Large Language and ...](https://rocm.blogs.amd.com/artificial-intelligence/sglang/README.html)
>
> **Estimating throughput and compute requirements for tokens**
>
> [Qwen/Qwen3.5-27B · Hugging Face](https://huggingface.co/Qwen/Qwen3.5-27B)
>
> **Analyzing power and throughput for high tok/s rigs**
>
> [Qwen/Qwen3.5-27B · Hugging Face](https://huggingface.co/Qwen/Qwen3.5-27B)
>
> **Analyzing power and throughput for large-scale models**
>
> [Qwen/Qwen3-Coder-30B-A3B-Instruct · Hugging Face](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct)
> [SWE-rebench Leaderboard](https://swe-rebench.com/)
>
> **Estimating compute requirements for token throughput**
>
> [danielcherubini/Qwen3.5-DeltaCoder-9B-GGUF · Hugging Face](https://huggingface.co/danielcherubini/Qwen3.5-DeltaCoder-9B-GGUF)
>
> **Reviewing quantized model options**
>
> I might consider searching for Jackrong GGUF or quantized versions
>
> **Searching power and throughput for Qwen models**
>
>
> **Calculating throughput and power requirements for token processing**
>
> [huggingface.co](https://huggingface.co/caiovicentino1/Qwen3.5-35B-A3B-EOQ-Q5-compressed/resolve/main/README.md?download=true)
>
> **Looking up hardware requirements and Qwen benchmarks**
>
> I could mention hardware details for Nemotron and GLM, potentially referencing multi-GPU needs, but I think it's manageable without that. I also want to look up Qwen's official blog for Coder Next benchmarks instead of relying on a snippet—I'll search for the Qwen.ai blog for more accurate
>
> **Searching performance benchmarks for Qwen3-Coder-Next**
>
> [Qwen3-Coder-Next: Pushing Small Hybrid Models](https://qwen.ai/blog?id=qwen3-coder-next)
>
> **Analyzing token throughput and compute requirements**
>
> [Qwen](https://qwen.ai/blog?id=qwen3-coder-next)
>
> **Considering Qwen's performance and citation approach**
>
> The search snippet from the official Qwen blog might be enough
>
> **Searching benchmarks for Qwen3-Coder-Next performance**
>
> [Qwen3-Coder-Next is the top model in SWE-rebench ...](https://www.reddit.com/r/LocalLLaMA/comments/1rn476o/qwen3codernext_is_the_top_model_in_swerebench/)
> [SWE-rebench Leaderboard](https://swe-rebench.com/)
> [Qwen3‑Coder‑Next: A 3B‑Active Beast for Local Coding ...](https://medium.com/data-science-in-your-pocket/qwen3-coder-next-a-3b-active-beast-for-local-coding-agents-84ea4233f152)
> [Qwen3-Coder-Next: Pushing Small Hybrid Models](https://qwen.ai/blog?id=qwen3-coder-next)
> [Qwen3-Coder-Next Technical Report](https://arxiv.org/html/2603.00729v1)
> [Qwen3-Coder-Next: How to Run Locally](https://unsloth.ai/docs/models/qwen3-coder-next)
> [Qwen3-Coder-Next: The Complete 2026 Guide to Running ...](https://dev.to/sienna/qwen3-coder-next-the-complete-2026-guide-to-running-powerful-ai-coding-agents-locally-1k95)
> [Qwen3-Coder-Next (Qwen3-Next-80B) CPU inference ~5x ...](https://github.com/ggml-org/llama.cpp/issues/19480)
> [Qwen3-Coder-Next Scores 40% on SWE-Rebench with 3B ...](https://www.linkedin.com/posts/thenextgentechinsider_qwen3codernext-swerebench-agentcoding-activity-7434891080598220800-RUKR)
> [unsloth/Qwen3-Coder-Next-GGUF](https://huggingface.co/unsloth/Qwen3-Coder-Next-GGUF/discussions/20)
> [Qwen3 Coder Next - API Pricing & Providers](https://openrouter.ai/qwen/qwen3-coder-next)
> [if you're serious about AI, read this. trust me.](https://x.com/DavidOndrej1/status/2022686855519670577)
> [This Week in Local AI — llama.cpp Gets MCP, Qwen3-Coder- ...](https://buttondown.com/insiderllm/archive/this-week-in-local-ai-llamacpp-gets-mcp-qwen3/)
> [Kimi](https://techstacks.io/tech/kimi)
> [Qwen3 4B (Non-reasoning) vs. Qwen3 Coder Next - LLMBase](https://llmbase.ai/compare/qwen3-4b-instruct%2Cqwen3-coder-next/)
> [SWE-rebench Leaderboard](https://swe-rebench.com/)
>
> Thought for 49m 36s

Bluntly: if you literally mean **$0.005 per million tokens**, that target is fantasy for self-hosted GPU inference. At your own stated volume, 100M tokens/day budgets **$0.50/day** and 400M budgets **$2/day**. For reference, Together’s hosted **Qwen3-Coder-Next** is priced at **$0.50/M input** and **$1.20/M output**, so your target is roughly **100x–240x lower** than an already-optimized commercial open-weight endpoint. [Together AI](https://www.together.ai/models/qwen3-coder-next?utm_source=chatgpt.com)

The good news is that **REAP itself is real**. Cerebras’ REAP writeup and paper argue that **expert pruning beats expert merging on generative MoE tasks**, and their first-party checkpoints back that up: **GLM-4.7-Flash-REAP-23B-A3B** stays essentially flat on HumanEval/HumanEval+, while **Kimi-Linear-REAP-35B-A3B** remains close to base quality and improves some evals while being **30% lighter**. So the idea is sound. The problem is that a lot of community REAP uploads still have weak cards, weak evals, or no evals at all. [arXiv+2Hugging Face+2](https://arxiv.org/html/2510.13999v1)

Here’s what actually survives scrutiny from the pile you dropped.

1.  **Qwen3-Coder-Next** is the strongest high-upside agentic-coding candidate, but it is **not** the easy one-card local path. The official card positions it as a coding-agent/local-dev model with **80B total / 3B activated**, **256K context**, and official support in **SGLang >= 0.5.8** and **vLLM >= 0.15.0**. Together reports **74.2% SWE-bench Verified**, **69.9% Aider**, and **39.3% Terminal-Bench 2.0**, which is serious. I would treat it as the best **escalation model** once you have matching VRAM, not as the cheap default worker. [Together AI+4Hugging Face+4Hugging Face+4](https://huggingface.co/Qwen/Qwen3-Coder-Next)
2.  **Qwen3.5-27B** is the best serious candidate for a strong local coder on your current kind of hardware. Qwen’s own published table gives it **72.4% SWE-bench Verified**, **41.6 Terminal Bench 2**, and **80.7 LiveCodeBench v6**; in that same table it slightly beats the table’s **GPT-5-mini** row on several items, including SWE-bench Verified, LongBench v2, GPQA Diamond, LiveCodeBench, and IFEval. Anthropic says **Claude Haiku 4.5** scores **73.3% on SWE-bench Verified** and is aimed at parallelized, high-volume work, so Qwen3.5-27B is at least in the right published band. Treat that as directional, not absolute, because scaffold choice changes these numbers. [Hugging Face+2Anthropic+2](https://huggingface.co/Qwen/Qwen3.5-27B)
3.  **Qwen3.5-9B** is the best default-worker candidate. Officially it lands at **65.6 LiveCodeBench v6**, **66.1 BFCL-V4**, **79.1 TAU2-Bench**, and **18.0 DeepPlanning**. That is not “replace Haiku/mini for hard coding-agent work,” but it is exactly the kind of model you can **replicate**, route aggressively, and use for the cheap half of traffic. [Hugging Face](https://huggingface.co/Qwen/Qwen3.5-9B)
4.  **GLM-4.7-Flash** and **GLM-4.7-Flash-REAP-23B-A3B** are real alternatives, not fluff. The official GLM card calls Flash a **30B-A3B** model and reports **59.2% SWE-bench Verified** and **64.0 LCB v6**; the REAP variant keeps **95.1 HumanEval** and **89.0 HumanEval+** while being **25% lighter**, and Cerebras says it deploys in current vLLM without source hacks. The downside is ecosystem maturity: the GLM card says local support in vLLM/SGLang is on their **main branches**, which is not my favorite place to anchor production unless the bakeoff forces you there. [Hugging Face+2Hugging Face+2](https://huggingface.co/zai-org/GLM-4.7-Flash)
5.  **Kimi-Linear-REAP-35B-A3B** is interesting if your real prompts are huge. Moonshot says the base Kimi Linear architecture can cut KV-cache need by **up to 75%** and improve long-context decode throughput by **up to 6x** at **1M context**, and the REAP variant is **30% lighter** while staying close to base quality and improving some evals such as MBPP+, LiveCodeBench, and AIME25. For a worker that mostly emits **50–100 tokens** with tight TTFT, I would not make this the default lane unless long context is actually the bottleneck. [Hugging Face+1](https://huggingface.co/moonshotai/Kimi-Linear-48B-A3B-Instruct)

Now the part where most of the community uploads fall apart.

I would **not** build the core fleet around **reaperdoesntknow/Qwen3-1.7B-Coder-Distilled-SFT**, **DeltaCoder-9B**, **Drjkedwards/Recursive-Transformer-Model**, **Flagstone8878’s 18B REAP**, **12bitmisfit’s 15B REAP**, or the **RepublicOfKorokke** oQ quant pack. The reaper card explicitly says it is **not for general code generation**; DeltaCoder’s published eval section is tiny; RTM admits it has **no public quantitative benchmark results**; Flagstone’s safetensor page says the README is empty and the GGUF page has **no model card**; 12bitmisfit’s safetensor and GGUF pages also have **no model card**; and RepublicOfKorokke reports mostly generic MMLU/HellaSwag/GSM8K-style numbers rather than the coding-agent evals you actually care about. These are lab curiosities, not foundation stones. [Hugging Face+7Hugging Face+7Hugging Face+7](https://huggingface.co/reaperdoesntknow/Qwen3-1.7B-Coder-Distilled-SFT)

The **Jackrong** and **bigatuna** stuff is the middle ground: not nonsense, but not “just trust the downloads” either. Jackrong’s **27B Claude-4.6-Opus reasoning distill** is interesting because the card says it fixes the developer-role template issue, preserves thinking mode, and community testing reports roughly **16.5 GB VRAM** at **Q4\_K\_M** with around **29–35 tok/s** on a single RTX 3090. The **9B v2** card says it was retrained for shorter, more efficient reasoning and explicitly warns that broader general-purpose capability may dip because the showcased gains are mainly on HumanEval/HumanEval+. That makes them excellent A/B candidates, not something I’d crown in advance. [Hugging Face+2Hugging Face+2](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled)

**bigatuna/Qwen3.5-9b-Sushi-Coder-RL** is genuinely promising, but it is still a lab model. Its card shows SFT on an Opus-reasoning dataset plus codeforces CoTs, then RL with Hermes-agent/Atropos, and it reports a matched local BF16 vLLM run where the RL model beats base **Qwen3.5-9B** by a wide margin on a LiveCodeBench task. That is enough to test seriously. It is not enough to make it the default worker without reproducing the gain on **your** harness. [Hugging Face+2Hugging Face+2](https://huggingface.co/bigatuna/Qwen3.5-9b-Sushi-Coder-RL-GGUF)

The **caiovicentino1** models are best understood as **deployment tech**, not base-model proof. PolarEngine v4 explicitly calls itself a **research artifact** and says for production to prefer **PolarQuant Q5 + torchao**; PolarQuant Q5 claims about **43 tok/s**, **7.1 GB VRAM**, and roughly **5x KV-cache context extension**; the EOQ-compressed 27B card shows about **2x storage reduction** with effectively **zero runtime overhead after load**. That is useful after you pick the winning base model. It is not evidence that a mediocre base magically becomes your production answer. [Hugging Face+3Hugging Face+3Hugging Face+3](https://huggingface.co/caiovicentino1/Qwen3.5-9B-PolarEngine-v4)

On **vLLM vs SGLang**, my call for your situation is simple: **start with vLLM, graduate to SGLang**. Qwen’s official cards support both vLLM and SGLang, but vLLM currently gives you the smoother path for the exact model families you’re testing, plus first-party Qwen recipes, speculative decoding support, per-request LoRA serving, and dynamic LoRA loading. Its docs are also very explicit that **MTP/speculative decoding is mostly a latency play under low-to-medium QPS** and can **reduce throughput under load**, which matters because the flashy dual-3090 numbers you pasted are not the same thing as a real **8–16 concurrent** worker lane. vLLM also tells you to use KV-cache logs to validate whether you actually have the concurrency headroom you think you have. [vLLM+6Hugging Face+6Hugging Face+6](https://huggingface.co/Qwen/Qwen3.5-27B)

**SGLang** becomes the better endgame when you stop playing with one box and start building a real serving fabric. Its runtime stacks **RadixAttention** prefix caching, a zero-overhead CPU scheduler, **prefill/decode disaggregation**, expert parallelism for MoE, data-parallel replicas for throughput, and multi-LoRA batching. Its own docs say data parallelism is the simplest and most effective way to scale throughput when the model fits, and the router/disaggregation pieces are exactly the kind of stuff you care about once you are optimizing TTFT and concurrency across a fleet instead of a single machine. [SGLang Documentation+3GitHub+3GitHub+3](https://github.com/sgl-project/sglang)

On your hardware question: **do not try to fuse a 1080 Ti and a 3090 Ti into one worker**. vLLM says a single inference instance does **not natively support heterogeneous GPUs** for sharding a model, and NVIDIA’s own forum thread confirms the **3090 Ti does not have NVLink**. More importantly, vLLM’s scaling docs say that on boxes **without NVLINK**, pipeline parallelism can actually beat tensor parallelism, so the real issue is not “no bridge,” it is “mismatched cards and ugly deployment geometry.” The 1080 Ti can still be a totally separate low-tier lane or background box, but I would not spend engineering time trying to make it behave like part of one modern inference worker. [vLLM Forums+2NVIDIA Developer Forums+2](https://discuss.vllm.ai/t/how-to-run-a-model-use-heterogeneous-gpus/1360)

So the unified strategy is this: **stop looking for one magic community prune/distill to replace Opus/Haiku everywhere. Build a routing stack.** Use **Qwen3.5-9B** as the default cheap worker and A/B it against **Jackrong 9B v2** and **bigatuna Sushi-Coder-RL**. Use **Qwen3.5-27B** as the escalation model on current 3090Ti-class hardware. Keep **Qwen3-Coder-Next** as the serious next step once you have enough **matching VRAM** or rented capacity. Only after a base model wins on your harness should you start layering in **PolarQuant/EOQ**, **LoRAs**, or custom speculators. That is how you get the cheap half of traffic local without betting your whole pipeline on anonymous Hugging Face uploads. [SGLang Documentation+4Hugging Face+4Hugging Face+4](https://huggingface.co/Qwen/Qwen3.5-9B)

My direct verdict: **vLLM first, Qwen3.5-9B as the base worker, Qwen3.5-27B as the practical local escalator, Qwen3-Coder-Next as the serious upside bet once you add matching VRAM, REAP only from first-party or well-evaluated sources, and no heroic 1080Ti+3090Ti fusion project.**

---

**Sources:**

- [Qwen3-Coder-Next API | Together AI](https://www.together.ai/models/qwen3-coder-next?utm_source=chatgpt.com)
- [https://arxiv.org/html/2510.13999v1](https://arxiv.org/html/2510.13999v1)
- [https://huggingface.co/Qwen/Qwen3-Coder-Next](https://huggingface.co/Qwen/Qwen3-Coder-Next)
- [https://github.com/sgl-project/sglang](https://github.com/sgl-project/sglang)
- [https://discuss.vllm.ai/t/how-to-run-a-model-use-heterogeneous-gpus/1360](https://discuss.vllm.ai/t/how-to-run-a-model-use-heterogeneous-gpus/1360)

## Prompt:
4/1/2026, 4:35:10 PM

![Uploaded image](https://chatgpt.com/backend-api/estuary/content?id=file_000000001a4871f8a02d695d37278b94&ts=493536&p=fs&cid=1&sig=f53bc3273c5082effc42d0152bd028e49857f633e484c9827ac63ba3c3b520e0&v=0)

The target needs to be for a 4-blend to 9-blend parameter models, concurrency to get about 8 to 16 at a time. The factor needs to be to minimize about 50 tokens per second inference speed. Self-hosted or rented GPU hardware should be doable for this, doesn't matter what hardware, what models we factor in, and then what techniques to be applied to minimize model compute needs, as well as optimize context needs to minimize that as well.

## Response:
4/1/2026, 4:35:13 PM

Thought for 35m 18s

Answer now

Assuming “UnitedTI” was a typo and you mean **three 24 GB NVIDIA cards plus one separate 40 GB NVIDIA card on PCIe**, the plan changes a lot.

I would **not** try to turn the 24 GB cards plus the 40 GB card into one pooled inference box. vLLM’s own guidance says a single inference instance is not meant to shard across heterogeneous GPUs, and its scaling guide says that on machines without NVLINK you should usually prefer **pipeline parallelism** over tensor parallelism. With mixed 24 GB / 40 GB VRAM, separate model servers are the sane design. [vLLM Forums+1](https://discuss.vllm.ai/t/how-to-run-a-model-use-heterogeneous-gpus/1360)

Your **three 24 GB cards** should be the **cheap worker fleet**. For your target pattern—short 50–100 token outputs and roughly 8–16 concurrent requests—**replicated smaller workers** are a better fit than one sharded larger model, because vLLM’s concurrency is bounded by KV-cache budget and its default scheduling explicitly optimizes **TTFT**. The clean starting point is **Qwen3.5-9B**: the official card says it works with **vLLM and SGLang**, and reports **65.6 LiveCodeBench v6**, **66.1 BFCL-V4**, and **79.1 TAU2-Bench**. [Hugging Face+3vLLM+3vLLM+3](https://docs.vllm.ai/en/stable/serving/parallelism_scaling/)

On top of that 9B base, I would only spend time on a **small A/B set**, not fifty hobby merges. The ones worth testing are: **Jackrong 9B v2** if you want shorter, cheaper reasoning traces; **DeltaCoder 9B** if tool-calling and self-verification are the pain point; and **Sushi-Coder-RL** only as an experiment, because its GGUF page is a **multimodal export** that expects an **mmproj** file rather than a clean plain-text serving package. [Hugging Face+2Hugging Face+2](https://huggingface.co/Jackrong/Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF?utm_source=chatgpt.com)

The **40 GB card** should be your **smart lane**, not another cheap lane. The strongest practical dense escalator here is still **Qwen3.5-27B**: the official card shows **72.4 SWE-bench Verified** and **41.6 Terminal Bench 2**, and it ships with native **262,144** context plus official vLLM/SGLang recipes. That huge context is useful for deeper jobs but terrible for cheap-worker economics, so keep 27B as **selective escalation**, not the default lane. If you want a REAP candidate, the first one I’d benchmark is **GLM-4.7-Flash-REAP-23B-A3B** from Cerebras, not random community prunes; Cerebras describes it as **25% lighter** with near-identical performance, while the base **GLM-4.7-Flash** card reports **59.2 SWE-bench Verified** and **79.5 τ²-Bench**. I would **postpone Qwen3-Coder-Next** until you can give it a homogeneous multi-GPU lane; its own card describes it as **80B total / 3B activated** and shows vLLM/SGLang deployment with reduced context if OOM appears. [Hugging Face+6Hugging Face+6Hugging Face+6](https://huggingface.co/Qwen/Qwen3.5-27B)

The **16 GB MacBook** is useful, but only as **edge assist**. MLX uses Apple silicon’s **unified memory**, and **MLX LM** supports quantization, low-rank and full fine-tuning, plus distributed inference/fine-tuning on Apple silicon. That makes it good for a **small draft/speculator**, reranker, embeddings, or adapter experiments, but not something I’d count as primary backend capacity for your main concurrent pool. [GitHub+2GitHub+2](https://github.com/ml-explore/mlx?utm_source=chatgpt.com)

On the serving stack, I’d start with **vLLM**, not SGLang. vLLM already has explicit **Qwen3.5 recipes**, TTFT-oriented scheduling, pipeline-parallel guidance for PCIe/no-NVLINK boxes, and **dynamic LoRA serving**. The crucial bit is that the official Qwen3.5 recipe says **MTP-1** is for **latency-sensitive, low-concurrency** serving and **trades away throughput under load**. That is exactly why I would **not** copy the aggressive community MTP settings straight into your 8–16-concurrent worker lane. **SGLang** becomes the better phase-two move only after you standardize hardware and actually need its **data-parallel router, PD disaggregation, multi-LoRA batching, and broader serving fabric**. [SGLang Documentation+3vLLM+3vLLM+3](https://docs.vllm.ai/en/stable/serving/parallelism_scaling/)

The **$20/month external budget** is not real baseline GPU capacity. Runpod currently lists **RTX 3090 at $0.22/hr** and **L4 at $0.44/hr**, while Vast lists **RTX 3090 from $0.13/hr**. That means $20 buys only about **91 hours** of Runpod 3090 time, **45 hours** of Runpod L4 time, or **154 hours** of Vast 3090 time—roughly **6% to 21% of a month**. So treat that money as **burst budget** for benchmark sweeps, one-off fine-tunes, or proving whether a model deserves permanent local hardware. [Runpod+1](https://www.runpod.io/gpu-pricing?utm_source=chatgpt.com)

So the build I’d actually run is this: **3×24 GB = replicated 9B workers**, **1×40 GB = 27B / first-party REAP escalation lane**, **MacBook = edge helper/speculator/reranker**, **$20 external = burst-only**. If you buy more hardware later, don’t buy another random 24 GB card. Buy a **matching 40–48 GB NVIDIA card**, because the next real step up is a **homogeneous high-end lane**, not more mixed-VRAM plumbing. [Hugging Face+3vLLM Forums+3vLLM+3](https://discuss.vllm.ai/t/how-to-run-a-model-use-heterogeneous-gpus/1360)

The concrete model shortlist I’d test first is: **Qwen3.5-9B**, **Jackrong 9B v2**, **DeltaCoder 9B** on the cheap lane; **Qwen3.5-27B** and **GLM-4.7-Flash-REAP-23B-A3B** on the smart lane.

Assuming you mean **4B–9B-class worker models**, the Together H200 screen you showed is the wrong tier. That H200 page is for **clusters of 256–1,000 GPUs**, and Together’s public pricing page currently lists H200 at **$4.19/hr on-demand** or **$3.49 / $3.19 / $2.89 reserved** depending on term. That is cluster-scale infra, not the sane starting point for a 4B–9B worker lane. [Together AI+1](https://www.together.ai/gpu-cluster-request/h200)

Also, the **$0.005 per million tokens** target is not a real rented-GPU number. RunPod’s current pricing page lists **RTX 3090 at $0.22/hr, RTX 4090 at $0.34/hr, RTX 5090 at $0.69/hr, and L40S at $0.79/hr**. To hit **$0.005/M tokens**, you would need roughly **12,222 tok/s** on a 3090, **18,889 tok/s** on a 4090, **38,333 tok/s** on a 5090, **43,889 tok/s** on an L40S, and a Together **H200 at $4.19/hr** would need about **232,778 tok/s**. So self-hosting can absolutely beat expensive API lanes, but it will not match that subscription-style token math unless the hardware is already sunk cost and utilized absurdly well. [Runpod+1](https://www.runpod.io/gpu-pricing)

For 4B–9B workers, **one 24–32GB GPU is enough to host the model**. Qwen3.5-9B is a **9B** model with **262,144-token native context** and official compatibility with **vLLM and SGLang**; Qwen3.5-4B has the same context and compatibility. NVIDIA lists **24GB** on the **3090 Ti** and **32GB** on the **5090**. So model fit is not the hard part anymore; **concurrency and KV-cache pressure** are. As a sanity check, a Q4\_K\_M GGUF export of a 9B Qwen3.5 fine-tune is **5.63GB**, and Q8\_0 is **9.53GB**. [Hugging Face+6Hugging Face+6Hugging Face+6](https://huggingface.co/Qwen/Qwen3.5-9B)

Model-wise, I would keep it narrow. **Qwen3.5-9B** is the default worker. Official Qwen benchmarks put it at **65.6 LiveCodeBench v6**, **66.1 BFCL-V4**, **79.1 TAU2-Bench**, and **18.0 DeepPlanning**; **Qwen3.5-4B** comes in lower on coding but is still useful as a cheap gate/summarizer lane. For tuned variants, only A/B a few: **bigatuna/Qwen3.5-9b-Sushi-Coder-RL** is interesting because its card shows a **matched local BF16 vLLM LiveCodeBench gain** over base Qwen3.5-9B; **DeltaCoder-9B** is aimed specifically at **tool-call JSON reliability** on top of Qwen3.5-9B using **LoRA + DPO**; **Jackrong v2** is worth testing if you want **shorter reasoning traces**, but its own card says broader general-purpose quality may be slightly impacted. I would not build the main lane around **Recursive-Transformer-Model**; that card is basically a conceptual architecture page from **2019**, not a current production serving candidate. [Hugging Face+5Hugging Face+5Hugging Face+5](https://huggingface.co/Qwen/Qwen3.5-9B)

On runtime, my call is **vLLM first, SGLang when you need a real replica pool**. vLLM gives you **automatic prefix caching, chunked prefill, disaggregated prefill, LoRA serving, and multiple quantization paths**. Its own Qwen3.5 recipe explicitly warns that **MTP/speculative decoding improves per-token latency at low concurrency but hurts throughput under load**, and vLLM’s disaggregated-prefill docs explicitly say it helps **tail inter-token latency** but **does not improve throughput**. SGLang becomes more attractive once you care about **fleet-level throughput and routing**: its docs highlight **RadixAttention** prefix sharing, **PD disaggregation**, **quantized KV cache**, **multi-LoRA batching**, and **tensor/pipeline/expert/data parallelism**, and its server-args docs explicitly say **data parallelism is better for throughput if memory allows**. [GitHub+7vLLM+7vLLM+7](https://docs.vllm.ai/en/latest/features/automatic_prefix_caching/)

So the sizing answer depends on what **“50 tok/s”** means.

If you mean **~50 tok/s aggregate across all active requests**, your existing **3090 Ti** can pilot this. Renting just buys headroom. On current RunPod list pricing, always-on cost is about **$158/mo for a 3090**, **$245/mo for a 4090**, **$497/mo for a 5090**, and **$569/mo for an L40S**. For this case, I would rather run **2–4 cheaper replicas behind a router** than one premium card. [Runpod](https://www.runpod.io/gpu-pricing)

If you mean **~50 tok/s per request at 8–16 concurrent**, that is **not a single-card problem**. That is a **400–800 tok/s decode-pool problem**, plus TTFT control. I would size that as **2–4 replicas of 4090 / 5090 / L40S-class hardware**, or H100-class if you want fewer boxes. At current RunPod list pricing, that is about **$490/mo for 2×4090**, **$979/mo for 4×4090**, **$1,138/mo for 2×L40S**, and **$2,275/mo for 4×L40S**. A Together H200 is **$2,513–$3,017/mo per GPU** by the public pages, so it only starts to make sense if you are consolidating a lot more than one 4B–9B worker lane. [Together AI](https://www.together.ai/pricing)

To cut compute and context cost, do this:

*   **Cap the hot path** to something like **4K–8K**, maybe **16K** max. Qwen3.5 supports **262K**, but exposing that whole window to the main worker just burns KV cache and batch room. Long-context jobs should go to a separate queue or lane. [Hugging Face+1](https://huggingface.co/Qwen/Qwen3.5-9B)
*   Keep the **system prompt, tool schema, and harness scaffolding identical** across requests so **vLLM APC** or **SGLang RadixAttention** can reuse prefixes instead of recomputing them. [vLLM+1](https://docs.vllm.ai/en/latest/features/automatic_prefix_caching/)
*   On **Ampere** like the 3090 Ti, stick to **AWQ / GPTQ / INT4 / Marlin-style weight compression**. vLLM’s hardware table shows **AWQ, GPTQ, and Marlin** are supported on Ampere, while full **FP8 W8A8** is officially **Ada/Hopper-only**. On **Ada/Hopper**, FP8 is much more attractive. [vLLM+1](https://docs.vllm.ai/en/latest/features/quantization/)
*   Use **MTP/speculative decoding only on latency lanes**, not on the saturated shared lane. vLLM’s own Qwen3.5 guide says it reduces per-token latency but degrades throughput under load. [vLLM](https://docs.vllm.ai/projects/recipes/en/latest/Qwen/Qwen3.5.html)
*   If prompts are long, use **chunked prefill** or **prefill/decode split** to protect TTFT and tail latency. vLLM explicitly says disaggregated prefill helps tail latency control, but **not throughput**. [vLLM+1](https://docs.vllm.ai/en/stable/configuration/optimization/)
*   Fine-tune with **LoRA + SFT/DPO on your own accepted harness traces** instead of retraining whole models. vLLM can serve LoRA adapters **per request with minimal overhead**, and DeltaCoder is basically that playbook applied to tool-using Qwen3.5-9B. [vLLM+1](https://docs.vllm.ai/en/v0.8.1/features/lora.html)

One experimental path that is actually worth watching is **caiovicentino1’s PolarQuant** work. His Qwen3.5-9B page reports **43.1 tok/s at 6.5GB VRAM** for **PolarQuant Q5 + torchao**, versus **45.7 tok/s and 17.9GB VRAM** for FP16, and he explicitly says that **PolarQuant Q5 + torchao** is the recommended production approach while **PolarEngine v4** is a research artifact. That is promising, but I would still treat it as R&D until you reproduce it on your hardware and harness. [Hugging Face](https://huggingface.co/caiovicentino1/Qwen3.5-9B-PolarEngine-v4)

And no, I would **not** try to pool the **1080 Ti + 3090 Ti** into one vLLM worker. vLLM does **not natively support running a single model across heterogeneous GPUs in one inference instance**. Use the **3090 Ti** as the main 9B worker and the **1080 Ti** for **embeddings, reranking, a 4B gate/summarizer lane, or a canary worker**. If you add more GPU, make it a **matching card** and scale with **replicas**; if you ever do multi-GPU on PCIe/no-NVLINK boxes, vLLM’s own guidance is to prefer **pipeline parallelism over tensor parallelism**. For 4B–9B workers, though, **replicas are cleaner than heroic tensor-parallel hacks**. [vLLM Forums+1](https://discuss.vllm.ai/t/how-to-run-a-model-use-heterogeneous-gpus/1360)

My direct recommendation: **3090 Ti at home + vLLM + Qwen3.5-9B as the main worker, Qwen3.5-4B as a cheap gate/summarizer, A/B Sushi-Coder-RL and DeltaCoder, hard-cap hot-path context, exact-prefix-cache everything, and scale to 2–4 replicas behind SGLang router only when the single box saturates.**

---

**Sources:**

- [https://www.together.ai/gpu-cluster-request/h200](https://www.together.ai/gpu-cluster-request/h200)
- [https://www.runpod.io/gpu-pricing](https://www.runpod.io/gpu-pricing)
- [https://huggingface.co/Qwen/Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B)
- [https://docs.vllm.ai/en/latest/features/automatic_prefix_caching/](https://docs.vllm.ai/en/latest/features/automatic_prefix_caching/)
- [https://discuss.vllm.ai/t/how-to-run-a-model-use-heterogeneous-gpus/1360](https://discuss.vllm.ai/t/how-to-run-a-model-use-heterogeneous-gpus/1360)

## Prompt:
4/4/2026, 9:15:38 AM

Kvcis and other papers?

## Response:
4/4/2026, 9:15:39 AM

Thought for 15m 17s

Answer now

Yep — **KVCIS** is real. Google Research describes it as **KV-Cache Importance Scoring**, a method that predicts token importance from intermediate activations **before attention is computed**, so KV compression can happen at cache-insertion time instead of after attention scores are available. [Google Research](https://research.google/pubs/kvcis-activation-based-token-importance-prediction-for-intelligent-kv-cache-compression-2/)

For your use case, I’d read papers in this order.

**1\. Serving-system papers first.** These usually matter more than exotic compression tricks for a 4B–9B worker lane.

*   **PagedAttention / vLLM**: paged KV memory management plus KV sharing; reports **2–4× throughput** at the same latency versus prior systems. [arXiv](https://arxiv.org/abs/2309.06180)
*   **SGLang**: **RadixAttention** for KV reuse and faster structured decoding; reports up to **6.4× higher throughput** on varied LM workloads. [arXiv+1](https://arxiv.org/abs/2312.07104)
*   **Sarathi-Serve**: **chunked prefills** and stall-free scheduling; reports **2.6× higher serving capacity** for Mistral-7B on one A100 under tail-latency constraints. [arXiv](https://arxiv.org/abs/2403.02310)
*   **DistServe**: splits **prefill** and **decode** onto different GPUs to improve goodput under TTFT/TPOT constraints. [arXiv](https://arxiv.org/html/2401.09670v2)

**2\. KV-cache papers second.** These matter once KV memory is actually the bottleneck.

*   **H2O**: heavy-hitter plus recency-based KV eviction. [arXiv](https://arxiv.org/abs/2306.14048?utm_source=chatgpt.com)
*   **Scissorhands**: “persistence of importance”; reports up to **5× KV memory reduction** without quality loss, and can combine with quantization. [arXiv+1](https://arxiv.org/abs/2305.17118?utm_source=chatgpt.com)
*   **StreamingLLM**: attention sinks for streaming and long multi-round interactions. [arXiv+1](https://arxiv.org/abs/2309.17453?utm_source=chatgpt.com)
*   **SnapKV**: predicts important KV positions from an observation window near the prompt end; reports **3.6× generation speed** and **8.2× memory efficiency** at 16K input. [arXiv+1](https://arxiv.org/abs/2404.14469?utm_source=chatgpt.com)
*   **NaCl**: encoding-phase eviction framework; reports up to **50% KV reduction** while keeping over **95%** performance. [arXiv](https://arxiv.org/abs/2408.03675?utm_source=chatgpt.com)
*   **KIVI**: **2-bit** asymmetric KV quantization; reports **2.6× less peak memory**, up to **4× larger batch size**, and **2.35–3.47× throughput** gains. [arXiv](https://arxiv.org/abs/2402.02750)
*   **KVQuant**: low-bit KV quantization with custom kernels; reports **<0.1 perplexity degradation** at 3-bit, up to **1M context on one A100-80GB**, and up to **~1.7× speedups**. [arXiv+1](https://arxiv.org/abs/2401.18079)
*   **MagicPIG**: LSH-based sampling / approximate attention; reports up to **5× decoding throughput** and **54 ms decoding latency** on a single RTX 4090 for Llama-3.1-8B at 96K context. [arXiv](https://arxiv.org/abs/2410.16179?utm_source=chatgpt.com)
*   **SCBench**: the benchmark paper that keeps you honest; it evaluates **generation, compression, retrieval, and loading** across shared-context multi-request settings, not just one-shot toy runs. [arXiv](https://arxiv.org/html/2412.10319v2)
*   **SCOPE**: useful for long-output reasoning; argues that over-compressing during **prefill** hurts reasoning and proposes different handling for prefill vs decode. [ACL Anthology+1](https://aclanthology.org/2025.acl-long.529/?utm_source=chatgpt.com)

**3\. Prompt/context reduction papers third.** These are often cheaper wins than fancy KV surgery.

*   **Selective Context**: prunes redundant input text; reports **50% context-cost reduction**, **36% less inference memory**, and **32% less inference time** with small quality loss. [arXiv](https://arxiv.org/abs/2310.06201)
*   **LLMLingua**: prompt compression with reported **up to 20× compression**. [arXiv](https://arxiv.org/abs/2310.05736?utm_source=chatgpt.com)
*   **LongLLMLingua**: for long prompts specifically; reports up to **21.4% better performance** on NaturalQuestions with about **4× fewer tokens**, **94.0% cost reduction** on LooGLE, and **1.4–2.6× latency speedup** on ~10K-token prompts. [arXiv](https://arxiv.org/abs/2310.06839)
*   **Prompt Cache**: precomputes and reuses attention states for overlapping prompt modules; reports **8× TTFT reduction on GPU** and **60× on CPU** for long overlapping prompts. [arXiv](https://arxiv.org/abs/2311.04934)

My blunt take for your stack: **read KVCIS, but don’t start there**. For a 4B–9B fleet with repeated harness prefixes and short outputs, the first levers are usually **KV/prefix reuse**, **prompt/module caching**, **chunked prefill or prefill/decode separation**, and **prompt compression**. Then measure whether KV memory is still the choke point; only after that would I spend real effort on **KIVI/KVQuant/SnapKV/NaCl/KVCIS**. [arXiv+5arXiv+5arXiv+5](https://arxiv.org/abs/2309.06180)

If you want the shortest possible shortlist, it’s this: **PagedAttention, SGLang, Sarathi-Serve, DistServe, KIVI, KVQuant, SnapKV, SCBench, LongLLMLingua, Prompt Cache, KVCIS**.

---

**Sources:**

- [KVCIS: Activation-Based Token Importance Prediction for Intelligent KV-Cache Compression](https://research.google/pubs/kvcis-activation-based-token-importance-prediction-for-intelligent-kv-cache-compression-2/)
- [[2309.06180] Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180)
- [Optimizing Key-Value Cache Compression in Long-context ...](https://aclanthology.org/2025.acl-long.529/?utm_source=chatgpt.com)



---
Powered by [ChatGPT Exporter](https://www.chatgptexporter.com)