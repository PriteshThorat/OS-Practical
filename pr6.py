#!/usr/bin/env python3
# pr6.py - Non-preemptive Priority CPU Scheduling
# Lower priority number => higher priority

def input_int(prompt, allow_empty=False):
    while True:
        try:
            s = input(prompt)
            if allow_empty and s.strip() == "":
                return None
            return int(s)
        except ValueError:
            print("Please enter an integer.")

def schedule_priority(processes):
    # processes: list of dicts with keys pid, at, bt, pr
    n = len(processes)
    time = 0
    completed = 0
    # initialize
    for p in processes:
        p.update({'start': None, 'finish': None, 'waiting': None, 'turnaround': None, 'done': False})

    while completed < n:
        # collect ready processes
        ready = [p for p in processes if (not p['done']) and p['at'] <= time]
        if not ready:
            # idle until the next arrival
            next_arrival = min(p['at'] for p in processes if not p['done'])
            time = next_arrival
            ready = [p for p in processes if (not p['done']) and p['at'] <= time]
        # choose highest priority (lower number). tie-breaker: earlier arrival then lower pid
        chosen = min(ready, key=lambda p: (p['pr'], p['at'], p['pid']))
        chosen['start'] = time
        chosen['finish'] = time + chosen['bt']
        chosen['waiting'] = chosen['start'] - chosen['at']
        chosen['turnaround'] = chosen['finish'] - chosen['at']
        chosen['done'] = True
        time = chosen['finish']
        completed += 1

    # sort by pid for output clarity
    processes.sort(key=lambda p: p['pid'])
    return processes

def main():
    print("Non-preemptive Priority Scheduling (lower number = higher priority)")
    n = input_int("Number of processes: ")
    processes = []
    for i in range(1, n+1):
        print(f"Process {i}:")
        at = input_int("  Arrival time: ")
        bt = input_int("  Burst time: ")
        pr = input_int("  Priority (integer, lower = higher): ")
        processes.append({'pid': i, 'at': at, 'bt': bt, 'pr': pr})

    scheduled = schedule_priority(processes)

    total_wt = sum(p['waiting'] for p in scheduled)
    total_tat = sum(p['turnaround'] for p in scheduled)
    avg_wt = total_wt / n
    avg_tat = total_tat / n

    print("\nPID\tAT\tBT\tPR\tST\tFT\tWT\tTAT")
    for p in scheduled:
        print(f"{p['pid']}\t{p['at']}\t{p['bt']}\t{p['pr']}\t{p['start']}\t{p['finish']}\t{p['waiting']}\t{p['turnaround']}")

    print(f"\nAverage Waiting Time    : {avg_wt:.2f}")
    print(f"Average Turnaround Time : {avg_tat:.2f}")

if __name__ == "__main__":
    main()