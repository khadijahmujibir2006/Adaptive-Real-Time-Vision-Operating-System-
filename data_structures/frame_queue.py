from collections import deque

class FrameQueue:
    def __init__(self, max_size=10):
        self.queue = deque(maxlen=max_size)

    def push(self, frame):
        self.queue.append(frame)

    def pop(self):
        if self.queue:
            return self.queue.popleft()
        return None

    def size(self):
        return len(self.queue)
