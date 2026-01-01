import cv2
import time

from data_structures.frame_queue import FrameQueue
from algorithms.scene_complexity import estimate_complexity
from system_monitor.monitor import system_stats

from vision_tasks.detect import detect
from vision_tasks.track import track

from scheduler.task import Task
from scheduler.live_scheduler import select_task


FPS_TARGET = 15
DETECTION_INTERVAL = 1.0
SCHEDULER_MODE = "PRIORITY"

cap = cv2.VideoCapture(0)
frame_queue = FrameQueue(max_size=5)

last_detection_time = 0
bbox_for_tracking = None

fps_start_time = time.time()
frame_count = 0


while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_queue.push(frame)
    current_frame = frame_queue.pop()
    if current_frame is None:
        continue

    complexity = estimate_complexity(current_frame)
    stats = system_stats()

    frame_count += 1
    elapsed = time.time() - fps_start_time
    fps = frame_count / elapsed if elapsed > 0 else 0

    if fps < FPS_TARGET:
        SCHEDULER_MODE = "PRIORITY"
        tracking_enabled = False
    else:
        SCHEDULER_MODE = "EDF"
        tracking_enabled = True

    tasks = []

    tasks.append(
        Task(
            name="DETECTION",
            priority=1,
            deadline=2,
            action="DETECT"
        )
    )

    if tracking_enabled:
        tasks.append(
            Task(
                name="TRACKING",
                priority=2,
                deadline=4,
                action="TRACK"
            )
        )

    selected_task = select_task(tasks, mode=SCHEDULER_MODE)
    now = time.time()

    if selected_task.action == "DETECT":
        if complexity != "LOW" and (now - last_detection_time > DETECTION_INTERVAL):
            current_frame, exec_time, faces = detect(current_frame)
            if faces is not None and len(faces) > 0:
                x, y, w, h = faces[0]
                bbox_for_tracking = (x, y, w, h)
            last_detection_time = now

    elif selected_task.action == "TRACK":
        if bbox_for_tracking is not None:
            current_frame = track(current_frame, bbox_for_tracking)

    cv2.putText(current_frame, f"Scheduler: {SCHEDULER_MODE}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.putText(current_frame, f"Complexity: {complexity}", (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.putText(current_frame, f"FPS: {int(fps)}", (10, 90),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.putText(current_frame, f"CPU: {stats['cpu']}%", (10, 120),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow("ARVOS", current_frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break


cap.release()
cv2.destroyAllWindows()
