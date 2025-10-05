# pr4.py - FCFS scheduling for given processes

def fcfs(processes, arrivals=None):
    n = len(processes)
    if arrivals is None:
        arrivals = [0] * n

    current_time = 0
    waiting = []
    turnaround = []
    completion = []

    for (name, burst), arrival in zip(processes, arrivals):
        if current_time < arrival:
            current_time = arrival  # CPU idle until process arrives
        wait = current_time - arrival
        current_time += burst
        comp = current_time
        tat = comp - arrival

        waiting.append(wait)
        completion.append(comp)
        turnaround.append(tat)

        print(f"{name:>3}  Burst={burst:>3}  Arrival={arrival:>3}  Waiting={wait:>3}  Turnaround={tat:>3}  Completion={comp:>3}")

    avg_wait = sum(waiting) / n
    avg_tat = sum(turnaround) / n
    print(f"\nAverage waiting time   = {avg_wait:.2f}")
    print(f"Average turnaround time= {avg_tat:.2f}")

if __name__ == "__main__":
    processes = [("P1", 21), ("P2", 6), ("P3", 3), ("P4", 2)]
    # All arrival times are 0 as per problem statement
    arrivals = [0, 0, 0, 0]
    fcfs(processes, arrivals)