# Python Keylogger — Educational Demo

**⚠️ WARNING / ETHICS:**  
This repository contains educational keylogger code. **DO NOT** use this software on machines you do not own or without explicit written permission. Recording other people's keystrokes without consent is illegal and unethical.

---

## Purpose
This project demonstrates how keyboard events can be captured for learning defensive and detection techniques. It is intended for educational use only (research, self-learning, labs you control).

---

## Repo contents
- `keylogger.py` — Python script using `pynput` to capture keystrokes locally.  
- `.gitignore` — prevents logs / virtualenv from being uploaded.  
- `README.md` — this file.

> **Note:** The `logs/` folder and `key_log.txt` are ignored and should never be pushed to GitHub.

---

## Setup (local & safe)
1. Make a Python virtual environment (recommended):
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate
