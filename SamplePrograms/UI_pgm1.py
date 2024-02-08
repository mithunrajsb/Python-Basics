import tkinter as tk
from tkinter import messagebox

def on_button_click():
    messagebox.showinfo("Message", "Hello, {}!".format(entry.get()))

# Create the main application window
app = tk.Tk()
app.title("Simple UI Application")

# Create a label
label = tk.Label(app, text="Enter your name:")
label.pack()

# Create an entry widget
entry = tk.Entry(app)
entry.pack()

# Create a button
button = tk.Button(app, text="Click me!", command=on_button_click)
button.pack()

# Start the main event loop
app.mainloop()
