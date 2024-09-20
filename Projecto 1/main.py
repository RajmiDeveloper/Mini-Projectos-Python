#Projecto 1: Detectar cantidad de palabras
import os
clear = lambda: os.system('cls')

clear()
print("ingrese un texto")
inp = input()
list = []
cantP = 0
spaceReady = True
for i,s in enumerate(inp):
    if (s != " " and spaceReady == True):
        cantP += 1
        spaceReady = False
    elif (s == " "):
        spaceReady = True 
        
print(f"Cantidad de palabras: {cantP}")