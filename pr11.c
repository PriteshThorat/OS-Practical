# /d:/Projects/OS-Practical/pr11.py
# LRU page replacement simulation for the reference string:
# 0,1,2,3,0,1,2,3,0,1,2,3,4,5,6,7 with frame size 3

def lru_page_faults(reference, capacity):
    frames = []            # hold pages, LRU at index 0, MRU at -1
    faults = 0
    for i, page in enumerate(reference, 1):
        if page in frames:
            # hit: move page to MRU position
            frames.remove(page)
            frames.append(page)
            action = "hit"
        else:
            # miss/fault
            faults += 1
            if len(frames) < capacity:
                frames.append(page)
            else:
                # evict LRU (index 0)
                frames.pop(0)
                frames.append(page)
            action = "fault"
        print(f"{i:2d}: access {page} -> {action:5s} | frames = {frames}")
    return faults

if __name__ == "__main__":
    ref_string = [0,1,2,3,0,1,2,3,0,1,2,3,4,5,6,7]
    capacity = 3
    faults = lru_page_faults(ref_string, capacity)
    print(f"\nTotal page faults (LRU, frames={capacity}): {faults}")