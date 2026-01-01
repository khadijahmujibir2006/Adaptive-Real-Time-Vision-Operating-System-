import cv2

tracker = cv2.TrackerCSRT_create()
initialized = False

def track(frame, bbox=None):
    global initialized

    if not initialized and bbox is not None:
        tracker.init(frame, bbox)
        initialized = True

    if initialized:
        success, box = tracker.update(frame)
        if success:
            x, y, w, h = map(int, box)
            cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)

    return frame
