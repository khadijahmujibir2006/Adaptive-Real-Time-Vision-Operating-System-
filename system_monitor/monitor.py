import psutil

def system_stats():
    return {
        "cpu": psutil.cpu_percent(),
        "memory": psutil.virtual_memory().percent
    }
