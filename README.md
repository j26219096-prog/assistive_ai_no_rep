# 👁️ Intelligence Without Representation: Assistive AI
### A Real-Time Perception System for the Visually Impaired

> **"The world is its own best model."** — Rodney Brooks

This project is a lightweight, reactive AI system designed to help visually impaired users navigate their environment and identify objects in real-time. Unlike traditional AI that relies on heavy Deep Learning models (like YOLO) and expensive GPUs, this system uses **Geometric Perception** and **Subsumption Architecture**.

It runs on low-power devices (CPU only) at **30+ FPS**, offering immediate safety feedback without internet or data storage.

---

## 🚀 Key Features

* **⚡ Zero-Latency Detection:** Runs at 30+ frames per second on standard laptops.
* **📐 Geometric Classification:** Identifies objects (Phones, Bottles, Boxes) using math (Aspect Ratio & Solidity) rather than image training.
* **📏 Monocular Depth Estimation:** Calculates distance using relative object size to warn users of immediate danger ("Stop!" vs "Warning").
* **🔊 Robust Audio Feedback:**
    * **Primary:** Voice descriptions ("Phone is close on your left").
    * **Backup:** Emergency Beeps if the audio driver fails or the danger is imminent.
* **🛡️ Privacy First:** No images are stored, uploaded, or processed in the cloud.

---

## 🛠️ How It Works (The Algorithm)

This system implements **"Intelligence Without Representation"**: it does not build a complex 3D map of the world. Instead, it reacts directly to visual inputs using a 3-layer architecture:

1.  **Perception Layer (`perception.py`):**
    * Uses **Canny Edge Detection** to strip color/texture.
    * Connects broken edges using **Morphological Dilation**.
    * Analyzes shapes based on **Solidity** (how solid the object is) and **Aspect Ratio** (height vs width).
    * *Example:* A "Phone" is defined as a solid rectangle (Solidity > 0.85) with an aspect ratio between 1.5 and 3.0.

2.  **Decision Layer (`decision.py`):**
    * Prioritizes safety above all else.
    * If an object fills >75% of the screen → **EMERGENCY STOP**.
    * If path is clear → Describe background objects.

3.  **Action Layer (`feedback.py`):**
    * Manages audio threads to prevent lag.
    * Uses a "Watchdog Timer" to reset the voice engine if it gets stuck.

---

## 📦 Installation

### Prerequisites
* Python 3.x
* Webcam

### 1. Clone the Repository
```bash
git clone [https://github.com/j26219096-prog/assistive_ai_no_rep.git](https://github.com/j26219096-prog/assistive_ai_no_rep.git)
cd assistive_ai_no_rep
### 2. Install Dependencies
```bash
pip install -r requirements.txt
---

## ▶️ Usage

1.  **Run the Main Script:**
    ```bash
    python main.py
    ```

2.  **Controls:**
    * The system will start speaking automatically.
    * **Quit:** Click the video window and press **`q`**.

---

## 📂 Project Structure

| File | Description |
| :--- | :--- |
| `main.py` | The central loop. Handles FPS counting, crosshair display, and coordinates all modules. |
| `perception.py` | The "Eye". Handles edge detection, contour finding, and geometric math. |
| `decision.py` | The "Brain". Decides what to say based on priority (Safety > Description). |
| `feedback.py` | The "Mouth". Handles Text-to-Speech (TTS) and emergency beeps. |
| `camera.py` | Handles camera drivers and connection. |

---

## 🔮 Future Scope
* **Haptic Feedback:** Integrating vibration motors for silent distance alerts.
* **Ultrasonic Fusion:** Adding hardware sensors to double-check distance measurements in pitch-dark environments.
* **Wearable Integration:** Porting the code to a Raspberry Pi Zero for a smart-glasses form factor.

---

## 📜 License
This project is open-source and available under the [MIT License](LICENSE).
