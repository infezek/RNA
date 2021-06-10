import numpy as np

taxa_apredizado = 0.03
epocas = 2

entradas_saidas = np.array([
    [1, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0],
    [1, 1, 1, 0, 1],
    [1, 0, 1, 1, 0],
    [1, 1, 0, 0, 1],
])

peso = np.array([0.2, 0.6, .1, .3])


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


index_epocas = 1
def treinamento():
    global peso
    global epocas
    global index_epocas
    nao_teve_ajuste = 0
    print("Epoca: "+ str(index_epocas))
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
            

        if(epocas != index_epocas):
            print("Epoca: "+ str(index_epocas))
            print('Novo peso: ' + str(peso))
            index_epocas = index_epocas + 1
            treinamento()


treinamento()

entradas_saidas = np.array([
    [1, 0, 1, 1, 0],
    [1, 1, 0, 0, 1],
])


print('\n Rede treinada: ' + str(peso))

print('\n Mamifero = 1 ')
print(' Não Mamífero = 0 \n')
print(' TESTE \n')
valores = 'XXX'
for i in range(0, len(entradas_saidas)):
    valor_encontrado = 0
    for jj in range(0, len(entrada(i))):
        valor_encontrado = valor_encontrado + entrada(i)[jj] * peso[jj]

    saida_encontrada = funcao_ativacao(valor_encontrado)

    if(saida_encontrada == 0):
        valores = 'Não mamifero'
    else:
        valores = 'Mamifero'

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
