# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 15:37:30 2021

@author: Ezequiel
"""

import numpy as np

taxa_apredizado = 0.1

entradas_saidas = np.array([
    [1, 1, 0, 1],
    [1, 0, 1, 1],
    [1, 1, 1, 1],
    [1, 0, 0, 0],
])

peso = np.array([-0.5, 0, 0])


def entrada(x):
    xx = entradas_saidas[x][0:-1]
    return xx


def resposta(x):
    xx = entradas_saidas[x][-1:]
    return xx


def ajuste_pesos(i, ii, saida_encontrada):

    novo_w = float(peso[ii]) + taxa_apredizado * (entrada(i)
                                                  [ii] * (resposta(i) - round(float(saida_encontrada), 2)))
    novo_w = round(novo_w[0], 2)

    return novo_w


def funcao_ativacao(valor):
    if(valor > 0):
        return 1
    else:
        return 0


print('Peso inicial: '+str(peso))


def treinamento():
    global peso
    nao_teve_ajuste = 0

    for i in range(0, len(entradas_saidas)):
        somatorio = np.dot(entrada(i), peso)
        saida_encontrada = funcao_ativacao(somatorio)

        if(saida_encontrada != resposta(i)):
            novos_pesos = []
            nao_teve_ajuste = 1
            for ii in range(0, len(entrada(i))):
                novos_pesos.append(ajuste_pesos(i, ii, saida_encontrada))
            peso = novos_pesos
            print('Novo peso: ' + str(peso))
        if(nao_teve_ajuste):
            treinamento()


treinamento()

print('\n Rede treinada: ' + str(peso))
print('\n Teste \n')


for i in range(0, len(entradas_saidas)):
    valor_encontrado = np.dot(entrada(i), peso)
    saida_encontrada = funcao_ativacao(valor_encontrado)
    if(saida_encontrada == resposta(i)):
        print('Acertou - saida encontrada: ' + str(saida_encontrada))
    else:
        print('err')
