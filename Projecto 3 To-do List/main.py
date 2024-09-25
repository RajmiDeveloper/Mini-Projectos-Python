#Projecto 3 To-do List

import os
import csv
import tkinter as tk

clear = lambda: os.system('cls')

clear() 

def escribir ():
    with open('list.csv','a', newline='') as file:
        txtInp = toDoEntry.get()
        
        writer = csv.writer(file)
        writer.writerow([str(txtInp), 1])


window = tk.Tk()
window.title("To-do List")
window.geometry("720x405")
window.configure(background="#c2bfbe")

inputFrame = tk.Frame(window)

newTask = tk.Label(window, text = "New Task:", bg="#ffc675")
newTask.pack()
toDoEntry = tk.Entry(inputFrame)
toDoEntry.pack(side='left', padx=10)
toDoButton = tk.Button(inputFrame, text = "Insert", command = escribir)
toDoButton.pack(side='right')
inputFrame.pack(fill=tk.X)





window.mainloop()
