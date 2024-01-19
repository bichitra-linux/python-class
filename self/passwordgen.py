import tkinter as tk
import random
import string

class PasswordGenerator:
    """A simple GUI application for generating random passwords."""

    def __init__(self, window):
        self.window = window
        self.window.title("Password Generator")

        self._create_widgets()

    def _create_widgets(self):
        """Create and pack the widgets for the application."""
        frame = tk.Frame(self.window, padx=20, pady=20)
        frame.pack()

        length_label = tk.Label(frame, text="Password Length:")
        length_label.grid(row=0, column=0, sticky='e')

        self.length_entry = tk.Entry(frame)
        self.length_entry.grid(row=0, column=1)

        generate_button = tk.Button(frame, text="Generate Password", command=self.generate_password)
        generate_button.grid(row=1, column=0, columnspan=2, pady=10)

        password_label = tk.Label(frame, text="Generated Password:")
        password_label.grid(row=2, column=0, sticky='e')

        self.password_entry = tk.Entry(frame)
        self.password_entry.grid(row=2, column=1)

    def generate_password(self):
        """Generate a random password and display it in the password entry."""
        length = int(self.length_entry.get())
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(tk.END, password)


# Create the main window and start the application
window = tk.Tk()
app = PasswordGenerator(window)
window.mainloop()