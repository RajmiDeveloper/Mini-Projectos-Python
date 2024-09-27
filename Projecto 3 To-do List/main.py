#Projecto 3 To-do List

import os
import csv
import tkinter as tk
import pandas as pd

clear = lambda: os.system('cls')

clear() 
script_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(script_dir, 'list.csv')

def checkFile():
    if not os.path.exists(path): 
        with open(path, 'w', newline='') as file: 
            writer = csv.writer(file)
            writer.writerow(['toDo','check'])


listToDo = []
def escribir ():
    with open(path,'a', newline='') as file:
        if toDoEntry.get():
            data = {'toDo': [toDoEntry.get()], 'check': [1]}
            dataF = pd.DataFrame(data)
            dataF.to_csv(path, mode = 'a', index=False, header=False)
            actualizar()
        

def delRow(i):
    dataF = pd.read_csv(path, delimiter=',')
    dataF = dataF.drop(dataF.index[i])
    dataF.to_csv(path, index=False)
    actualizar()
widgetsList = []
def actualizar():
    with open(path,'r') as file:
        dataF = pd.read_csv(path, delimiter = ',')
        dataL = dataF.values.tolist()
        if widgetsList:
            for n in widgetsList:
                n[0].destroy()
                n[1].destroy()
                n[2].destroy()
            widgetsList.clear()
        toDoList = []

        i = 0
        for n in dataL:
            toDoList.append(n)
            toDoList[i][0:0] = [i]  
            frame = tk. Frame(window)
            label = tk.Label(frame, text = n[1])
            button = tk.Button(frame, text="Terminada", command=lambda i=i+1: delRow(i-1))
            label.pack(side='left',padx=75)
            button.pack(side='right', padx=75)
            frame.pack(fill=tk.X)
            widgetsList.append([frame, label, button])
            i += 1


checkFile()
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
actualizar()



window.mainloop()
