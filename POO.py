from tkinter import *
import random
import time

class Pelota:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10,10,25,25, fill=color)
        self.canvas.move(self.id, 245, 100)


tk = Tk()
tk.title("First")
tk.resizable(0,0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=400, height=400, bd=0, highlghtthicknees=0)
canvas.pack()
tk.update()