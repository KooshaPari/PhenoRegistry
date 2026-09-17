# Canonical design state and executable mockups

## Design is first-class state, not disposable chat output

Keep inspectable design decisions beside the product model, not solely in screenshots pasted into agent chats. The user should be able to inspect the current intended experience, alternatives and rejected options before and during implementation. An accepted design constrains work; it is not proof that the running implementation conforms.

Each design record links: human source and interpretation; user job/capability; required states and transitions; data fixtures; interface/interaction constraints; architecture assumptions; editable source and rendered previews; provenance/licensing; review state and exact version; implementation paths; acceptance scenarios; and actual resulting captures. Use subject-local source with reconciled Tracera entities rather than a hardcoded universal design database in a tool.

## Representations by purpose

| Representation | Appropriate use |
|---|---|
| ASCII/text sketch | Fast CLI layout, command transcript, flow and state discussion |
| SVG/Figma/Penpot/vector/raster | Editable screen composition, alternatives, typography and assets |
| Story/component fixture | Real interactive control behavior and state variants |
| Clickable prototype | Navigation and workflow validation before backend completion |
| Scene/blockout | Camera, spatial interaction, environment, character scale and lighting |
| Motion/audio specimen | Timing, transition, feedback, pacing and sound behavior |
| API/schema/state model | Nonvisual workflows, event ordering, data and error contracts |
| Runtime capture | Actual implementation evidence, never a substitute for the design's source |

Choose the smallest useful fidelity; do not force Figma on an engine scene or a 3D prototype on a CLI. Reuse qualified shared tokens, components, generators and sources. Adobe/Blender/native tools are used where available and properly licensed. Font binaries and restricted third-party assets are not redistributed by default.

## State coverage

For each applicable surface model default, empty, loading, partial, populated, success, error, denied, offline, reconnecting and recovery states. Include long/localized content, keyboard/IME, focus, accessibility, DPI/window sizes, themes and reduced motion where supported. Capture relationships rather than an unbounded Cartesian screenshot explosion; critical variants remain explicit.

For games, include build/inspect/command/possession modes, overlays, population scale, camera regimes and unattended-world return. A static landing-style mockup is not a gameplay interaction specification.

## Lifecycle and creative freedom

Exploratory -> proposed -> reviewed -> accepted-for-scope -> implemented-candidate -> behavior-validated -> superseded. 'Reviewed' names actual feedback; 'accepted' needs scoped authority and version, not an agent changing a status file. Creative alternatives may coexist. Branch experiments are not defects merely because they differ from the accepted design.

User approval may be asynchronous. Agents can make reversible provisional proposals while waiting, but must not label them approved. Freeze only what is needed for the current slice; keep explicit design degrees of freedom so creative work is not reduced to pixel tracing.

## Baselines and change control

Maintain a design baseline (intended outcome) and a runtime regression baseline (observed qualified artifact). A regression screenshot can preserve a bug; a mockup can portray an impossible or unfinished capability. Qualification checks both design intent and runtime contract.

Changing a failed baseline requires a legitimate design/compatibility decision, not just a new screenshot. Record impact on downstream consumers, shared tokens, documentation, journeys and grading scope. Changes to a shared component must re-evaluate affected hosts, not only the original app.

## First slice

Choose one current user journey. Publish its editable flow plus fixture-backed states and proposed interactions. Bind the accepted version when approval exists. Implement one path, capture the actual result through the bridge, compare the result with relevant design and behavioral contracts, record dissatisfaction, and iterate. The design tools/records remain usable before the complete Tracera UI exists.
