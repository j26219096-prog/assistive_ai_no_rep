# 👁️ Assistive AI — Intelligence Without Representation

> A real-time assistive AI system for the visually impaired that detects objects and announces distance using geometric perception — no deep learning, no GPU, no internet required.

> *"The world is its own best model."* — Rodney Brooks

---

## 🚀 Key Features

- ⚡ **30+ FPS** on CPU — zero latency, no GPU needed
- 📐 **Geometric Classification** — identifies objects using Aspect Ratio & Solidity math, not trained models
- 📏 **Monocular Depth Estimation** — estimates distance from relative object size
- 🔊 **Voice Feedback** — speaks object positions ("Phone is close on your left")
- 🚨 **Emergency Beep** — triggers if voice engine fails or danger is imminent
- 🛡️ **Privacy First** — no images stored, uploaded, or sent to cloud

---

## 🧠 How It Works

This system uses a **3-layer Subsumption Architecture**:

| Layer | File | What it does |
|-------|------|-------------|
| Perception | `perception.py` | Canny edge detection → contour analysis → geometric shape classification |
| Decision | `decision.py` | Safety priority logic — STOP if object fills >75% of frame |
| Action | `feedback.py` | Text-to-Speech output + emergency beep fallback |

---

## 📦 Installation
```bash
git clone https://github.com/j26219096-prog/assistive_ai_no_rep.git
cd assistive_ai_no_rep
pip install -r requirements.txt
python main.py
```

Press **`q`** on the video window to quit.

---

## 📂 Project Structure
```
assistive_ai_no_rep/
├── main.py         ← Central loop, FPS counter, module coordinator
├── perception.py   ← Edge detection, contour finding, geometric math
├── decision.py     ← Priority-based decision engine
├── feedback.py     ← Text-to-Speech + emergency beep
├── camera.py       ← Camera driver handler
└── requirements.txt
```

---

## 🔮 Roadmap

- [ ] Haptic feedback via vibration motors
- [ ] Ultrasonic sensor fusion for dark environments
- [ ] Raspberry Pi Zero port for smart-glasses form factor

---

## 👨‍💻 Author

**Jawahar R** — BTech AI & Data Science, Dhanalakshmi Srinivasan Engineering College  
[GitHub](https://github.com/j26219096-prog)

---

## 📄 License
MIT
