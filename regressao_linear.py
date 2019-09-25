import csv
import math
from random import randint
import matplotlib.pyplot as plt
import numpy as np



def modelo( data, tipo, i):
    dados = dv_dados(data, tipo)
    b_treino, b_teste = dv_bases(dados, i)
    b_0, b_1 = regressao_linear(b_treino, tipo)
    x = [d[0] for d in dados]
    y = [(b_0 + (d[0] * b_1)) for d in dados]
    print(sorted(set(w)))
    desvio = desvio_padrao(b_teste, b_0, b_1)
    print("Desvio padrão: " + str( round(desvio, 2) ))
    plt.title('Média Provas x ' + tipo )
    plt.xlabel(tipo.title())
    plt.ylabel('Média provas')
    plt.scatter(x, y)
    plt.plot(x, y)
    plt.show()


def desvio_padrao( b_teste, b_0, b_1):
    desvio = 0
    for d in b_teste:
        y = d[1]
        fx = (b_0 + (d[0] * b_1))
        desvio += (y - fx) ** 2
    return desvio

def regressao_linear( b_treino, type):
    N = len(b_treino)
    x = somatorio(b_treino, 'x')
    y = somatorio(b_treino, 'y')
    xy = somatorio(b_treino, 'xy')
    x1 = somatorio(b_treino, 'x2')
    b_1 = ((x * y) - (N * xy)) / ((x ** 2) - (N * x1))
    b_0 = (y - (b_1 * x))/ N
    print(type + ": y = " + str( round(b_0, 2)) + " + " + str(round(b_1, 2)) + "x")
    return b_0, b_1

def somatorio( l_n, tipo):
    numeros = []
    for t in l_n:
        if tipo == 'x':
            a = t[0]
        elif tipo == 'y':
            a = t[1]
        elif tipo == 'xy':
            a = t[0] * t[1]
        elif tipo == 'x2':
            a = t[0] ** 2
        else:
            a = 1
            print('Erro')
        numeros.append(a)
    return sum(numeros)

def dv_dados( data, tipo):
    res = []
    for item in data:
        if tipo == "Idade":
            x = item.get("Idade")
        elif tipo == "Tempo de Estudo":
            x = item.get("Tempo de Estudo")
        elif tipo == "Faltas":
            x = item.get("Faltas") 
        y = item.get("MediaProvas")
        res.append((int(x), int(y)))
    return res      

def dv_bases(dados, i):
    p_treino = []
    while (len(p_treino) < round(i * 0.7)):
        posicao = randint(0, i - 1)
        if posicao not in p_treino:
            p_treino.append(posicao)
    d_treino = [dados[p] for p in p_treino]
    d_treino = [dados[p] for p in range(len(dados)) if p not in p_treino]
    return d_treino, d_treino
   


def excutar():
    data = []
    with open("AnaliseEstudo.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=";")
        for row in csv_reader:
            if row[0] != "Idade":
                media = (int(row[3]) + int(row[4]) + int(row[5])) / 3 
                aux = {
                    "Idade": row[0],
                    "Tempo de Estudo": row[1],
                    "Faltas":row[2],
                    "MediaProvas": media
                }
                data.append(aux)
    for tipo in ["Idade", "Tempo de Estudo", "Faltas"]:
        modelo(data, tipo, len(data))


excutar()