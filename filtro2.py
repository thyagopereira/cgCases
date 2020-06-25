import csv

with open('bairro.csv') as file:
    reader = csv.reader(file)
    lista = []
    for row in reader :
        lista.append(str(row))


    lista.sort()
    for i in lista:
        print(str(i))    