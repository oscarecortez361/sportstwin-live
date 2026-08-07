# SportsTwin Live Architecture

## Goal

Treat the sports room as a digital twin whose virtual state mirrors display assignments, active streams, game priorities, and reaction modes.

## Main layers

1. **Sports data layer** — schedules, scores, game state, and final results.
2. **Priority engine** — decides which games deserve which displays.
3. **Room twin** — tracks the current state of each TV and the command hub.
4. **Reaction engine** — converts game outcomes into room behaviors.
5. **Automation layer** — future control of displays, audio, and lighting.

## Event flow

```text
sports event -> classify event -> update room twin -> choose reaction -> send display/audio/lighting actions
```

## Design rule

Manual override should always remain available. Automation should make game day easier, not trap the room in a bad layout when the user wants something different.

## Public assets

The repository should use original, licensed, or user-supplied artwork. Meme-inspired reactions can be supported through local custom asset paths without bundling copyrighted images into the public project.
