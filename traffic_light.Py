# Traffic Signal Simulation using Tkinter
# Author: Rohan Saini

import tkinter as tk
import time
from PIL import Image, ImageTk

def show_light(color, time_left):
    """Display traffic light image and countdown timer"""
    img = ImageTk.PhotoImage(Image.open(f"{color}.png"))
    image_label.config(image=img)
    image_label.image = img
    timer_label.config(text=f"Time Left: {time_left}s")
    root.update()

def traffic_light():
    """Traffic light control logic"""
    while True:
        for i in range(15, 0, -1):
            show_light("green", i)
            time.sleep(1)

        for i in range(5, 0, -1):
            show_light("yellow", i)
            time.sleep(1)

        for i in range(15, 0, -1):
            show_light("red", i)
            time.sleep(1)

        for i in range(5, 0, -1):
            show_light("yellow", i)
            time.sleep(1)

root = tk.Tk()
root.title("Traffic Light Signal Program")
root.geometry("700x700")

image_label = tk.Label(root)
image_label.pack(pady=20)

timer_label = tk.Label(root, font=("Arial", 20))
timer_label.pack(pady=20)

traffic_light()
root.mainloop()
