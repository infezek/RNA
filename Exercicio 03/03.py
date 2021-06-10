# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 11:44:29 2019

@author: Nilton Alves Maia
         Programa de Pós-Graduação em Modelagem Computacional e Sistemas - PPGMCS
         Departamento de Ciências da Computação - DCC
         Universidade Estadual de Montes Claros - UNIMONTES
"""
import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer

eta=0.005   # antes 0.3

# Padrões de Treinamento
x=[[1, 0.2, 0.3], 
    [1, 0.1, 0.4], 
    [1, 0.4, 0.3], 
    [1, 0.11, 0.9], 
    [1, 0.84, 0.6], 
    [1, 0.1, 0.2],
    [1, 0.6, 0.2],
    [1, 0.2, 0.2],
    [1, 0.7, 0.8], 
    [1, 0.1, 0]]

yd=[0.13, 0.17, 0.25, 0.822, 1.065, 0.05, 0.4, 0.08,1.13, 0.01]

entradas=len(x[0])
padroes=len(x)

print("Treinamento do Adaline")
numciclos=int(input("Informe o numero de ciclos desejados: "))
print("\nNumero de entradas(x):",entradas,"Numero de padroes:",padroes,"\n")
winicial = [0, 0, 0]
w=winicial
print("Pesos iniciais: ", w)  

initreino = timer()

EMQG = []
errodes=0.00
EMQ=1
j=1
epoca=0
while ((EMQ > errodes) and (epoca < numciclos)):
    eq = []    
    for i in range(0,padroes):
        print("\nCiclo: ",j," Padrao: ",i+1) 
        net=np.dot(x[i],w)
        y=net
        print("Somatorio(net): ", "%.4f" % net)
        print("Saida desejada(yd): ", "%.2f" % yd[i]," Saida calculada(y): ", "%.2f" % y)   
        
        e = yd[i] - y 
        
        #eq.append(0.5 * (e[i])**2)
        eq.append(0.5 * (e)**2)      
                          
        if (e != 0):            
           w = w + eta*np.dot(x[i],e)              
           
        print("erro(e): ", "%.4f" % e)  
        print("erro quadrático(eq): ", "%.4f" % eq[i]) 
        print("Pesos: ",w)     
    
    # Calculo do erro medio quadrático
    somaeq=0;
    for i in range(0,padroes):
        somaeq = somaeq + eq[i]
    
    EMQ = somaeq/padroes           
    print("EMQ: ", "%.8f" % EMQ) 
    #EMQG[j]=EMQ
    EMQG.append(EMQ)           
    j=j+1
    epoca = epoca + 1

fimtreino = timer()

epoch = np.linspace(1,len(EMQG),len(EMQG))
# %matplotlib inline 
"exec(%matplotlib inline)" 
plt.plot(epoch, EMQG)
plt.xlabel("Ciclos")
plt.ylabel("EMQ")
plt.title("Evolução do Erro Médio Quadrático(EMQ)" + " - " +str(numciclos)+ " Ciclos")

# Padrões de Teste

# [1, 0.7, 0.8], [1, 0.1, 0]
# 1.13,           0.01

xt=[[1, 0.2, 0.3], [1, 0.1, 0.4]]
padroest=len(xt)

initeste = timer()
for i in range(0,padroest):
    #print("\nPadrao de treinamento: ", "%d" % i+1)  
    print("\nPadrao de treinamento: ", i+1)
    net=np.dot(xt[i],w)
    y=net
    print("Saida desejada(yd): ", "%.2f" % yd[i], " Saida calculada(y): ", "%.2f" % y)   

fimteste = timer()
tempotreino = fimtreino-initreino
tempoteste = fimteste-initeste
tempototal = tempotreino + tempoteste


# [1, 0.7, 0.8], [1, 0.1, 0]
# 1.13,           0.01
print("=============================")
print("\nTeste da previsão:") 
xt=[1, 0.7, 0.8]
net=np.dot(xt,w)
y=net;
print("Saida prevista(y): ", "%.2f" % y); 

print ("\nTempo de treinamento = ", "%.4f" % tempotreino, "segundos")
print ("Tempo de teste = ", "%.4f" % tempoteste, "segundos")
print ("Tempo total (treinamento + teste) = ", "%.4f" % tempototal, "segundos")

tempotreinoms = tempotreino*1000
tempotestems = tempoteste*1000
tempototalms = tempototal*1000
print ("\nTempo de treinamento = ", "%.4f" % tempotreinoms, "ms")
print ("Tempo de teste = ", "%.4f" % tempotestems, "ms")
print ("Tempo total (treinamento + teste) = ", "%.4f" % tempototalms, "ms")