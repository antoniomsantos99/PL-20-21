import json
import re

filePath = "D:\\DEV\\PL\\TP1\\test.csv"


#Abre o ficheiro e inicializa a lista JSON
f = open(filePath,"r")
res = []

#Separa todos os argumentos delimitados por ; na primeira linha do csv removendo os \n se existirem
args = [re.sub("\n","",x) if re.search("\n",x) else x for x in re.split(';',f.readline())]

#Começa a ler o resto das linhas do csv
for linha in f.readlines():

    #Separa todos as caracteristicas dos elementos delimitadas por ; removendo os \n se existirem
    listaelem = [re.sub("\n","",x) if re.search("\n",x) else x for x in re.split(';',linha)]

    #Cria um dicionario para o elemento (formato usado pelo json)
    elem = {}

    #Itera sobre a lista de argumentos para os relacionar com as caracteristicas
    for index in range(len(args)):
        #Verifica se o argumento contem uma lista
        if re.search("\*",args[index]):
            #Cria uma lista com o array de valores
            print(re.findall("\d+(?:\.\d+)?",listaelem[index]).group(1))
            listaValores = [float(x) for x in re.findall("\d+(?:\.\d+)?",listaelem[index])]
            #Agregação avg
            if re.search("avg$",args[index]):
                elem[re.sub("\*","_",args[index])] = sum(listaValores) / len(listaValores)
            #Agregação sum
            elif re.search("sum$",args[index]):
                elem[re.sub("\*","_",args[index])] = sum(listaValores)
            #Agregação max
            elif re.search("max$",args[index]):
                listaValores.sort()
                elem[re.sub("\*","_",args[index])] = listaValores[-1]
            #Agregação min
            elif re.search("min$",args[index]):
                listaValores.sort()
                elem[re.sub("\*","_",args[index])] = listaValores[0]
            #Se não tiver nenhuma agregação
            else:
                 elem[re.sub("\*","",args[index])] = listaValores
        #Se não for uma lista
        else:
            elem[args[index]] = listaelem[index]

    #Adiciona o elemento á lista json
    res.append(elem)

#Escreve o json num novo ficheiro
with open(filePath.replace("csv","json"), 'w') as outfile:
    json.dump(res, outfile,indent=2)
