import sys

"""
pr12.py

Sequential File Allocation Simulation

Usage:
- On start you set the total number of blocks on the disk.
- Menu options allow creating files (auto-first-fit or at a given start),
    deleting files, and displaying disk/file table state.

This is a simple educational simulation (no real filesystem calls).
"""


def input_int(prompt, min_val=None, max_val=None):
        while True:
                try:
                        v = int(input(prompt).strip())
                        if (min_val is not None and v < min_val) or (max_val is not None and v > max_val):
                                print("Value out of allowed range.")
                                continue
                        return v
                except ValueError:
                        print("Please enter a valid integer.")

def find_contiguous_free(blocks, size):
        n = len(blocks)
        if size <= 0 or size > n:
                return -1
        run = 0
        start = 0
        for i in range(n):
                if blocks[i] is None:
                        if run == 0:
                                start = i
                        run += 1
                        if run >= size:
                                return start
                else:
                        run = 0
        return -1

def create_file(blocks, file_table):
        name = input("Enter file name: ").strip()
        if not name:
                print("Invalid name.")
                return
        if name in file_table:
                print("File already exists.")
                return
        size = input_int("Enter file size (number of contiguous blocks): ", min_val=1)
        mode = input("Allocate automatically? (y/n) [y]: ").strip().lower() or "y"
        if mode == "y":
                start = find_contiguous_free(blocks, size)
                if start == -1:
                        print("No contiguous region of size", size, "available.")
                        return
        else:
                start = input_int(f"Enter starting block index (0 to {len(blocks)-1}): ", min_val=0, max_val=len(blocks)-1)
                if start + size > len(blocks):
                        print("Requested range exceeds disk size.")
                        return
                # check contiguous free
                for i in range(start, start + size):
                        if blocks[i] is not None:
                                print("Blocks not free in the requested range. Allocation failed.")
                                return
        # allocate
        for i in range(start, start + size):
                blocks[i] = name
        file_table[name] = (start, size)
        print(f"File '{name}' allocated from block {start} to {start+size-1}.")

def delete_file(blocks, file_table):
        name = input("Enter file name to delete: ").strip()
        if name not in file_table:
                print("No such file.")
                return
        start, size = file_table.pop(name)
        for i in range(start, start + size):
                # safety check: only clear if it matches the file name
                if blocks[i] == name:
                        blocks[i] = None
        print(f"File '{name}' deleted (blocks {start}..{start+size-1} freed).")

def display_disk(blocks):
        n = len(blocks)
        print("\nDisk Blocks:")
        # print a compact view: index and content ('.' for free)
        line = []
        for i in range(n):
                cell = "." if blocks[i] is None else blocks[i]
                line.append(f"{i}:{cell}")
        # print wrapped lines to remain readable
        per_line = 8
        for i in range(0, n, per_line):
                print("  " + " | ".join(line[i:i+per_line]))
        print()

def display_file_table(file_table):
        if not file_table:
                print("File table empty.")
                return
        print("\nFile Table:")
        print("  Name\tStart\tSize\tEnd")
        for name, (start, size) in file_table.items():
                print(f"  {name}\t{start}\t{size}\t{start+size-1}")
        print()

def main():
        print("Sequential File Allocation Simulator")
        total_blocks = input_int("Enter total number of disk blocks: ", min_val=1)
        blocks = [None] * total_blocks
        file_table = {}

        menu = (
                "\nMenu:\n"
                "  1. Create file (sequential allocation)\n"
                "  2. Delete file\n"
                "  3. Display disk blocks\n"
                "  4. Display file table\n"
                "  5. Exit\n"
        )

        while True:
                print(menu)
                choice = input("Choose an option (1-5): ").strip()
                if choice == "1":
                        create_file(blocks, file_table)
                elif choice == "2":
                        delete_file(blocks, file_table)
                elif choice == "3":
                        display_disk(blocks)
                elif choice == "4":
                        display_file_table(file_table)
                elif choice == "5":
                        print("Exiting.")
                        sys.exit(0)
                else:
                        print("Invalid option.")

if __name__ == "__main__":
        main()