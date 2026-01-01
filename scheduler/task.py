class Task:
    def __init__(self, name, priority, deadline, action):
        self.name = name
        self.priority = priority
        self.deadline = deadline
        self.action = action  # function pointer
