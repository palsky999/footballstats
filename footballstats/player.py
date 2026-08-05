"""
player.py
---------
Defines the Player class for tracking an individual player's stats.
"""

from .stats import goals_per_match


class Player:
    """Represents a football player and their season/career stats."""

    def __init__(self, name: str, goals: int = 0, assists: int = 0, matches: int = 0):
        self.name = name
        self.goals = goals
        self.assists = assists
        self.matches = matches

    def goals_per_match(self) -> float:
        """Average goals scored per match."""
        return goals_per_match(self.goals, self.matches)

    def goal_involvements(self) -> int:
        """Total goals + assists (a common attacking-contribution stat)."""
        return self.goals + self.assists

    def involvements_per_match(self) -> float:
        """Average goal involvements (goals + assists) per match."""
        if self.matches <= 0:
            return 0.0
        return round(self.goal_involvements() / self.matches, 2)

    def add_match(self, goals: int = 0, assists: int = 0):
        """Record stats from a new match played."""
        self.goals += goals
        self.assists += assists
        self.matches += 1

    def __repr__(self):
        return (
            f"Player(name={self.name!r}, goals={self.goals}, "
            f"assists={self.assists}, matches={self.matches})"
        )

    def __str__(self):
        return (
            f"{self.name}: {self.goals}G {self.assists}A in {self.matches} matches "
            f"({self.goals_per_match()} goals/match)"
        )
