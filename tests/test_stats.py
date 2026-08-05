"""
Basic tests for footballstats.
Run with:  python -m pytest
(or just:  python -m unittest discover tests)
"""

import unittest
from footballstats import Player, Team
from footballstats.stats import (
    goals_per_match,
    win_percentage,
    points_per_game,
    goal_difference,
)


class TestStatsFunctions(unittest.TestCase):

    def test_goals_per_match(self):
        self.assertEqual(goals_per_match(10, 5), 2.0)
        self.assertEqual(goals_per_match(0, 0), 0.0)

    def test_win_percentage(self):
        self.assertEqual(win_percentage(5, 10), 50.0)
        self.assertEqual(win_percentage(0, 0), 0.0)

    def test_points_per_game(self):
        # 3 wins, 2 draws, 5 matches -> (9 + 2) / 5 = 2.2
        self.assertEqual(points_per_game(3, 2, 5), 2.2)

    def test_goal_difference(self):
        self.assertEqual(goal_difference(10, 4), 6)
        self.assertEqual(goal_difference(2, 5), -3)


class TestPlayer(unittest.TestCase):

    def test_goals_per_match(self):
        p = Player("Test Player", goals=10, assists=5, matches=5)
        self.assertEqual(p.goals_per_match(), 2.0)

    def test_goal_involvements(self):
        p = Player("Test Player", goals=10, assists=5, matches=5)
        self.assertEqual(p.goal_involvements(), 15)
        self.assertEqual(p.involvements_per_match(), 3.0)

    def test_add_match(self):
        p = Player("Test Player")
        p.add_match(goals=2, assists=1)
        p.add_match(goals=1, assists=0)
        self.assertEqual(p.goals, 3)
        self.assertEqual(p.assists, 1)
        self.assertEqual(p.matches, 2)


class TestTeam(unittest.TestCase):

    def test_add_result_and_record(self):
        t = Team("Test FC")
        t.add_result(2, 1)   # win
        t.add_result(1, 1)   # draw
        t.add_result(0, 3)   # loss
        self.assertEqual(t.wins, 1)
        self.assertEqual(t.draws, 1)
        self.assertEqual(t.losses, 1)
        self.assertEqual(t.matches, 3)
        self.assertEqual(t.goal_difference(), -2)
        self.assertEqual(t.total_points(), 4)

    def test_top_scorer(self):
        t = Team("Test FC")
        t.add_player(Player("A", goals=5))
        t.add_player(Player("B", goals=9))
        self.assertEqual(t.top_scorer().name, "B")


if __name__ == "__main__":
    unittest.main()
