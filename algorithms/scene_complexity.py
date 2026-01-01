import cv2
import numpy as np

def estimate_complexity(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    edge_density = np.mean(edges)

    if edge_density > 50:
        return "HIGH"
    elif edge_density > 20:
        return "MEDIUM"
    else:
        return "LOW"
