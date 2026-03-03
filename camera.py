import cv2

def get_camera():
    # Try index 0 first, if it fails try 1 (external cam)
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        cap = cv2.VideoCapture(1)
        if not cap.isOpened():
            raise Exception("Camera not accessible")
    return cap