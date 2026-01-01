def select_task(tasks, mode="PRIORITY"):
    if mode == "EDF":
        return min(tasks, key=lambda t: t.deadline)
    else:  # PRIORITY
        return min(tasks, key=lambda t: t.priority)
