"""
footballstats
=============

A small Python library for basic football (soccer) statistics and analytics.

Example:
    >>> from footballstats import Player, Team
    >>> messi = Player("Lionel Messi", goals=20, assists=15, matches=25)
    >>> messi.goals_per_match()
    0.8
"""

from .player import Player
from .team import Team
from .stats import (
    goals_per_match,
    win_percentage,
    points_per_game,
    goal_difference,
)

__version__ = "0.1.0"
__all__ = [
    "Player",
    "Team",
    "goals_per_match",
    "win_percentage",
    "points_per_game",
    "goal_difference",
]
