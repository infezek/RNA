import numpy as np

taxa_apredizado = 0.03

entradas_saidas = np.array([
    [1, 1.00, .20, 0],
    [1, 1.00, .26, 1],
    [1, 1.00, .30, 1],

    [1, 1.00, .32, 1],
    [1, 1.02, .21, 0],
    [1, 1.05, .22, 0],

    [1, 1.07, .32, 1],
    [1, 1.10, .35, 1],
    [1, 1.11, .25, 0],

    [1, 1.14, .24, 0],
    [1, 1.16, .36, 1],
    [1, 1.18, .27, 0],
])

peso = np.array([.5, .2, .7])


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


print('Peso inicial: '+str(peso))


def treinamento():
    global peso
    nao_teve_ajuste = 0

    for i in range(0, len(entradas_saidas)):
        somatorio = 0
        for jj in range(0, len(entrada(i))):
            somatorio = somatorio + entrada(i)[jj] * peso[jj]

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

entradas_saidas = np.array([
    [1, 1.00, .50, 1],
    [1, 1.20, .20, 0],
    [1, 1.20, .70, 1],
])


print('\n Rede treinada: ' + str(peso))

print('\n +Peso = 1 ')
print('  Normal = 1 \n')
valores = 'XXX'
for i in range(0, len(entradas_saidas)):
    valor_encontrado = 0
    for jj in range(0, len(entrada(i))):
        valor_encontrado = valor_encontrado + entrada(i)[jj] * peso[jj]

    saida_encontrada = funcao_ativacao(valor_encontrado)

    if(saida_encontrada == 0):
        valores = 'Normal'
    else:
        valores = '+ Peso'

    if(saida_encontrada == resposta(i)):
        print('Acertou - saida encontrada: ' +
              str(saida_encontrada) + ' - ' + valores)
    else:
        print('err ' + str(saida_encontrada))


# Wij(n+1) = Wij + n * Xi(yd -y)
# Wij(n+1) = novo peso
# Wij(n) = peso atual
# n = taxa de aprendizado
# Xi = entrada
# y = saida encontrada
# yd = saida esperada
