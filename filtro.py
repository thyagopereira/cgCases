import csv

with open("base.csv") as file:
    reader = csv.DictReader(file)
    lista = [] 
    for row in reader :
        if( (row["MunicÃ­pio de ResidÃªncia"]  == "Campina Grande") and (row["Resultado do Teste"]  == "Positivo") ):
            lista.append(row["Bairro"])

    lista.sort()
    for i in lista:
        print(i)