import random
import numpy as np
import mmedias_parametros as Parametros
import os
import Notas
from math import sqrt



#Selecionando os melhores
def besters(SPE):
    SEL = []
    Sel = round(Parametros.FraSel*Parametros.pop)
    res = range(0,Sel)
    for i in res:
        SEL.append(SPE[i])
    return SEL

#Salvando pela complascência
def savers(SPE):
    SAV = []
    Sel = round(Parametros.FraSel*Parametros.pop)
    Com = round(Parametros.FraCom*Parametros.pop)
    contador = 0
    while contador != Com:
        SAV.append(SPE[Sel+Com])
        contador+=1
    return SAV

#Montando a matriz dos escolhidos
def selecters(BST,SAV):
    ESC = np.concatenate((BST,SAV), axis = 0)
    return ESC

#Montando a matriz dos descendentes
def descenders(ESC, pesos):
    nescolh = round((Parametros.FraSel + Parametros.FraCom)*Parametros.pop)
    nfilhos = Parametros.pop - nescolh
    count_pop = 0
    DES = []
    flagsPop = [0]*(len(Parametros.flags)+1)
    
    while count_pop < nfilhos+1:
        
        #Escolha dos genitores
        pai = ESC[random.randint(0,len(ESC)-1)].dicionario
        mae = ESC[random.randint(0,len(ESC)-1)].dicionario

  
        #Cruzamento das informações genéticas
        Vpop = {}
        for i in Parametros.limParametros:
            Vpop[i] = {}
            for j in Parametros.limParametros[i]:
                ran = random.random()
                if ran < Parametros.Mutate:
                    Vpop[i][j] = valor_param(Parametros.limParametros[i][j])
                elif ran < (Parametros.Mutate + Parametros.CrOver):
                    Vpop[i][j] = pai[i][j]
                else:
                    Vpop[i][j] = mae[i][j]
        NotasVpop = Notas.notas(Vpop)
        
        Merito, flag = Merit(NotasVpop, pesos) 
        if flag == 0:
            NotasVpop.merito = Merito
            DES.append(NotasVpop)
            count_pop = count_pop + 1
        else:
            flagsPop[flag] += 1
    
    return DES, flagsPop

# def salvapop(SPE, count_gen):

#     for Notas in SPE:
#         linha = np.array([])
#         for i in Parametros.limParametros:
#             for j in Parametros.limParametros[i]:
#                 linha = np.append(linha, [Notas.dicionario[i][j]])
#         try:
#             salvar = np.append(salvar, [linha], axis=0)
#         except:
#             salvar = np.array([linha])
    
#     if count_gen % 500 == 0 or count_gen <= 10:
#         np.savetxt(f'Pop_gen_{count_gen}.txt', salvar, delimiter=';')


    # if count_gen == 1:
    #     np.savetxt('Header.txt', [list(vars(SPE[0]).keys())[1:]], delimiter = ';', fmt="%s")
    # if count_gen % 500 == 0 or count_gen <= 10:
    #     if count_gen % 500 == 0:
    #         np.savetxt(f'Pop_gen_{count_gen}.txt', [list(vars(x).values())[1:] for x in SPE], delimiter=';')

def Merit(Notas, pesos):
    media = pesos[0]*((Notas.P1 + Notas.P2)/2) + pesos[1]*((Notas.T1+Notas.T2+Notas.T3)/3)

    if media < 6:
        # Media muito baixa
        flag = 1
    else:
        flag = 0

    Mer = media
    return Mer, flag

def Pesos():
    pesos = []
    prova = float(input("Insira o peso das provas em forma decimal (Por exemplo: 0.6), se não houver provas na matéria insira 0: "))
    trabalhos = 1-prova
    pesos.append(prova)
    pesos.append(trabalhos)
    return pesos

def valor_param(x):
    ran = random.random()
    x = x[0] + (x[1] - x[0])*ran
    x = round(x,2)
    return x