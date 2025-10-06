#include <stdio.h>
int main() {
    int n = 4;
    int burst_time[] = {21, 6, 3, 2};
    int waiting_time[n], turnaround_time[n];
    int total_waiting = 0, total_turnaround = 0;
    waiting_time[0] = 0;
    for (int i = 1; i < n; i++) {
        waiting_time[i] = waiting_time[i - 1] + burst_time[i - 1];
    }
    for (int i = 0; i < n; i++) {
        turnaround_time[i] = waiting_time[i] + burst_time[i];
        total_waiting += waiting_time[i];
        total_turnaround += turnaround_time[i];
    }
    printf("Process\tBurst\tWaiting\tTurnaround\n");
    for (int i = 0; i < n; i++) {
        printf("P%d\t%d\t%d\t%d\n", i + 1, burst_time[i], waiting_time[i], turnaround_time[i]);
    }
    float avg_waiting = (float)total_waiting / n;
    float avg_turnaround = (float)total_turnaround / n;
    printf("\nAverage Waiting Time: %.2f\n", avg_waiting);
    printf("Average Turnaround Time: %.2f\n", avg_turnaround);
    return 0;
}