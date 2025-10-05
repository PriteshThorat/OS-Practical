# pr5.py
# Shortest Job First (non-preemptive) CPU Scheduling
# Reads process count and arrival/burst times from user, prints avg waiting & turnaround times.

def sjf_non_preemptive(processes):
    # processes: list of dicts with keys 'pid','arrival','burst'
    n = len(processes)
    # sort by arrival then burst as tiebreaker for determinism
    processes.sort(key=lambda p: (p['arrival'], p['burst'], p['pid']))
    completed = 0
    time = 0
    waiting_times = {}
    turnaround_times = {}
    finished = set()

    while completed < n:
        # select available, unfinished process with smallest burst
        available = [p for p in processes if p['arrival'] <= time and p['pid'] not in finished]
        if not available:
            # no process available now -> jump to next arrival
            time = min(p['arrival'] for p in processes if p['pid'] not in finished)
            available = [p for p in processes if p['arrival'] <= time and p['pid'] not in finished]

        # choose process with smallest burst (tie: earlier arrival then smaller pid)
        chosen = min(available, key=lambda p: (p['burst'], p['arrival'], p['pid']))
        start_time = time
        completion_time = time + chosen['burst']
        waiting = start_time - chosen['arrival']
        turnaround = completion_time - chosen['arrival']

        waiting_times[chosen['pid']] = waiting
        turnaround_times[chosen['pid']] = turnaround

        # mark complete
        finished.add(chosen['pid'])
        completed += 1
        time = completion_time

    avg_wait = sum(waiting_times.values()) / n
    avg_tat = sum(turnaround_times.values()) / n
    return waiting_times, turnaround_times, avg_wait, avg_tat

def main():
    try:
        n = int(input("Enter number of processes: ").strip())
    except Exception:
        print("Invalid number.")
        return

    processes = []
    print("For each process enter arrival time and burst time separated by space (one per line):")
    for i in range(1, n+1):
        while True:
            try:
                line = input(f"P{i}: ").strip()
                parts = line.split()
                if len(parts) != 2:
                    raise ValueError
                arrival = int(parts[0])
                burst = int(parts[1])
                if arrival < 0 or burst <= 0:
                    raise ValueError
                processes.append({'pid': f"P{i}", 'arrival': arrival, 'burst': burst})
                break
            except Exception:
                print("  Invalid input. Enter two integers: arrival (>=0) and burst (>0).")

    waiting, tat, avg_wait, avg_tat = sjf_non_preemptive(processes)

    print("\nPID\tArrival\tBurst\tWaiting\tTurnaround")
    # print in PID order
    for p in sorted(processes, key=lambda x: int(x['pid'][1:])):
        pid = p['pid']
        print(f"{pid}\t{p['arrival']}\t{p['burst']}\t{waiting[pid]}\t{tat[pid]}")

    print(f"\nAverage waiting time: {avg_wait:.2f}")
    print(f"Average turnaround time: {avg_tat:.2f}")

if __name__ == "__main__":
    main()