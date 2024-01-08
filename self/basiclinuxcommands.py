import subprocess
import time
import os

# List of commands to run
commands = [
    "clear",
    "ls",
    "pwd",
    # Add more commands here
]

# Run each command and take a screenshot
for command in commands:
    # Open a new MATE Terminal window and run the command
    bash_command = f'bash -c "sleep 1; xdotool type \\"{command}\\"; xdotool key Return; exec bash"'

    subprocess.Popen(['mate-terminal', '-e', bash_command])   
    # Wait for the command to finish and the output to appear
    time.sleep(6)
    
    # Get the window ID of the MATE Terminal
    window_id = subprocess.check_output(['xdotool', 'search', '--name', 'Terminal']).split()[0]
    
    # Take a screenshot of the MATE Terminal
    os.system(f"import -window {window_id} {command}.png")
    
    # Close the terminal window
    subprocess.run(['xdotool', 'windowclose', window_id])
    
    # Wait for a second before running the next command
    time.sleep(3)