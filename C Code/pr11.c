#include <stdio.h>
#define SIZE 16
#define FRAME_SIZE 3
int main() {
    int pages[SIZE] = {0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 4, 5, 6, 7};
    int frames[FRAME_SIZE];
    int time[FRAME_SIZE];
    int faults = 0, hits = 0, counter = 0;
    for (int i = 0; i < FRAME_SIZE; i++) {
        frames[i] = -1;
        time[i] = 0;
    }
    for (int i = 0; i < SIZE; i++) {
        int found = 0;
        for (int j = 0; j < FRAME_SIZE; j++) {
            if (frames[j] == pages[i]) {
                counter++;
                time[j] = counter;
                found = 1;
                hits++;
                break;
            }
        }
        if (!found) {
            int lru = 0;
            for (int j = 1; j < FRAME_SIZE; j++) {
                if (time[j] < time[lru])
                    lru = j;
            }
            frames[lru] = pages[i];
            counter++;
            time[lru] = counter;
            faults++;
        }
    }
    printf("Total Page Faults using LRU: %d\n", faults);
    printf("Total Page Hits: %d\n", hits);
    return 0;
}