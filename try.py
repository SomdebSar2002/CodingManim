import pyautogui
import ctypes
import time

def get_active_window_title():
    hwnd = ctypes.windll.user32.GetForegroundWindow()
    length = ctypes.windll.user32.GetWindowTextLengthW(hwnd)
    buffer = ctypes.create_unicode_buffer(length + 1)
    ctypes.windll.user32.GetWindowTextW(hwnd, buffer, length + 1)
    return buffer.value

# Example usage: Move the mouse within the current window
try:
    while True:
        x, y = pyautogui.position()
        window_title = get_active_window_title()
        print(f"Mouse Position: ({x}, {y}) | Active Window: {window_title}")
        time.sleep(0.5)  # Adjust the sleep duration as needed
except KeyboardInterrupt:
    print("\nProgram terminated.")
