#include <stdio.h>
int main() {
    int n;
    printf("Enter number of processes: ");
    scanf("%d", &n);
    int process_id[n], burst_time[n], arrival_time[n];
    int waiting_time[n], turnaround_time[n], completion_time[n];
    int total_waiting = 0, total_turnaround = 0;
    for (int i = 0; i < n; i++) {
        process_id[i] = i + 1;
        printf("Enter Burst Time for P%d: ", i + 1);
        scanf("%d", &burst_time[i]);
        printf("Enter Arrival Time for P%d: ", i + 1);
        scanf("%d", &arrival_time[i]);
    }
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (arrival_time[i] > arrival_time[j] || 
               (arrival_time[i] == arrival_time[j] && burst_time[i] > burst_time[j])) {
                int temp;

                temp = arrival_time[i];
                arrival_time[i] = arrival_time[j];
                arrival_time[j] = temp;

                temp = burst_time[i];
                burst_time[i] = burst_time[j];
                burst_time[j] = temp;

                temp = process_id[i];
                process_id[i] = process_id[j];
                process_id[j] = temp;
            }
        }
    }
    int current_time = 0;
    for (int i = 0; i < n; i++) {
        if (current_time < arrival_time[i]) {
            current_time = arrival_time[i]; 
        }
        waiting_time[i] = current_time - arrival_time[i];
        current_time += burst_time[i];
        completion_time[i] = current_time;
        turnaround_time[i] = completion_time[i] - arrival_time[i];
        total_waiting += waiting_time[i];
        total_turnaround += turnaround_time[i];
    }
    printf("\nProcess\tAT\tBT\tCT\tWT\tTAT\n");
    for (int i = 0; i < n; i++) {
        printf("P%d\t%d\t%d\t%d\t%d\t%d\n", process_id[i], arrival_time[i], burst_time[i], completion_time[i], waiting_time[i], turnaround_time[i]);
    }
    float avg_waiting = (float)total_waiting / n;
    float avg_turnaround = (float)total_turnaround / n;
    printf("\nAverage Waiting Time: %.2f\n", avg_waiting);
    printf("Average Turnaround Time: %.2f\n", avg_turnaround);
    return 0;
}