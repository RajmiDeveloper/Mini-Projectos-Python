#projecto 2: lectura de Logs

from datetime import datetime
import os
import csv
clear = lambda: os.system('cls')
date_format = "%d/%b/%Y:%H:%M:%S %z"

i = 1
listIps = [[]]
clear()

with open("Projecto 2 Lectura Logs\logs.txt", 'r') as file:
    lista = file.readlines()
    for line in lista:
        
        pointer = 0
        ip = line[pointer:(line.find(" - - "))]
        pointer = line.find(" - - ")+6
        date = line[pointer:pointer+26]
        pointer = pointer + 28
        error = line[pointer+1:line.find('"', pointer+1)]
        pointer = line.find('"', pointer+1)+2
        numError = line[pointer:pointer+3]
        pointer = pointer+4
        sizeAns = line[pointer:-1]

        i += 1
        fechaformateada = datetime.strptime(date, date_format)
        for n in range(len(listIps)+1):
            if(0 <= n < len(listIps)):
                try:   
                    if listIps[n][0] == ip:
                        listIps[n][1] += 1
                        listIps[n].append(fechaformateada)
                        break
                except:
                    listIps[0].append(f"{ip}")
                    listIps[0].append( 1)
                    listIps[0].append(fechaformateada)
                    break
            else:
                listIps.append([f"{ip}", 1,fechaformateada])


with open("Projecto 2 Lectura Logs/results.csv", mode='w') as wFile:
    writer = csv.writer(wFile, delimiter='|')
    for n in range(len(listIps)):
        writer.writerow(listIps[n])