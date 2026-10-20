import time

from uninformed_bfs_solution import bfs, is_valid
from uninformed_dfs_solution import dfs
from uninformed_IDS_solution import ids
from informed_Astar_solution import a_star
from informed_heuristic_local_sa_solution import simulated_annealing

SA_TRIALS = 100  # SA is random & it runs many times, so the results are averaged

def run_search(func, start_state):
    """ Runs one deterministic search and returns (path, nodes_expanded, time_in_ms) """
    start_time = time.perf_counter()
    path, nodes = func(start_state)
    elapsed = (time.perf_counter() - start_time) * 1000
    return path, nodes, elapsed

def run_sa_trials(start_state):
    """ Runs SA many times and returns (successes, avg_moves, avg_steps, avg_time_in_ms) """
    successes, total_moves, total_steps = 0, 0, 0
    start_time = time.perf_counter()

    for _ in range(SA_TRIALS):
        path, steps, success = simulated_annealing(start_state)
        total_steps += steps
        if success:
            successes += 1
            total_moves += len(path) - 1

    avg_time = (time.perf_counter() - start_time) * 1000 / SA_TRIALS
    avg_moves = total_moves / successes if successes else None
    return successes, avg_moves, total_steps / SA_TRIALS, avg_time

def print_row(name, result, moves, nodes, time_ms):
    print(f"  {name:<24}| {result:<14}| {moves:<8}| {nodes:<10}| {time_ms:<10}")

def print_comparison(start_state):
    header = f"  {'Algorithm':<24}| {'Result':<14}| {'Moves':<8}| {'Nodes':<10}| {'Time (ms)':<10}"
    print(header)
    print("  " + "-"*(len(header)-2))

    shortest = None
    deterministic = [("Breadth-First Search", bfs), ("Depth-First Search", dfs),
                     ("Iterative Deepening", ids), ("A* Search", a_star)]

    for name, func in deterministic:
        path, nodes, elapsed = run_search(func, start_state)
        if path:
            if name == "Breadth-First Search": shortest = len(path) - 1  # BFS is optimal, used as reference
            print_row(name, "Solved", len(path)-1, nodes, f"{elapsed:.3f}")
        else:
            print_row(name, "No Solution", "-", nodes, f"{elapsed:.3f}")

    successes, avg_moves, avg_steps, avg_time = run_sa_trials(start_state)
    moves_text = f"{avg_moves:.1f}" if avg_moves is not None else "-"
    print_row("Simulated Annealing*", f"{successes}/{SA_TRIALS} solved", moves_text, f"{avg_steps:.1f}", f"{avg_time:.3f}")

    print("\n  Notes:")
    print("  - Nodes = nodes expanded (IDS counts every re-expansion across all depth limits).")
    print(f"  - * SA is random: Moves = average over solved runs, Nodes = average steps taken over {SA_TRIALS} runs.")
    if shortest is not None:
        print(f"  - Shortest solution (BFS) = {shortest} moves. Any algorithm with more moves is not optimal.")

def run_experiment():
    print("="*70 + "\n  ALGORITHM COMPARISON (BFS vs DFS vs IDS vs A* vs SA)\n" + "="*70)
    
    while True:
        try:
            print("\n--- Enter Manual Test Data ---")
            m = int(input("Enter number of Missionaries on Left Bank (0-3): "))
            c = int(input("Enter number of Cannibals on Left Bank (0-3): "))
            b = int(input("Enter Boat position (1 for Left, 0 for Right): "))
            
            if m < 0 or m > 3 or c < 0 or c > 3 or b not in [0, 1]:
                print("[!] Invalid input. Please follow the range rules.")
                continue
                
            start_state = (m, c, b)
            
            if not is_valid(start_state):
                print("[!] Warning: This start state is unsafe/invalid.")
                
            print(f"\nEvaluating Start: {start_state} -> Goal: (0, 0, 0)\n")
            print_comparison(start_state)
                
            print("\nOptions:")
            print("1 - Continue to test another data")
            print("2 - Exit the program")
            choice = input("Enter your choice (1 or 2): ")
            
            if choice == '2':
                print("Exiting program...")
                break
            elif choice != '1':
                print("Invalid choice detected. Exiting program by default...")
                break
                
        except ValueError:
            print("[!] Invalid input format. Please enter integers only.")

if __name__ == "__main__":
    run_experiment()
