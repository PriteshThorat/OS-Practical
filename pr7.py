from typing import List, Tuple

# pr7.py
# Round Robin CPU Scheduling - computes waiting times and turnaround times
# Usage (interactive):
#  - Enter number of processes
#  - Enter burst times (space-separated)
#  - Enter time quantum



def round_robin(burst_times: List[int], quantum: int) -> Tuple[List[int], List[int], float, float]:
    n = len(burst_times)
    remaining = burst_times.copy()
    waiting = [0] * n
    time = 0

    # Track when each process finishes to compute waiting time
    finished = [False] * n
    finished_count = 0

    while finished_count < n:
        made_progress = False
        for i in range(n):
            if remaining[i] > 0:
                made_progress = True
                if remaining[i] > quantum:
                    time += quantum
                    remaining[i] -= quantum
                else:
                    time += remaining[i]
                    waiting[i] = time - burst_times[i]
                    remaining[i] = 0
                    finished[i] = True
                    finished_count += 1
        if not made_progress:
            break  # safety

    turnaround = [waiting[i] + burst_times[i] for i in range(n)]
    avg_wait = sum(waiting) / n if n else 0.0
    avg_turnaround = sum(turnaround) / n if n else 0.0
    return waiting, turnaround, avg_wait, avg_turnaround


def _parse_int_list(s: str) -> List[int]:
    return [int(x) for x in s.replace(',', ' ').split() if x.strip()]


def main():
    try:
        n = int(input("Number of processes: ").strip())
        bursts = _parse_int_list(input(f"Enter {n} burst times (space or comma separated): ").strip())
        if len(bursts) != n:
            print("Count of burst times does not match number of processes.")
            return
        q = int(input("Time quantum: ").strip())
    except Exception as e:
        print("Invalid input:", e)
        return

    waiting, turnaround, avg_wait, avg_turnaround = round_robin(bursts, q)

    print("\nPID\tBurst\tWaiting\tTurnaround")
    for i in range(n):
        print(f"P{i+1}\t{bursts[i]}\t{waiting[i]}\t{turnaround[i]}")
    print(f"\nAverage waiting time: {avg_wait:.2f}")
    print(f"Average turnaround time: {avg_turnaround:.2f}")


if __name__ == "__main__":
    main()