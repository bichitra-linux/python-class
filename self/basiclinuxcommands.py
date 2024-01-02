import subprocess
import pyautogui

# List of commands to run
commands = [
    "clear",
    "ls",
    "pwd",
    # Add more commands here
]

# Run each command and take a screenshot
for command in commands:
    # Run the command and capture the output
    output = subprocess.check_output(command, shell=True, universal_newlines=True)
    
    # Take a screenshot of the output
    screenshot = pyautogui.screenshot()
    screenshot.save(f"{command}.png")
