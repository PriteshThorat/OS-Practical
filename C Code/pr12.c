#include <stdio.h>
#include <stdbool.h>
#define MAX_BLOCKS 50
#define MAX_FILES 10
int main() {
    int total_blocks, blocks[MAX_BLOCKS] = {0};
    int file_count;
    printf("Enter total number of disk blocks: ");
    scanf("%d", &total_blocks);
    printf("Enter number of files: ");
    scanf("%d", &file_count);
    for (int i = 0; i < file_count; i++) {
        int start, length;
        printf("\nFile %d:\n", i + 1);
        printf("Enter starting block and length: ");
        scanf("%d %d", &start, &length);
        if (start < 0 || start + length > total_blocks) {
            printf("Allocation failed: exceeds disk size.\n");
            continue;
        }
        bool can_allocate = true;
        for (int j = start; j < start + length; j++) {
            if (blocks[j] == 1) {
                can_allocate = false;
                break;
            }
        }
        if (can_allocate) {
            for (int j = start; j < start + length; j++) {
                blocks[j] = 1;
            }
            printf("File allocated from block %d to %d\n", start, start + length - 1);
        } else {
            printf("Allocation failed: blocks already occupied.\n");
        }
    }
    printf("\nDisk Block Status:\n");
    for (int i = 0; i < total_blocks; i++) {
        printf("Block %d: %s\n", i, blocks[i] ? "Occupied" : "Free");
    }
    return 0;
}