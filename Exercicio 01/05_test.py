# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 02:07:35 2021

@author: Ezequiel
"""

import numpy as np

taxa_apredizado = 0.4

entradas_saidas = np.array([
    [1, 1, 1, 0, 1, 0],
    [1, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 0],
    [1, 1, 0, 0, 1, 1],
    [1, 0, 0, 1, 1, 0],
])

peso = np.array([0.1, 0.2, -0.2, -0.2, -0.3])


def entrada(x):
    xx = entradas_saidas[x][0:-1]
    return xx


def resposta(x):
    xx = entradas_saidas[x][-1:]
    return xx


def ajuste_pesos(i, ii, saida_encontrada):

    novo_w = float(peso[ii]) + taxa_apredizado * (entrada(i)[ii] *
                                                  (resposta(i) - round(float(saida_encontrada), 2)))
    novo_w = round(novo_w[0], 2)

    return novo_w


def funcao_ativacao(valor):
    if(valor > 0):
        return 1
    else:
        return 0

soma = 0
for i in range(0, len(entrada(0))):
    soma = soma + entrada(0)[i] * peso[i]



print(ajuste_pesos(0,0,0))





# Wij(n+1) = Wij + n * Xi(yd -y)
# Wij(n+1) = novo peso
# Wij(n) = peso atual
# n = taxa de aprendizado
# Xi = entrada
# y = saida encontrada
# yd = saida esperada

# Nome     Febre  Enjôo  Manchas  Dores  Diagnóstico
# João     S      S      Peq      S      Doente
# Pedro    N      N      Grd      N      Saudável
# Maria    S      S      Peq      N      Saudável
# José     S      N      Grd      S      Doente
# Ana      S      N      Peq      S      Saudável
# Leila    N      N      Grd      S      Doente
#          S:1    S:1    Grd:1    S:1    DOENTE:1
