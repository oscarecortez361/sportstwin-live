"""Starter event-driven reaction engine for SportsTwin Live."""

from dataclasses import dataclass


@dataclass
class GameResult:
    team: str
    opponent: str
    team_score: int
    opponent_score: int
    is_rival: bool = False
    is_championship: bool = False


def reaction_for(result: GameResult) -> dict:
    won = result.team_score > result.opponent_score

    if won and result.is_championship:
        return {
            "mode": "CHAMPIONSHIP",
            "graphics": "full-room celebration",
            "audio": "victory cue",
            "lighting": "celebration scene",
            "display_action": "take over all available displays",
        }

    if won:
        return {
            "mode": "WIN",
            "graphics": "original celebration reaction",
            "audio": "upbeat cue",
            "lighting": "bright scene",
            "display_action": "show win overlay on primary display",
        }

    if result.is_rival:
        return {
            "mode": "RIVAL_LOSS",
            "graphics": "dramatic rivalry heartbreak reaction",
            "audio": "playful taunt cue",
            "lighting": "rivalry scene",
            "display_action": "show rivalry overlay",
        }

    return {
        "mode": "LOSS",
        "graphics": "original heartbreak reaction",
        "audio": "sad cue",
        "lighting": "dim scene",
        "display_action": "show loss overlay on primary display",
    }


def main() -> None:
    demo = GameResult(
        team="Home Team",
        opponent="Rival Team",
        team_score=27,
        opponent_score=24,
        is_rival=True,
    )

    print("SportsTwin Live Reaction Engine")
    print(reaction_for(demo))


if __name__ == "__main__":
    main()
