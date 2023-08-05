import os
import sys
import tomllib
from random import choices
from itertools import filterfalse
from tabulate import tabulate


with open(os.path.join(os.path.dirname(__file__), "config.toml"), "rb") as f:
    config = tomllib.load(f)

    try:
        num_simulations = config["SIMULATION"]["NUM_SIMULATIONS"]
        odds = config["ODDS"]
        preferences = config["PREFERENCES"]
    except KeyError:
        print("Please include a valid config.toml")
        sys.exit(1)

managers = list(odds.keys())
probabilities = list(odds.values())
num_teams = len(odds)
picks = { manager: { (pick + 1): 0 for pick in range(num_teams) }
         for manager in managers }

for _ in range(num_simulations):
    simulation_picks = {}

    while len(simulation_picks) < 8:
        manager = choices(managers, weights=probabilities, k=1)[0]

        if manager in simulation_picks:
            continue

        pick = next(filterfalse(
            list(simulation_picks.values()).__contains__,
            preferences[manager]))
        picks[manager][pick] += 1

        simulation_picks[manager] = pick

table = [[m] + [picks[m][k] / num_simulations 
                for k in sorted(picks[m].keys())] for m in managers]
print(tabulate(table, headers=[""] + list(range(1, num_teams + 1))))
