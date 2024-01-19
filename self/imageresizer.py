import tkinter as tk
from PIL import Image, ImageTk

def resize_image():
    # Get the selected file path
    file_path = file_entry.get()

    # Get the desired width and height
    width = int(width_entry.get())
    height = int(height_entry.get())

    # Open the image using PIL
    image = Image.open(file_path)

    # Resize the image
    resized_image = image.resize((width, height))

    # Display the resized image
    resized_image.show()

def update_preview():
    # Get the selected file path
    file_path = file_entry.get()

    # Open the image using PIL
    image = Image.open(file_path)

    # Resize the image to fit the preview label
    preview_width = 200
    preview_height = 200
    resized_image = image.resize((preview_width, preview_height))

    # Convert the resized image to Tkinter PhotoImage
    photo = ImageTk.PhotoImage(resized_image)

    # Update the preview label with the resized image
    preview_label.configure(image=photo)
    preview_label.image = photo

# Create the main window
window = tk.Tk()
window.title("Image Resizer")

# Create the file path entry
file_label = tk.Label(window, text="File Path:")
file_label.pack()
file_entry = tk.Entry(window)
file_entry.pack()

# Create the width entry
width_label = tk.Label(window, text="Width:")
width_label.pack()
width_entry = tk.Entry(window)
width_entry.pack()

# Create the height entry
height_label = tk.Label(window, text="Height:")
height_label.pack()
height_entry = tk.Entry(window)
height_entry.pack()

# Create the resize button
resize_button = tk.Button(window, text="Resize", command=resize_image)
resize_button.pack()

# Create the image preview label
preview_label = tk.Label(window)
preview_label.pack()

# Create the update preview button
update_preview_button = tk.Button(window, text="Update Preview", command=update_preview)
update_preview_button.pack()

# Start the main loop
window.mainloop()
