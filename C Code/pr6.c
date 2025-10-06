#include <stdio.h>
int main() {
    int n = 4;
    int process_id[] = {1, 2, 3, 4};
    int burst_time[] = {21, 6, 3, 2};
    int priority[] = {2, 1, 4, 3};  
    int waiting_time[n], turnaround_time[n];
    int total_waiting = 0, total_turnaround = 0;
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (priority[i] > priority[j]) {
                int temp = priority[i];
                priority[i] = priority[j];
                priority[j] = temp;
                temp = burst_time[i];
                burst_time[i] = burst_time[j];
                burst_time[j] = temp;
                temp = process_id[i];
                process_id[i] = process_id[j];
                process_id[j] = temp;
            }
        }
    }
    waiting_time[0] = 0;
    for (int i = 1; i < n; i++) {
        waiting_time[i] = waiting_time[i - 1] + burst_time[i - 1];
    }
    for (int i = 0; i < n; i++) {
        turnaround_time[i] = waiting_time[i] + burst_time[i];
        total_waiting += waiting_time[i];
        total_turnaround += turnaround_time[i];
    }
    printf("Process\tBurst\tPriority\tWaiting\tTurnaround\n");
    for (int i = 0; i < n; i++) {
        printf("P%d\t%d\t%d\t\t%d\t%d\n", process_id[i], burst_time[i], priority[i], waiting_time[i], turnaround_time[i]);
    }
    float avg_waiting = (float)total_waiting / n;
    float avg_turnaround = (float)total_turnaround / n;
    printf("\nAverage Waiting Time: %.2f\n", avg_waiting);
    printf("Average Turnaround Time: %.2f\n", avg_turnaround);
    return 0;
}