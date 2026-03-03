import pyttsx3
import threading
import winsound  # Built-in Windows sound library

# Global flag to prevent voice overlap
is_speaking = False

def _speak_thread(text, is_emergency):
    global is_speaking
    try:
        # EMERGENCY BEEP (Works even if voice fails)
        if is_emergency:
            # Frequency 1000Hz, Duration 200ms
            winsound.Beep(1000, 200) 

        # Initialize a FRESH engine every time (Reliable for Demos)
        engine = pyttsx3.init()
        engine.setProperty("rate", 165)
        
        engine.say(text)
        engine.runAndWait()
        
    except Exception as e:
        print(f"Audio Error: {e}")
        # If voice crashes, beep again so you know it detected something
        winsound.Beep(500, 500)
    finally:
        is_speaking = False

def speak(text):
    global is_speaking
    
    # If currently talking, ignore new non-emergency messages
    if is_speaking:
        return

    is_speaking = True
    
    # Check if this is a "Stop" message to trigger the beep
    is_emergency = "Stop" in text
    
    t = threading.Thread(target=_speak_thread, args=(text, is_emergency))
    t.start()