# SportsTwin Live

SportsTwin Live is a personal digital-twin project for a multi-TV sports room. It combines live sports data, stream assignment, room-state logic, and event-driven reactions so the physical viewing setup can respond automatically to what is happening in games.

## Concept

```text
Live Sports Data
       |
       v
Outcome / Event Detection
       |
       v
Reaction Engine
       |
       +--> TV layout
       +--> Graphics / overlays
       +--> Audio cues
       +--> Lighting scenes
       +--> Celebration / heartbreak modes
```

## Real-world setup

The project is designed around a home sports room with multiple TVs and a mini PC acting as the command hub. The system can eventually coordinate different streaming sources across displays and use multiview layouts where supported.

## Planned features

- Game schedule and live-score ingestion
- Automatic assignment of games to displays
- Priority rules for favorite teams, playoffs, title fights, and major events
- Multi-screen layout presets
- Manual override dashboard
- Event-driven win/loss reactions
- Room-state logging for digital-twin visualization

## Reaction Engine

The fun part: game outcomes can trigger different room modes.

- **Win mode:** celebration graphics, confetti-style animation, upbeat audio cue, brighter room scene
- **Loss mode:** intentionally dramatic heartbreak graphic, muted/darker scene, sad audio cue
- **Rival loss mode:** optional petty celebration mode
- **Championship mode:** full-room takeover across every available display

For the public repository, reaction artwork should be original or user-supplied rather than bundling copyrighted meme assets. The engine can still support local custom images.

## Repository structure

```text
.
├── README.md
├── config/
│   └── room_config.json
├── docs/
│   └── ARCHITECTURE.md
└── src/
    └── reaction_engine.py
```

## Run the starter reaction engine

```bash
python src/reaction_engine.py
```

## Roadmap

1. Room configuration and reaction engine
2. Live sports data adapter
3. Display assignment logic
4. Dashboard running on the mini PC
5. Stream-launch integration
6. Lighting and audio automation
7. Full digital-twin room view

## Status

**Active personal prototype.** The current version starts with event logic and room-state simulation before controlling real displays or smart-home devices.

## Author

Oscar Cortez  
AI and Robotics Engineering
