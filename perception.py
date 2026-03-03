import cv2
import numpy as np

def perceive(frame):
    # 1. Pre-processing
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (7, 7), 0)
    edges = cv2.Canny(blur, 40, 120) 
    
    # Close gaps to make solid shapes
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    closed_edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

    contours, _ = cv2.findContours(
        closed_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    h, w = frame.shape[:2]
    detected_objects = []

    if not contours:
        return [], closed_edges

    # Sort by area (Biggest first)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    # Look at TOP 5 objects
    for cnt in contours[:5]:
        area = cv2.contourArea(cnt)
        if area < 2000: continue # Ignore tiny noise

        x, y, cw, ch = cv2.boundingRect(cnt)
        
        # --- MATH ---
        aspect_ratio = float(ch) / cw
        width_ratio = cw / w
        rect_area = cw * ch
        solidity = float(area) / rect_area 
        
        # --- CLASSIFICATION ---
        label = "Object"
        
        # Only guess specific names if the shape is VERY SOLID (Rectangular)
        # This prevents calling a face (round/blobby) a "Box"
        if solidity > 0.85:
            if 1.5 < aspect_ratio < 3.0:
                label = "Phone" # Solid + Tall
            elif 0.8 < aspect_ratio < 1.2:
                label = "Box"   # Solid + Square
            elif aspect_ratio > 3.0:
                label = "Bottle" # Solid + Very Tall
        
        # --- DISTANCE CALIBRATION ---
        # 0.75 = Must fill 75% of screen to be "Very Close" (Touching lens)
        if width_ratio > 0.75:
            dist = "very close"
            color = (0, 0, 255) # Red
        # 0.30 = Normal interaction distance
        elif width_ratio > 0.30:
            dist = "close"
            color = (0, 255, 255) # Yellow
        else:
            dist = "far"
            color = (0, 255, 0) # Green

        # Position
        obj_center = x + cw // 2
        if obj_center < w * 0.33: pos = "left"
        elif obj_center > w * 0.66: pos = "right"
        else: pos = "center"

        detected_objects.append({
            "label": label,
            "dist": dist,
            "pos": pos,
            "box": (x, y, cw, ch),
            "color": color
        })

    return detected_objects, closed_edges