import os
class TextEditor:
    def __init__(self):
        self.text = ""

    def open_file(self):
        file_path = input("Enter the file path: ")
        with open(file_path, 'r') as file:
            self.text = file.read()

    def save_file(self):
        file_path = input("Enter the file path: ")
        file_extension = input("Enter the file extension: ")
        file_path_with_extension = os.path.splitext(file_path)[0] + file_extension
        with open(file_path_with_extension, 'w') as file:
            file.write(self.text)

    # Rest of the class methods...

# Usage example:
editor = TextEditor()
editor.open_file()
editor.append_text("Hello, world!")
editor.save_file()
