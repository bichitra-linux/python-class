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
    
    # Get the terminal window
    terminal_windows = pyautogui.getWindowsWithTitle("MATE Terminal")
    if terminal_windows:
        terminal_window = terminal_windows[0]
        
        # Take a screenshot of the terminal window
        screenshot = pyautogui.screenshot(region=(terminal_window.left, terminal_window.top, terminal_window.width, terminal_window.height))
        screenshot.save(f"{command}.png")
