"""
team.py
-------
Defines the Team class for tracking a team's season results and stats,
and for holding a roster of Player objects.
"""

from .stats import win_percentage, points_per_game, goal_difference


class Team:
    """Represents a football team and its season record."""

    def __init__(self, name: str):
        self.name = name
        self.wins = 0
        self.draws = 0
        self.losses = 0
        self.goals_for = 0
        self.goals_against = 0
        self.players = []

    @property
    def matches(self) -> int:
        return self.wins + self.draws + self.losses

    def add_result(self, goals_for: int, goals_against: int):
        """Record the result of one match by scoreline."""
        self.goals_for += goals_for
        self.goals_against += goals_against

        if goals_for > goals_against:
            self.wins += 1
        elif goals_for == goals_against:
            self.draws += 1
        else:
            self.losses += 1

    def add_player(self, player):
        """Add a Player object to this team's roster."""
        self.players.append(player)

    def win_percentage(self) -> float:
        return win_percentage(self.wins, self.matches)

    def points_per_game(self) -> float:
        return points_per_game(self.wins, self.draws, self.matches)

    def goal_difference(self) -> int:
        return goal_difference(self.goals_for, self.goals_against)

    def total_points(self) -> int:
        return (self.wins * 3) + (self.draws * 1)

    def top_scorer(self):
        """Return the Player with the most goals on the roster, or None."""
        if not self.players:
            return None
        return max(self.players, key=lambda p: p.goals)

    def __repr__(self):
        return f"Team(name={self.name!r}, W{self.wins}-D{self.draws}-L{self.losses})"

    def __str__(self):
        return (
            f"{self.name}: {self.matches} played, {self.total_points()} pts, "
            f"GD {self.goal_difference():+d}"
        )
