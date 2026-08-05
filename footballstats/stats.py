"""
stats.py
--------
Stand-alone functions for common football statistics.
These work on plain numbers, so they can be reused by both
the Player and Team classes (or called directly).
"""


def goals_per_match(goals: int, matches: int) -> float:
    """Return goals scored per match played."""
    if matches <= 0:
        return 0.0
    return round(goals / matches, 2)


def win_percentage(wins: int, matches: int) -> float:
    """Return win rate as a percentage (0-100)."""
    if matches <= 0:
        return 0.0
    return round((wins / matches) * 100, 2)


def points_per_game(wins: int, draws: int, matches: int) -> float:
    """
    Standard football points system: win = 3, draw = 1, loss = 0.
    Returns average points earned per match played.
    """
    if matches <= 0:
        return 0.0
    total_points = (wins * 3) + (draws * 1)
    return round(total_points / matches, 2)


def goal_difference(goals_for: int, goals_against: int) -> int:
    """Return goal difference (GF - GA)."""
    return goals_for - goals_against
