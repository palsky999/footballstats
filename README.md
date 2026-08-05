# footballstats

A small Python library for calculating football (soccer) statistics —
built as a learning project for packaging, testing, and publishing a
Python library to GitHub.

## Features

- `Player` class — track goals, assists, matches, goals/match, goal involvements
- `Team` class — track match results, win %, points per game, goal difference, top scorer
- Stand-alone stat functions in `footballstats.stats` you can use without the classes

## Installation (local / editable install)

```bash
git clone https://github.com/<your-username>/footballstats.git
cd footballstats
pip install -e .
```

## Usage

```python
from footballstats import Player, Team

# Player example
messi = Player("Lionel Messi", goals=20, assists=15, matches=25)
print(messi)
print(messi.goals_per_match())        # 0.8
print(messi.involvements_per_match()) # 1.4

# Team example
team = Team("Accra Hearts")
team.add_result(2, 1)  # win
team.add_result(1, 1)  # draw
team.add_result(0, 2)  # loss
team.add_player(messi)

print(team)
print(team.win_percentage())
print(team.points_per_game())
print(team.top_scorer())
```

## Running tests

```bash
python -m unittest discover tests
```

## Project structure

```
footballstats/
├── footballstats/
│   ├── __init__.py
│   ├── player.py
│   ├── team.py
│   └── stats.py
├── tests/
│   └── test_stats.py
├── pyproject.toml
├── README.md
└── .gitignore
```

## License

MIT
