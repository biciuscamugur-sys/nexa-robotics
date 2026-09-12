"""Basic safety invariant checks for NEXA."""

from dataclasses import dataclass


@dataclass(frozen=True)
class SafetyState:
    speed: float
    battery: float
    obstacle_distance: float


def check_safety(state: SafetyState) -> bool:
    """Return True when the robot state satisfies basic safety limits."""
    return (
        0.0 <= state.speed <= 2.0
        and 0.0 <= state.battery <= 100.0
        and state.obstacle_distance >= 0.5
    )
