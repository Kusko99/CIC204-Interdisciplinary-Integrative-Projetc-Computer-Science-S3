import mmedias_parametros as param
class notas:
    def __init__(self, dicionarioNotas=''):
        if dicionarioNotas != '':
            #Dicionario
            self.dicionario = dicionarioNotas

            self.P1 = dicionarioNotas["Provas"]["P1"]

            self.P2 = dicionarioNotas["Provas"]["P2"]

            self.Psub = dicionarioNotas["Provas"]["Psub"]

            self.T1 = dicionarioNotas["Trabalhos"]["T1"]

            self.T2 = dicionarioNotas["Trabalhos"]["T2"]

            self.T3 = dicionarioNotas["Trabalhos"]["T3"]