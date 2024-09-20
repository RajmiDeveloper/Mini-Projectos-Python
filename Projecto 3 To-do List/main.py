#Projecto 3 To-do List

import os
import csv
import tkinter as tk
clear = lambda: os.system('cls')

clear()
window = tk.Tk()
window.title("To-do List")
window.geometry("720x405")
window.configure(background="#c2bfbe")

newTask = tk.Label(window, text = "New Task:", bg="#ffc675")
newTask.grid(row=1, column=1)
toDoEntry = tk.Entry(window)
toDoEntry.grid(row=2,column=0)

window.mainloop()