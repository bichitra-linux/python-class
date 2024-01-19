import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import ThemedTk
import random
import string
import pyperclip

class PasswordGenerator:
    """A simple GUI application for generating random passwords."""

    def __init__(self, window):
        self.window = window
        self.window.title("Password Generator")

        self.password_history = []

        self._create_widgets()

    def _create_widgets(self):
        """Create and pack the widgets for the application."""
        frame = ttk.Frame(self.window, padding="20 20 20 20")
        frame.pack()

        length_label = ttk.Label(frame, text="Password Length:")
        length_label.grid(row=0, column=0, sticky='e')

        self.length_entry = ttk.Entry(frame)
        self.length_entry.grid(row=0, column=1)

        strength_label = ttk.Label(frame, text="Password Strength:")
        strength_label.grid(row=1, column=0, sticky='e')

        self.strength_var = tk.StringVar()
        self.strength_combobox = ttk.Combobox(frame, textvariable=self.strength_var)
        self.strength_combobox['values'] = ('Weak', 'Medium', 'Strong')
        self.strength_combobox.current(0)
        self.strength_combobox.grid(row=1, column=1)

        generate_button = ttk.Button(frame, text="Generate Password", command=self.generate_password)
        generate_button.grid(row=2, column=0, columnspan=2, pady=10)

        password_label = ttk.Label(frame, text="Generated Password:")
        password_label.grid(row=3, column=0, sticky='e')

        self.password_entry = ttk.Entry(frame)
        self.password_entry.grid(row=3, column=1)

        copy_button = ttk.Button(frame, text="Copy to Clipboard", command=self.copy_to_clipboard)
        copy_button.grid(row=4, column=0, columnspan=2, pady=10)

        history_label = ttk.Label(frame, text="Password History:")
        history_label.grid(row=5, column=0, sticky='e')

        self.history_listbox = tk.Listbox(frame)
        self.history_listbox.grid(row=5, column=1)

    def generate_password(self):
        """Generate a random password and display it in the password entry."""
        length = int(self.length_entry.get())
        if length < 8:
            messagebox.showerror("Error", "Password length should be at least 8.")
            return

        strength = self.strength_var.get()

        if strength == 'Weak':
            pool = string.ascii_lowercase
        elif strength == 'Medium':
            pool = string.ascii_letters + string.digits
        else:  # Strong
            pool = string.ascii_letters + string.digits + string.punctuation

        password = ''.join(random.choices(pool, k=length))
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(tk.END, password)

        self.password_history.append(password)
        self.password_history = self.password_history[-5:]  # Keep only the last 5 passwords

        self.history_listbox.delete(0, tk.END)
        for password in self.password_history:
            self.history_listbox.insert(tk.END, password)

    def copy_to_clipboard(self):
        """Copy the generated password to the clipboard."""
        password = self.password_entry.get()
        pyperclip.copy(password)


# Create the main window and start the application
window = ThemedTk(theme="arc")  # Use a Material Design-like theme
app = PasswordGenerator(window)
window.mainloop()