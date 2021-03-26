import numpy as np

taxa_apredizado = 0.01

entradas_saidas = np.array([
    [1, 1.00, 0.20, 0],
    [1, 1.00, 0.26, 1],
    [1, 1.00, 0.30, 1],
    [1, 1.00, 0.32, 1],
    [1, 1.02, 0.21, 0],
    [1, 1.05, 0.22, 0],
    [1, 1.07, 0.32, 1],
    [1, 1.10, 0.35, 1],
    [1, 1.11, 0.25, 0],
    [1, 1.14, 0.24, 0],
    [1, 1.16, 0.36, 1],
    [1, 1.18, 0.27, 0],
])

peso = np.array([-0.5, 0.4, -0.6])


def entrada(x):
    xx = entradas_saidas[x][0:-1]
    return xx


def resposta(x):
    xx = entradas_saidas[x][-1:]
    return xx


def ajuste_pesos(i, ii, saida_encontrada):
    """
    print(float(peso[ii]))
    print(taxa_apredizado)
    print(entrada(i)[ii])
    print((resposta(i) - round(float(saida_encontrada), 2))[0])
    print("===============")
    """
    novo_w = float(peso[ii]) + (taxa_apredizado * entrada(i)
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
print('Rede treinada: ' + str(peso))


entradas_saidas = np.array([
    [100, 20, 0],
    [100, 26, 1],
])


for i in range(0, len(entradas_saidas)):
    valor_encontrado = np.dot(entradas_saidas[i], peso)
    saida_encontrada = funcao_ativacao(valor_encontrado)

    print('Saida encontrada: ' + str(saida_encontrada))


# Wij(n+1) = Wij + n * Xi(yd -y)
# Wij(n+1) = novo peso
# Wij(n) = peso atual
# n = taxa de aprendizado
# Xi = entrada
# y = saida encontrada
# yd = saida esperada
