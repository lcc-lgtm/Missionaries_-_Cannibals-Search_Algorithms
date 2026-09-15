# Missionaries and Cannibals — Search Algorithms

Python implementations of classic AI search algorithms solving the
**Missionaries and Cannibals** problem: get 3 missionaries and 3 cannibals
across a river using a 2-person boat, without ever letting cannibals
outnumber missionaries on either bank.

## Algorithms

| File | Algorithm | Type |
|---|---|---|
| `ids_solver_a.py` / `ids_solver_b.py` | Iterative Deepening Search (IDS) | Uninformed |
| `astar_solver_a.py` / `astar_solver_b.py` | A* Search | Informed (heuristic) |

## State Representation

Each state is a tuple `(M_left, C_left, boat_pos)`:
- `M_left` — missionaries on the left bank (0–3)
- `C_left` — cannibals on the left bank (0–3)
- `boat_pos` — 1 if boat is on the left bank, 0 if on the right

Goal state: `(0, 0, 0)`

## A* Heuristic

```
h(n) = (M_left + C_left) / 2
```

Admissible and consistent — never overestimates the remaining boat trips needed.

## How to Run

```bash
python ids_solver_a.py
python astar_solver_a.py
```

Each script prompts for a starting state (M, C, boat position), runs the
search, and prints the step-by-step solution along with nodes expanded.

## Example

```
Enter number of Missionaries on Left Bank (0-3): 3
Enter number of Cannibals on Left Bank (0-3): 3
Enter Boat position (1 for Left, 0 for Right): 1

-> Success! Nodes Expanded: 15 | Total Moves: 11
```

## Background

This project was built for a university AI course to compare uninformed
vs. informed search strategies on completeness, cost-optimality, time
complexity, and space complexity.

## License

MIT
