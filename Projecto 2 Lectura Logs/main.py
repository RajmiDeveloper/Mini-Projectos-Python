#projecto 2: lectura de Logs
i = 1
with open("D:\Github\MiniP Python\Projecto 2 Lectura Logs\logs.txt", 'r') as file:
    lista = file.readlines()
    for line in lista:
        print(f"Linea {i}")
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
        
        print(f"ip: {ip}")
        print(f"date: {date}")
        print(f"error: {error}")
        print(f"numError: {numError}")
        print(f"size of the answer: {sizeAns}")
        i += 1