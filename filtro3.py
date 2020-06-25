import csv

with open("bairro.csv") as file:
    reader = csv.reader(file)
    bairros = ["FIGUEIRÊDO
               "CATOLÉ",
               "MALVINAS",
               "VILA CABRAL",
               "NOVA BRASÍLIA",
               "TRÊS IRMÃS",
               "QUARENTA",
               "MÉDICI",
               "CENTRO",
               "RAMADINHA",
               "CIDADES",
               "VELAME",
               "JARDIM PAULISTANO",
               "ESTAÇÃO VELHA",
               "JARDIM TAVARES",
               "JARDIM CONTINENTAL",
               "CRUZEIRO",
               "SANTA CRUZ",
               "NAÇÕES",
               "CUITÉS",
               "DISTRITO INDUSTRIAL",
               "ITARARÉ",
               "SANTO ANTÔNIO",
               "SANDRA CAVALCANTE",
               "TAMBOR",
               "MIRANTE",
               "DINAMÉRICA",
               "SANTA ROSA",
               "LIBERDADE",
               "CENTENÁRIO",
               "SÃO JOSÉ",
               "PEDREGAL",
               "JOSÉ PINHEIRO",
               "MONTE CASTELO",
               "BELA VISTA",
               "PRATA",
               "LAURITZEN",
               "CASTELO BRANCO",
               'CONCEIÇÃO',
               "MONTE SANTO",
               "BODOCONGÓ",
               "PALMEIRA",
               "UNIVERSITÁRIO",
               "SERROTÃO",
               "JEREMIAS",
               "LOUZEIRO",
               "ARAXÁ",
               "ALTO BRANCO",
               "NOVO BODOCONGÓ"]
    result = []
              
    for bairro in bairros:
        for row in reader :
            contador = 0
            if(bairro == row):
                contador = contador +1
        result.append( str(bairro) + ',' + str(contador))       
    
    print(result)