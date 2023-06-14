# # -*- coding: utf-8 -*-
# """Mmedias.ipynb

# Automatically generated by Colaboratory.

# Original file is located at
#     https://colab.research.google.com/drive/1BP8AwfRUupIZJkmJZ5AamWTx4hPDUUSP
# """

# def arrumar_peso():
#   peso_prova = int(input("digite o peso de prova: "))
#   if peso_prova > 1:
#     peso_prova = peso_prova/10
#   peso_trab = peso_prova-1

# p1 = int(input("digite a nota da p1: "))
# t1 = int(input("digite a nota da t1: "))
# arrumar_peso()
# media = (((p1)/2)*peso_prova + ((t1+10)/2)*peso_trab)
# if (media<6):
#   p2 = (((6-((t1+10)/2)*peso_trab)/peso_prova)*2)-p1
#   if (p2>10):
#     print("Po cara vai se sub mesmo")
#   p_sub = (((6-((t1+10)/2)*peso_trab)/peso_prova)*2)-p1
#   if (p1<p_sub):
#     p_sub = (((6-((t1+10)/2)*peso_trab)/peso_prova)*2)/2
#   print(f"Considerando a nota do T2 = 10 a Nota da P2 = {p2}")
#   print(f"Considerando que a nota da P2 nao foi a esperada vc precisa tirar {p_sub} na p_sub")
# elif(media>=6):
#    t2 = (((6-(p1/2)*peso_prova)/peso_trab)*2)-t1
#    print(f"Podendo zerar a P2, tire {t2} na T2")

# Módulos necessários
import time
import numpy as np

#Arquivos auxiliares ao código principal
import mmedias_parametros as Parametros
import mmedias_func as Funcoes
import Notas
import os

def CalcME(NotasProva, NotasTrabalho, QuantidadeProvas, QuantidadeTrabalhos, Psub, PesoProva, PesoTrabalho):

    limParametros = {
        "Provas": 
                    {"P1":              [0,     10],
                    "P2":              [0,     10],
                    "Psub":            [0,     10]}, 
        "Trabalhos": 
                    {"T1":              [0,   10],
                    "T2":              [0,   10]}
    }

    if NotasProva[0] != "":
        limParametros["Provas"]["P1"][0] = int(NotasProva[0])
        limParametros["Provas"]["P1"][1] = int(NotasProva[0])
    if NotasProva[1] != "":
        limParametros["Provas"]["P2"][0] = int(NotasProva[1])
        limParametros["Provas"]["P2"][1] = int(NotasProva[1])
    print(len(NotasTrabalho))
    if int(QuantidadeTrabalhos) != 0:
        if NotasTrabalho[0] != "":
            limParametros["Trabalhos"]["T1"][0] = int(NotasTrabalho[0])
            limParametros["Trabalhos"]["T1"][1] = int(NotasTrabalho[0])
        if int(QuantidadeTrabalhos)>1 and NotasTrabalho[1] != "":
            limParametros["Trabalhos"]["T2"][0] = int(NotasTrabalho[1])
            limParametros["Trabalhos"]["T2"][1] = int(NotasTrabalho[1])
    elif  int(QuantidadeTrabalhos) == 1:
            limParametros["Trabalhos"]["T2"][0] = 0
            limParametros["Trabalhos"]["T2"][1] = 0
    else:
            limParametros["Trabalhos"]["T1"][0] = 0
            limParametros["Trabalhos"]["T1"][1] = 0
            limParametros["Trabalhos"]["T2"][0] = 0
            limParametros["Trabalhos"]["T2"][1] = 0

    # Tempo de referência do inicio do processamento
    Init_Time = time.time()

    # Montando a primeira geração
    count_gen = 1
    count_pop = 0
    SPE = []
    tempo = time.time()
    flagsPop = [0]*(len(Parametros.flags)+1)

    n=0
    while count_pop < (Parametros.pop):
        if tempo - Init_Time >= 6000:
            count_gen = Parametros.gentot
            if Psub == "com_psub":
                print("Não tem salvação")
            else:
                print("Vai de sub")
            break
        Vpop = {}
        # Atribuindo valores aleatórios aos parâmetros de projeto
        # npar = 0
        # while npar != Parametros.Nparam:
        #     Vpop[npar] = Funcoes.valor_param(Parametros.LimParamMin[npar], Parametros.LimParamMax[npar])
        #     npar = npar + 1
        for i in limParametros:
            Vpop[i] = {}
            for j in limParametros[i]:
                Vpop[i][j] = Funcoes.valor_param(limParametros[i][j])
        NotasVpop = Notas.notas(Vpop)
        #Calculando o Mérito
        Merito, flag = Funcoes.Merit(NotasVpop, Psub, QuantidadeTrabalhos, PesoProva, PesoTrabalho) 
        if flag == 0:
            NotasVpop.merito = Merito
            SPE.append(NotasVpop)
            count_pop = count_pop + 1
        else:
            # print(count_pop, "Aviões")
            # print(flag)
            flagsPop[flag] += 1
            tempo = time.time()
            

            # if flag == 1:
            #     print("Erro 1")
                # Funcoes.displayar([[AviaoVpop.dicionario, 0]], count_gen, flagsPop)
        n += 1
        #Avançando no contador da população

    #Classificando a primeira geração pelo Mérito
    SPE = np.array(SPE)


    SPE = sorted(SPE, key=lambda x: x.merito, reverse=Parametros.maximizar)

    # Matriz final da primeira população e seu armazenamento
    # Funcoes.salvapop(SPE, count_gen)


    # Iniciando O laço de Loop das gerações
    while count_gen != (Parametros.gentot):

        #Avançando para a próxima geração
        count_gen = count_gen + 1
        #Selecionando os melhores
        BST = Funcoes.besters(SPE)
        #Salvando pela Complascência
        SAV = Funcoes.savers(SPE)
        #Matriz dos escolhidos
        ESC = Funcoes.selecters(BST, SAV)
        #Montagem dos descendentes
        DES, flagsPop = Funcoes.descenders(ESC, limParametros, Psub, QuantidadeTrabalhos, PesoProva, PesoTrabalho)
        #Montando a nova matriz de população
        SPE = Funcoes.selecters(ESC, DES) 
        #Classificando a geração pelo Mérito
        SPE = np.array(SPE)
        SPE = sorted(SPE, key=lambda x: x.merito, reverse=Parametros.maximizar)
        # #Armazenando a matriz de população
        # Funcoes.salvapop(SPE, count_gen)
        # # Mostrando Resultados Parciais
        # Funcoes.displayar(SPE, count_gen, flagsPop)

    Final_Time = time.time()
        
    return {"P1": SPE[0].P1, "P2": SPE[0].P2, "Psub":SPE[0].Psub, "T1": SPE[0].T1, "T2": SPE[0].T2}

if __name__ == "__main__":
    u_i = CalcME(["", ""], ["4"], "2", "1", "sem_psub", "1", "0")
    print(u_i)
