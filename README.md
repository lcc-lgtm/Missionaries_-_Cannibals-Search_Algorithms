# Missionaries and Cannibals — Search Algorithms

Python implementations of classic AI search algorithms solving the
**Missionaries and Cannibals** problem: get 3 missionaries and 3 cannibals
across a river using a 2-person boat, without ever letting cannibals
outnumber missionaries on either bank.

## Purpose

This project compares how different families of search algorithms behave on the
same problem: uninformed search (BFS, DFS, IDS), informed search (A*) and local
search (Simulated Annealing). Every algorithm shares the same state
representation and move-validation logic, so differences in results come from
the search strategy alone.

## Algorithms

| File | Algorithm | Type |
|---|---|---|
| `uninformed_bfs_solution.py` | Breadth-First Search (BFS) | Uninformed |
| `uninformed_dfs_solution.py` | Depth-First Search (DFS) | Uninformed |
| `uninformed_IDS_solution.py` | Iterative Deepening Search (IDS) | Uninformed |
| `informed_Astar_solution.py` | A* Search | Informed |
| `informed_heuristic_local_sa_solution.py` | Simulated Annealing (SA) | Local search |
| `compare.py` | Runs all five on the same start state and prints a comparison table | - |

## State Representation

Each state is a tuple `(M_left, C_left, boat_pos)`:
- `M_left` — missionaries on the left bank (0–3)
- `C_left` — cannibals on the left bank (0–3)
- `boat_pos` — 1 if boat is on the left bank, 0 if on the right

Goal state: `(0, 0, 0)`

## Constraint Validation

`is_valid` rejects any state where the counts go negative, or where cannibals
outnumber missionaries (while at least one missionary is present) on either
bank. `get_successors` only returns moves that pass this check, so every path
found is safe by construction.

## How to Run

Each file is an interactive program. Run it and enter the start state when prompted:

```
python uninformed_bfs_solution.py
python compare.py
```

Input: missionaries on the left bank (0-3), cannibals on the left bank (0-3),
boat position (1 = left, 0 = right). Use `3, 3, 1` for the classic problem.

## Sample Comparison (start state `(3, 3, 1)`)

| Algorithm | Result | Moves | Nodes Expanded |
|---|---|---|---|
| BFS | Solved | 11 | 15 |
| DFS | Solved | 11 | 12 |
| IDS | Solved | 11 | 151 |
| A* | Solved | 11 | 15 |
| Simulated Annealing | 48/100 runs solved | 49.3 (avg) | 96.1 steps (avg) |

Notes:
- BFS, A* and IDS return the shortest solution. DFS is not guaranteed to be optimal; it happens to be here.
- IDS counts every re-expansion across all depth limits, so its node count is higher.
- Simulated Annealing is random and not guaranteed to succeed. It can get trapped in local minima, so `compare.py` runs it 100 times and reports the success rate. Exact SA numbers vary between runs.
