# Visual and perceptual verification: detecting small meaningful defects

## A feature-sized contract

A full-frame similarity average can conceal a missing two-pixel seam, one-pixel icon, short flicker, invisible outline or wrong resource digit. Every high-risk visual capability needs a named observable witness: target object/region, camera/pose, scale, lighting/time, expected state, interval, render profile, mask policy, spatial/temporal tolerance, and meaningful unacceptable defects.

Track final frame pixels and, where available, semantic scene state and read-only diagnostic buffers. A visible target needs existence, position/visibility, appearance and temporal behavior tests, not just 'component is present'. A camera may deliberately expose the target during fixture setup; do not retarget it after a defect disappears from view to manufacture a passing shot.

## Two capture profiles, both necessary

**Controlled regression** pins seed/checkpoint, resolution/DPI, fonts, content, camera, driver/engine/profile and bounded warm-up. It may remove approved noisy effects to isolate an algorithm or layout property.

**Representative player profile** retains the actual shipping anti-aliasing, animation, motion blur, LOD, lighting, dynamic resolution, audio and presentation path relevant to the promise. It tests the same feature under motion, overlap, extreme content and supported resource pressure. Turning off the feature to stabilize a screenshot cannot certify that feature.

Baseline compatibility is keyed to the complete render profile. A changed engine/driver or product design invalidates or segments a baseline; workers do not automatically accept a new screenshot when the old one fails. Empty baseline/capture sets produce NOT_ASSESSED or blocked acceptance, not success.

## Complementary methods

| Method | Best use | Limitation |
|---|---|---|
| Exact/pixel threshold | Stable text, icons and controlled renders | Brittle across uncontrolled rendering environments |
| ROI/edge/shape checks | Small seams, outlines, alignment, clipping, object silhouettes | Regions, masks and alignment require independent review |
| Perceptual similarity | Broader structural changes and noisy images | Global averages can hide tiny critical failures |
| Semantic/accessibility checks | Labels, focus, state, visibility semantics | A correct tree does not prove visible pixels |
| Depth/normal/object-ID buffers | Diagnose occlusion, geometry, material and picking issues | Internal buffer success does not prove final composition |
| Temporal windows | Flicker, TAA trails, LOD popping, animation stalls, response timing | Needs frame identity and sufficient sampling |
| Calibrated vision model | Interpreted layout/style/readability and unfamiliar defect triage | Fallible, prompt-sensitive and unsuitable as sole critical oracle |
| Audio signal/listening checks | Silence, clipping, sync, missing cues, glitches | File presence and decoded duration do not prove perceptual quality |

Use bounded high-resolution crops in addition to full-context frames. Never enlarge a downscaled thumbnail and call it recovered pixel detail. Preserve original frames and lossless analysis derivatives; marketing video compression is a different output. Color checks must record transfer function, primaries, range, bit depth and tone mapping. An SDR screenshot cannot prove full HDR panel behavior.

## Calibration and adversarial controls

Build a known-good/known-bad corpus per feature class. Seed a missing mesh, clipped label, wrong biome sample, disabled tooltip, tiny seam, flipped normal, hidden required icon, short flicker, stale frame, silent audio and nonfunctional input handler. Measure detector false acceptance and false rejection per class, not only a pooled score. Keep holdout cases separate from the development loop and retain all failed attempts.

For model-assisted judgments bind the model/version, rubric/prompt digest, actual image/clip payload digests, crop context and response. Reject fabricated screenshot paths, malformed output and confident narrative unsupported by captured media. Captured UI and logs can contain prompt injection; treat them as untrusted evidence. Do not allow a model's self-declared confidence to become a mathematical probability or a new permission.

Independent detectors can still have correlated blind spots. Disagreement is a finding, not an invitation to choose the most favorable result. Use analyst/operator sampling and adjudication for disputed perceptual claims; broad claims of fun, taste, accessibility or universal quality cannot be proven by one image model. The machine can produce useful repeatable proxy grades when their limits and calibration are explicit.

## Product witnesses

Civis: placement ghost, selection, minimap indicator, terrain/water change, character animation, menu/HUD layering, camera transition and save/reopen continuity in the real game. Preserve subsystem reproducibility without imposing global determinism.

Dino: a distinctive real pack change, public user-path action, game-state effect and actual changed pixels; test main-menu/gameplay transitions, asset catalog failures and hook lifecycle.

WorldSphereMod: full camera orbit, seam/pole behavior, terrain coloring, LOD transitions, depth/collision/picking, animated actors and supported effects in the actual host game. A world coordinate may be correct while a projected surface is visibly wrong.

CivicWarfare: actual installed mod HUD, onboarding, combat/economy loop, visual feedback, save/reload, compatibility and clean disable under the supported host-game profile.

All other GUIs: design states, focus/navigation, accessibility, loading/empty/error/recovery paths and real content. CLI-only subjects use transcript/PTY assertions, machine-output contracts and VHS demonstrations rather than invented GUIs.
