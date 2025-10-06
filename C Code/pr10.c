#include <stdio.h>
#include <stdbool.h>
#define SIZE 16  
#define FRAME_SIZE 3
int main() {
    int pages[SIZE] = {0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 4, 5, 6, 7};
    int frames[FRAME_SIZE];
    int front = 0, count = 0, faults = 0;
    for (int i = 0; i < FRAME_SIZE; i++)
        frames[i] = -1;
    for (int i = 0; i < SIZE; i++) {
        bool hit = false;
        for (int j = 0; j < FRAME_SIZE; j++) {
            if (frames[j] == pages[i]) {
                hit = true;
                break;
            }
        }
        if (!hit) {
            frames[front] = pages[i];
            front = (front + 1) % FRAME_SIZE;
            faults++;
        }
    }
    printf("Total Page Faults using FIFO: %d\n", faults);
    printf("Total Page Hits: %d\n", SIZE - faults);
    return 0;
}