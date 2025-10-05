from collections import deque

# pr10.py
# FIFO page replacement simulation for:
# reference string: 0,1,2,3,0,1,2,3,0,1,2,3,4,5,6,7
# frame size: 3
# computes page faults for two cases:
# 1) standard FIFO starting with empty frames
# 2) FIFO starting with frames preloaded with the first distinct pages (no initial load counted)


REF = [0,1,2,3,0,1,2,3,0,1,2,3,4,5,6,7]
FRAME_SIZE = 3

def fifo_page_faults(ref, frame_size, preload=False):
    frames = deque()
    in_frame = set()
    faults = 0

    if preload:
        # preload first distinct pages up to frame_size without counting faults
        for p in ref:
            if p not in in_frame:
                frames.append(p)
                in_frame.add(p)
            if len(frames) == frame_size:
                break

    # To implement FIFO eviction, we use deque (popleft when evicting).
    for p in ref:
        if p in in_frame:
            continue  # hit
        # miss
        faults += 1
        if len(frames) < frame_size:
            frames.append(p)
            in_frame.add(p)
        else:
            evicted = frames.popleft()
            in_frame.remove(evicted)
            frames.append(p)
            in_frame.add(p)
    return faults

def main():
    faults_empty = fifo_page_faults(REF, FRAME_SIZE, preload=False)
    faults_preloaded = fifo_page_faults(REF, FRAME_SIZE, preload=True)

    print("Reference string:", REF)
    print("Frame size:", FRAME_SIZE)
    print()
    print("FIFO starting with empty frames -> page faults:", faults_empty)
    print("FIFO with first distinct pages preloaded -> page faults:", faults_preloaded)

if __name__ == "__main__":
    main()