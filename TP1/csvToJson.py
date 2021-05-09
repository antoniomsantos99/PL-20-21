# Library json para a conversão
import json
#Library re para fazer as expressões regulares
import re
#Library sys para podermos receber e ler argumentos na linha de comandos
import sys

#Se recebermos o nome do ficheiro como argumento então converte esse ficheiro, caso contrário usa o caminho por defeito
if(len(sys.argv) == 1):
    filePath = "test.csv"
else:
    filePath = sys.argv[1]

#Abre o ficheiro e inicializa a lista JSON
f = open(filePath,"r",encoding='utf8')
res = []

#Separa todos os argumentos delimitados por ; na primeira linha do csv removendo os \n se existirem
args = [re.sub("\n","",x) if re.search("\n",x) else x for x in re.split(';',f.readline())]

#Começa a ler o resto das linhas do csv
for linha in f.readlines():

    #Separa todos as caracteristicas dos elementos delimitadas por ; removendo os \n se existirem
    listaelem = [re.sub("\n","",x) if re.search("\n",x) else x for x in re.split(';',linha)]

    #Se a quantidade de valores e a quantidade de argumentos for diferente atiramos um erro e o programa para
    if(len(args) != len(listaelem)):
        raise Exception("CSV Inválido! (Num de argumentos != Num de Valores)")

    #Cria um dicionario para o elemento (formato usado pelo json)
    elem = {}

    #Itera sobre a lista de argumentos para os relacionar com as caracteristicas
    for index in range(len(args)):
        
        #Verifica se o argumento contem uma lista
        if re.search("\*",args[index]):
            
            #Se o elemento não for uma lista de formato (num,...) então atiramos um erro e o programa para
            if not re.match("^\((\d+(?:\.\d+)*)(,(\d+(?:\.\d+)*))*\)$",listaelem[index]):
                raise Exception("CSV Inválido! (Lista inválida)")
            
            #Cria uma lista com o array de valores
            listaValores = [float(x) for x in re.findall("\d+(?:\.\d+)?",listaelem[index])]
            
            #Cria uma lista com todas as operações sobre a lista do CSV
            listaAgr = re.split("\*",args[index])
            
            #Itera cada operação para executar
            for agr in listaAgr[1:]:
                #Agregação avg
                if agr == "avg":
                    elem[listaAgr[0]+'_'+agr] = sum(listaValores) / len(listaValores)
                #Agregação sum
                elif agr == "sum":
                    elem[listaAgr[0]+'_'+agr] = sum(listaValores)
                #Agregação max
                elif agr == "max":
                    listaValores.sort()
                    elem[listaAgr[0]+'_'+agr] = listaValores[-1]
                #Agregação min
                elif agr == "min":
                    listaValores.sort()
                    elem[listaAgr[0]+'_'+agr] = listaValores[0]
                #Se não tiver nenhuma agregação
                else:
                    elem[re.sub("\*\w*","",args[index])] = listaValores
        #Se não for uma lista
        else:
            elem[args[index]] = listaelem[index]

    #Adiciona o elemento á lista json
    res.append(elem)

#Escreve o json num novo ficheiro
with open(re.sub("csv$","json",filePath), 'w', encoding='utf-8') as jsonFile:
    json.dump(res, jsonFile,indent=2,ensure_ascii=False)