import time
import tkinter as tk

def update_time():
    current_time = time.strftime("%I:%M:%S %p")
    label.config(text=current_time)
    label.after(1000, update_time)

root = tk.Tk()
label = tk.Label(root, font=("Arial", 24))
label.pack()

update_time()

root.mainloop()
