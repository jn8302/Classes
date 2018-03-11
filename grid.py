from tkinter import *
from tkinter import ttk

root = Tk()

Label(root, text = "Hello").grid(row = 0)
Label(root, text = "World").grid(row = 1)

e1 = Entry(root)

e1.grid(row = 0, column = 1)

logo = Image.open("assets/python_logo.png")
logo.grid(row = 1, column = 1)
