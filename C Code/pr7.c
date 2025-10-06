#include <stdio.h>
int main() {
    int n = 4;
    int process_id[] = {1, 2, 3, 4};
    int burst_time[] = {21, 6, 3, 2};
    int remaining_time[4];
    int waiting_time[4] = {0}, turnaround_time[4] = {0};
    int time = 0, quantum = 4;
    for (int i = 0; i < n; i++) {
        remaining_time[i] = burst_time[i];
    }
    int done;
    do {
        done = 1;
        for (int i = 0; i < n; i++) {
            if (remaining_time[i] > 0) {
                done = 0;
                if (remaining_time[i] > quantum) {
                    time += quantum;
                    remaining_time[i] -= quantum;
                } else {
                    time += remaining_time[i];
                    waiting_time[i] = time - burst_time[i];
                    remaining_time[i] = 0;
                }
            }
        }
    } while (!done);
    for (int i = 0; i < n; i++) {
        turnaround_time[i] = waiting_time[i] + burst_time[i];
    }
    printf("Process\tBurst\tWaiting\tTurnaround\n");
    int total_waiting = 0, total_turnaround = 0;
    for (int i = 0; i < n; i++) {
        printf("P%d\t%d\t%d\t%d\n", process_id[i], burst_time[i], waiting_time[i], turnaround_time[i]);
        total_waiting += waiting_time[i];
        total_turnaround += turnaround_time[i];
    }
    float avg_waiting = (float)total_waiting / n;
    float avg_turnaround = (float)total_turnaround / n;
    printf("\nAverage Waiting Time: %.2f\n", avg_waiting);
    printf("Average Turnaround Time: %.2f\n", avg_turnaround);
    return 0;
}