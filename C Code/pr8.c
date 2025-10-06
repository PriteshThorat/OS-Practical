from typing import List, Tuple

#!/usr/bin/env python3
"""
pr8.py

Banker's Algorithm for deadlock avoidance.
Usage:
- Follow prompts to enter number of processes and resource types.
- Enter Allocation and Max matrices row by row (space-separated).
- Enter Available vector.
- Program prints if the system is currently in a safe state and a safe sequence (if any).
- Optional: try a resource request for a process to see if it would be granted.
"""


def compute_need(max_mat: List[List[int]], alloc: List[List[int]]) -> List[List[int]]:
    return [[m - a for m, a in zip(max_row, alloc_row)]
            for max_row, alloc_row in zip(max_mat, alloc)]

def is_safe(alloc: List[List[int]], max_mat: List[List[int]], avail: List[int]) -> Tuple[bool, List[int]]:
    n = len(alloc)
    m = len(avail)
    need = compute_need(max_mat, alloc)
    work = avail.copy()
    finish = [False] * n
    safe_seq = []

    changed = True
    while changed:
        changed = False
        for i in range(n):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(m)):
                # can satisfy process i
                for j in range(m):
                    work[j] += alloc[i][j]
                finish[i] = True
                safe_seq.append(i)
                changed = True

    if all(finish):
        return True, safe_seq
    return False, []

def request_resources(pi: int, req: List[int], alloc: List[List[int]],
                      max_mat: List[List[int]], avail: List[int]) -> Tuple[bool, str]:
    n = len(alloc)
    m = len(avail)
    if not (0 <= pi < n):
        return False, f"Invalid process index: {pi}"
    need = compute_need(max_mat, alloc)
    # Check request <= need
    if any(req[j] > need[pi][j] for j in range(m)):
        return False, "Error: process has exceeded its maximum claim."
    # Check request <= available
    if any(req[j] > avail[j] for j in range(m)):
        return False, "Resources not available; process must wait."

    # Pretend to allocate
    alloc2 = [row.copy() for row in alloc]
    avail2 = avail.copy()
    for j in range(m):
        avail2[j] -= req[j]
        alloc2[pi][j] += req[j]

    safe, seq = is_safe(alloc2, max_mat, avail2)
    if safe:
        return True, f"Request can be granted. Safe sequence: {seq}"
    else:
        return False, "Request would lead to unsafe state; deny."

def read_matrix(rows: int, cols: int, name: str) -> List[List[int]]:
    print(f"Enter {name} matrix ({rows} rows, {cols} columns), rows as space-separated integers:")
    mat = []
    for i in range(rows):
        while True:
            line = input(f"Row {i}: ").strip()
            parts = line.split()
            if len(parts) != cols:
                print(f"Expected {cols} values, got {len(parts)}. Try again.")
                continue
            try:
                row = [int(x) for x in parts]
            except ValueError:
                print("Invalid integers. Try again.")
                continue
            mat.append(row)
            break
    return mat

def read_vector(size: int, name: str) -> List[int]:
    while True:
        line = input(f"Enter {name} vector ({size} values, space-separated): ").strip()
        parts = line.split()
        if len(parts) != size:
            print(f"Expected {size} values, got {len(parts)}. Try again.")
            continue
        try:
            vec = [int(x) for x in parts]
            return vec
        except ValueError:
            print("Invalid integers. Try again.")

def main():
    try:
        n = int(input("Number of processes: ").strip())
        m = int(input("Number of resource types: ").strip())
    except ValueError:
        print("Invalid integer input. Exiting.")
        return

    alloc = read_matrix(n, m, "Allocation")
    max_mat = read_matrix(n, m, "Max")
    avail = read_vector(m, "Available")

    safe, seq = is_safe(alloc, max_mat, avail)
    if safe:
        print("System is in a SAFE state.")
        print("Safe sequence:", seq)
    else:
        print("System is in an UNSAFE state (no safe sequence).")

    while True:
        ans = input("Do you want to try a resource request? (y/n): ").strip().lower()
        if ans == 'n':
            break
        if ans != 'y':
            continue
        try:
            pi = int(input(f"Process index (0..{n-1}): ").strip())
        except ValueError:
            print("Invalid process index.")
            continue
        req = read_vector(m, "Request")
        ok, msg = request_resources(pi, req, alloc, max_mat, avail)
        print(msg)
        if ok:
            # apply granted request to current state
            for j in range(m):
                avail[j] -= req[j]
                alloc[pi][j] += req[j]

if __name__ == "__main__":
    main()