#include <stdio.h>
int main() {
    int n, quantum;
    printf("Enter number of processes: ");
    scanf("%d", &n);
    int process_id[n], burst_time[n], arrival_time[n];
    int remaining_time[n], waiting_time[n], turnaround_time[n], completion_time[n];
    int total_waiting = 0, total_turnaround = 0;
    for (int i = 0; i < n; i++) {
        process_id[i] = i + 1;
        printf("Enter Burst Time for P%d: ", i + 1);
        scanf("%d", &burst_time[i]);
        printf("Enter Arrival Time for P%d: ", i + 1);
        scanf("%d", &arrival_time[i]);
        remaining_time[i] = burst_time[i];
        waiting_time[i] = 0;
        turnaround_time[i] = 0;
    }
    printf("Enter Time Quantum: ");
    scanf("%d", &quantum);
    int time = 0, done;
    do {
        done = 1;
        for (int i = 0; i < n; i++) {
            if (remaining_time[i] > 0 && arrival_time[i] <= time) {
                done = 0;
                if (remaining_time[i] > quantum) {
                    time += quantum;
                    remaining_time[i] -= quantum;
                } else {
                    time += remaining_time[i];
                    waiting_time[i] = time - burst_time[i] - arrival_time[i];
                    remaining_time[i] = 0;
                    completion_time[i] = time;
                }
            } else if (arrival_time[i] > time) {
                time++;
            }
        }
    } while (!done);
    for (int i = 0; i < n; i++) {
        turnaround_time[i] = burst_time[i] + waiting_time[i];
        total_waiting += waiting_time[i];
        total_turnaround += turnaround_time[i];
    }
    printf("\nProcess\tAT\tBT\tCT\tWT\tTAT\n");
    for (int i = 0; i < n; i++) {
        printf("P%d\t%d\t%d\t%d\t%d\t%d\n",
               process_id[i], arrival_time[i], burst_time[i],
               completion_time[i], waiting_time[i], turnaround_time[i]);
    }
    float avg_waiting = (float)total_waiting / n;
    float avg_turnaround = (float)total_turnaround / n;
    printf("\nAverage Waiting Time: %.2f\n", avg_waiting);
    printf("Average Turnaround Time: %.2f\n", avg_turnaround);
    return 0;
}