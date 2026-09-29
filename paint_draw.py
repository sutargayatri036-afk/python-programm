import tkinter as tk
from tkinter import colorchooser

# Create window
window = tk.Tk()
window.title("🖌️ Mini Paint App")
window.geometry("900x650")
window.configure(bg="lightgray")

# ---------------- SETTINGS ----------------
brush_color = "black"
brush_size = 5

# ---------------- FUNCTIONS ----------------

def start_drawing(event):
    global last_x, last_y
    last_x = event.x
    last_y = event.y


def draw(event):
    global last_x, last_y

    canvas.create_line(
        last_x,
        last_y,
        event.x,
        event.y,
        fill=brush_color,
        width=brush_size,
        capstyle=tk.ROUND,
        smooth=True
    )

    last_x = event.x
    last_y = event.y


def choose_color():
    global brush_color

    color = colorchooser.askcolor()[1]

    if color:
        brush_color = color


def change_size(size):
    global brush_size
    brush_size = int(size)


def clear_canvas():
    canvas.delete("all")


# ---------------- TITLE ----------------

title = tk.Label(
    window,
    text="🖌️ MINI PAINT",
    font=("Arial", 22, "bold"),
    bg="lightgray"
)

title.pack(pady=10)


# ---------------- TOOLBAR ----------------

toolbar = tk.Frame(window, bg="lightgray")
toolbar.pack(pady=5)

color_button = tk.Button(
    toolbar,
    text="🎨 Choose Color",
    command=choose_color,
    bg="white"
)

color_button.pack(side="left", padx=5)


size_label = tk.Label(
    toolbar,
    text="Brush Size:",
    bg="lightgray"
)

size_label.pack(side="left", padx=5)


size_slider = tk.Scale(
    toolbar,
    from_=1,
    to=30,
    orient="horizontal",
    command=change_size,
    bg="lightgray"
)

size_slider.set(5)
size_slider.pack(side="left")


clear_button = tk.Button(
    toolbar,
    text="🗑️ Clear",
    command=clear_canvas,
    bg="white"
)

clear_button.pack(side="left", padx=10)


# ---------------- CANVAS ----------------

canvas = tk.Canvas(
    window,
    width=850,
    height=500,
    bg="white",
    cursor="cross"
)

canvas.pack(pady=10)


# ---------------- MOUSE EVENTS ----------------

canvas.bind("<Button-1>", start_drawing)
canvas.bind("<B1-Motion>", draw)


# ---------------- START ----------------

window.mainloop()
