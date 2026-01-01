import heapq

class TaskQueue:
    def __init__(self):
        self.heap = []

    def add_task(self, priority, task):
        heapq.heappush(self.heap, (priority, task))

    def get_task(self):
        if self.heap:
            return heapq.heappop(self.heap)
        return None
