import cv2
import time
from camera import get_camera
from perception import perceive
from decision import decide
from feedback import speak

def main():
    try:
        cap = get_camera()
        print("System Started. Click Video Window and press 'q' to quit.")
        speak("System online.")
    except Exception as e:
        print(f"Error: {e}")
        return

    last_message = "Path is clear"
    last_speak_time = 0
    
    # Debounce variables (Stability)
    clear_path_counter = 0 
    REQUIRED_CLEAR_FRAMES = 5
    
    # FPS Variables
    prev_frame_time = 0
    new_frame_time = 0

    while True:
        ret, frame = cap.read()
        if not ret: break

        # 1. Perception
        detected_objects, edges = perceive(frame)
        
        # 2. Decision
        raw_message = decide(detected_objects)
        
        # 3. STABILITY LOGIC
        if raw_message == "Path is clear":
            clear_path_counter += 1
        else:
            clear_path_counter = 0

        if clear_path_counter >= REQUIRED_CLEAR_FRAMES:
            message = "Path is clear"
        elif raw_message != "Path is clear":
            message = raw_message
        else:
            message = last_message

        # 4. Action (Speaking)
        current_time = time.time()
        time_diff = current_time - last_speak_time
        should_speak = False
        
        if message != last_message:
            should_speak = True
        elif message != "Path is clear" and time_diff > 4.0:
            should_speak = True

        if should_speak:
            print(f"🗣️ {message}") 
            speak(message)
            last_message = message
            last_speak_time = current_time

        # 5. VISUALIZATION (HUD)
        
        # A. Draw Boxes
        if detected_objects:
            for obj in detected_objects:
                x, y, cw, ch = obj["box"]
                color = obj["color"]
                lbl = obj.get('label', 'Object')
                dist = obj.get('dist', '')
                cv2.rectangle(frame, (x, y), (x + cw, y + ch), color, 2)
                cv2.putText(frame, f"{lbl} {dist}", (x, y - 10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

        # B. FPS Counter (Proof of Speed)
        new_frame_time = time.time()
        fps = 1 / (new_frame_time - prev_frame_time) if (new_frame_time - prev_frame_time) > 0 else 0
        prev_frame_time = new_frame_time
        fps_text = f"System Speed: {int(fps)} FPS"

        # C. Crosshair (Targeting)
        h, w = frame.shape[:2]
        cx, cy = w // 2, h // 2
        cv2.line(frame, (cx - 20, cy), (cx + 20, cy), (200, 200, 200), 2)
        cv2.line(frame, (cx, cy - 20), (cx, cy + 20), (200, 200, 200), 2)

        # D. Draw Stats Background
        cv2.rectangle(frame, (5, 5), (280, 45), (0, 0, 0), -1) 
        cv2.putText(frame, fps_text, (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        cv2.imshow("Assistive AI - Edge View", edges)
        cv2.imshow("Assistive AI - Camera Feed", frame)

        # Click video window and press 'q' to quit
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()