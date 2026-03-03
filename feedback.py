import pyttsx3
import threading
import time

# SAFE IMPORT: Prevents crash on Mac/Linux
try:
    import winsound
except ImportError:
    winsound = None  # We are not on Windows

# Global flag to prevent voice overlap
is_speaking = False

def _speak_thread(text, is_emergency):
    global is_speaking
    try:
        # EMERGENCY BEEP (Only runs if winsound exists)
        if is_emergency and winsound:
            winsound.Beep(1000, 200) 

        # Initialize engine
        engine = pyttsx3.init()
        engine.setProperty("rate", 165)
        
        engine.say(text)
        engine.runAndWait()
        
    except Exception as e:
        print(f"Audio Error: {e}")
        # Backup beep (Only if winsound exists)
        if winsound:
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
