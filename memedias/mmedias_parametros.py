from random import randint
from random import uniform

pop       = 200     #Tamanho da População da Geração
gentot    = 1000    #Número de Gerações que serão analisadas
maximizar = 0      # 0 se você for minimizar o mérito e 1 se for maximizar
FraSel    = 0.30    #Fração de Seleção da Geração
FraCom    = 0.10    #Fração de Complascência da Geração
Mutate    = 0.30    #Fração de Mutação do Gene
CrOver    = 0.25    #Fração de Mutação de CrOver

flags = ['Tudo certo',
         'Media < 6']

limParametros = {
    "Provas": 
                {"P1":              [0,     10],
                 "P2":              [0,     10],
                 "Psub":            [0,     10]}, 
    "Trabalhos": 
                {"T1":              [0,   10],
                 "T2":              [0,   10],
                 "T3":              [0,   10]}
}

Nparam = 0
for i in limParametros:
    Nparam += len(limParametros[i])