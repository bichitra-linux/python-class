import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from ttkthemes import ThemedTk
import random
import string
import pyperclip
import hashlib
import csv

class ToolTip:
    """A custom tooltip class for displaying tooltips on widgets."""

    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None

        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event):
        """Display the tooltip."""
        x = self.widget.winfo_rootx() + self.widget.winfo_width() + 5
        y = self.widget.winfo_rooty() + self.widget.winfo_height() + 5

        self.tooltip = tk.Toplevel()
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")

        label = tk.Label(self.tooltip, text=self.text, background="#ffffe0", relief="solid", borderwidth=1)
        label.pack()

    def hide_tooltip(self, event):
        """Hide the tooltip."""
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None

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
        frame.pack(fill=tk.BOTH, expand=True)

        length_label = ttk.Label(frame, text="Password Length:")
        length_label.grid(row=0, column=0, sticky='e')
        ToolTip(length_label, "Enter the desired length of the password.")

        self.length_entry = ttk.Entry(frame)
        self.length_entry.grid(row=0, column=1, sticky='w')

        generate_button = ttk.Button(frame, text="Generate Password", command=self.generate_password)
        generate_button.grid(row=1, column=0, columnspan=2, pady=10)
        ToolTip(generate_button, "Generate a random password.")

        password_label = ttk.Label(frame, text="Generated Password:")
        password_label.grid(row=2, column=0, sticky='e')

        self.password_entry = ttk.Entry(frame)
        self.password_entry.grid(row=2, column=1, sticky='w')

        copy_button = ttk.Button(frame, text="Copy to Clipboard", command=self.copy_to_clipboard)
        copy_button.grid(row=3, column=0, columnspan=2, pady=10)
        ToolTip(copy_button, "Copy the generated password to the clipboard.")

        clear_button = ttk.Button(frame, text="Clear History", command=self.clear_history)
        clear_button.grid(row=4, column=0, columnspan=2, pady=10)
        ToolTip(clear_button, "Clear the password history.")

        history_label = ttk.Label(frame, text="Password History:")
        history_label.grid(row=5, column=0, sticky='e')

        self.history_listbox = tk.Listbox(frame)
        self.history_listbox.grid(row=5, column=1, sticky='w')

        self.progress_bar = ttk.Progressbar(frame, mode='indeterminate')
        self.progress_bar.grid(row=6, column=0, columnspan=2, pady=10)

        save_button = ttk.Button(frame, text="Save History to File", command=self.save_history_to_file)
        save_button.grid(row=7, column=0, columnspan=2, pady=10)
        ToolTip(save_button, "Save the password history to a file.")

        load_button = ttk.Button(frame, text="Load History from File", command=self.load_history_from_file)
        load_button.grid(row=8, column=0, columnspan=2, pady=10)
        ToolTip(load_button, "Load the password history from a file.")

        export_button = ttk.Button(frame, text="Export History to CSV", command=self.export_history_to_csv)
        export_button.grid(row=9, column=0, columnspan=2, pady=10)
        ToolTip(export_button, "Export the password history to a CSV file.")

        import_button = ttk.Button(frame, text="Import History from CSV", command=self.import_history_from_csv)
        import_button.grid(row=10, column=0, columnspan=2, pady=10)
        ToolTip(import_button, "Import the password history from a CSV file.")

        encrypt_button = ttk.Button(frame, text="Encrypt Password", command=self.encrypt_password)
        encrypt_button.grid(row=11, column=0, columnspan=2, pady=10)
        ToolTip(encrypt_button, "Encrypt the generated password.")

        scrollbar = ttk.Scrollbar(self.window)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        canvas = tk.Canvas(self.window, yscrollcommand=scrollbar.set)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar.config(command=canvas.yview)

        canvas.create_window((0, 0), window=frame, anchor="nw")

    def generate_password(self):
        """Generate a random password and display it in the password entry."""
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError("Password length should be a positive integer.")

            pool = string.ascii_letters + string.digits + string.punctuation

            self.progress_bar.start()

            password = ''.join(random.choices(pool, k=length))
            self.password_entry.delete(0, tk.END)
            self.password_entry.insert(tk.END, password)

            self.password_history.append(password)
            self.password_history = self.password_history[-5:]  # Keep only the last 5 passwords

            self.history_listbox.delete(0, tk.END)
            for password in self.password_history:
                self.history_listbox.insert(tk.END, password)

        except ValueError as e:
            messagebox.showerror("Error", str(e))

        finally:
            self.progress_bar.stop()

    def copy_to_clipboard(self):
        """Copy the generated password to the clipboard."""
        password = self.password_entry.get()
        pyperclip.copy(password)

    def clear_history(self):
        """Clear the password history."""
        self.password_history = []
        self.history_listbox.delete(0, tk.END)

    def save_history_to_file(self):
        """Save the password history to a file."""
        filename = filedialog.asksaveasfilename(defaultextension=".txt")
        if filename:
            with open(filename, 'w') as file:
                for password in self.password_history:
                    file.write(password + '\n')

    def load_history_from_file(self):
        """Load the password history from a file."""
        filename = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if filename:
            self.password_history = []
            with open(filename, 'r') as file:
                for line in file:
                    password = line.strip()
                    self.password_history.append(password)
                    self.history_listbox.insert(tk.END, password)

    def export_history_to_csv(self):
        """Export the password history to a CSV file."""
        filename = filedialog.asksaveasfilename(defaultextension=".csv")
        if filename:
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Password'])
                writer.writerows([[password] for password in self.password_history])

    def import_history_from_csv(self):
        """Import the password history from a CSV file."""
        filename = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if filename:
            self.password_history = []
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip the header row
                for row in reader:
                    password = row[0]
                    self.password_history.append(password)
                    self.history_listbox.insert(tk.END, password)

    def encrypt_password(self):
        """Encrypt the generated password using SHA-256."""
        password = self.password_entry.get()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(tk.END, hashed_password)


# Create the main window and start the application
window = ThemedTk(theme="arc")  # Use a Material Design-like theme
app = PasswordGenerator(window)
window.mainloop()