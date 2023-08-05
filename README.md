# Draft Lottery Simulator

The Draft Lottery Simulator models a NBA-style draft lottery targeted at fantasy football leagues. Each player in the league ranks their preferred draft picks and is assigned odds for receiving the first chance of selecting their pick. A player is randomly chosen according to this probability distribution, and their highest ranked pick that remains is assigned. By running a Monte Carlo simulation of this process, this program generates the chances each player has of receiving a certain draft pick.

## Requirements

* Python 3.11 or later

## Usage

To get started, download the files in this repository and run 

```
pip install -r requirements.txt
```

to install dependencies.

Create a `config.toml` file in the same directory as `simulate.py`. The config file should adhere to the following format:

```
[SIMULATION]
NUM_SIMULATIONS = <int>

[ODDS]
PLAYER_1 = <float>
PLAYER_2 = <float>
...
PLAYER_N = <float>

[PREFERENCES]
PLAYER_1 = permutation([1, 2, ..., N])
PLAYER_2 = permutation([1, 2, ..., N])
...
PLAYER_N = permutation([1, 2, ..., N])
```

After defining the configuration, run `python simulate.py` to output a grid of players and draft order probabilities. To save the table to a file, for example, run `python simulate.py > output.txt`.
