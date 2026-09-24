# Reference landscape and alternatives

The platform should model **capability classes**, not encode a fashionable provider list as architecture.

## Provider classes

- Hyperscale IaaS/platform: AWS, GCP, Azure and peers — broad primitives and deep operational controls.
- Developer PaaS/edge: Vercel, Render, Railway, Fly.io, Heroku, Netlify, Cloudflare and peers — narrower abstractions with strong deployment DX.
- VPS/commodity cloud: Hetzner, OVHcloud, DigitalOcean, Vultr/Akamai and peers — simple machines/network/storage with operator-owned higher layers.
- Managed data/backend: Supabase, Neon, PlanetScale, Turso/Aiven and peers — database/backend semantics that cannot be reduced to "a container is running".
- Local/private execution substrates: Podman/WSLC/native/NVMS/Incus and potentially dedicated-host platforms — execution implementations beneath the BytePort provider contract.

The important output of planning is therefore not `provider = X`. It is a capability-qualified plan that states which semantics are native, emulated, approximated or unsupported.

## What to borrow from existing private-cloud systems

Incus is a useful reference because its REST API exposes resources, instances and backups and its configuration includes CPU/memory/IO limits. S076-S077. That supports the v0.3 contract design, but does not establish that Incus should be installed on the user's laptop or desktop.

Dedicated-node private clouds can become optional adapters later. The default personal-device path should stay lighter because those hosts retain interactive, creator, gaming and local-inference duties.

## What to borrow from managed PaaS

The target UX is the good part: repository linkage, build/deploy histories, previews, environment promotion, health, rollback, logs, managed secrets and clear state transitions. The local provider should reproduce the **control experience where the underlying capability exists**, not fake managed durability or HA it does not have.
