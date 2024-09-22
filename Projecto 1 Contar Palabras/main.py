#Projecto 1: Detectar cantidad de palabras
import os
clear = lambda: os.system('cls')

clear()
print("ingrese un texto")
inp = input()
list = []
delimeter = [" ", ".", ",", ";"]
cantP = 0
spaceReady = True
for i,s in enumerate(inp):
    if (s != " " and spaceReady == True):
        cantP += 1
        spaceReady = False
    elif (s in delimeter):
        spaceReady = True 
print(f"Cantidad de palabras: {cantP}")