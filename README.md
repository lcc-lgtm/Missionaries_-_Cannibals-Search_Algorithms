# Missionaries and Cannibals — Search Algorithms

Python implementations of classic AI search algorithms solving the
**Missionaries and Cannibals** problem: get 3 missionaries and 3 cannibals
across a river using a 2-person boat, without ever letting cannibals
outnumber missionaries on either bank.

## Algorithms

| File | Algorithm | Type |
|---|---|---|
| `uninformed_bfs.py` | Breadth-First Search (BFS) | Uninformed[cite: 3] |
| `uninformed_ids.py` | Iterative Deepening Search (IDS) | Uninformed[cite: 2] |
| `informed_astar.py` | A* Search | Informed (heuristic)[cite: 1] |
| `informed_sa.py` | Simulated Annealing (SA) | Local Search[cite: 4] |

## State Representation

Each state is a tuple `(M_left, C_left, boat_pos)`:
- `M_left` — missionaries on the left bank (0–3)
- `C_left` — cannibals on the left bank (0–3)
- `boat_pos` — 1 if boat is on the left bank, 0 if on the right

Goal state: `(0, 0, 0)`

## A* Heuristic
