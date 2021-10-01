import random

class Elenco:
    
    listaDeCoadjuvantes = []
    listaDeMocinhos = []
    listaDeViloes = []

    def insereMocinha(self, mocinha):
        self.listaDeMocinhos.append(mocinha)

    def insereMocinho(self, mocinho):
        self.listaDeMocinhos.append(mocinho)

    def insereVilao(self, vilao):
        self.listaDeViloes.append(vilao)
    
    def insereVila(self, vila):
        self.listaDeViloes.append(vila)

    def insereCoadjuvante(self, coadjuvante):
        self.listaDeCoadjuvantes.append(coadjuvante)

    def getMocinha(self):
        return self.listaDeMocinhos[0]
        
    def getMocinho(self):
        return self.listaDeMocinhos[1]
    
    def getVila(self):
        return self.listaDeViloes[0]
        
    def getVilao(self):
        return self.listaDeViloes[1]

    def getQuantidadeCoadjuvantes(self):
        return len(self.listaDeCoadjuvantes)

    def getCoadjuvante(self, indice):
        return self.listaDeCoadjuvantes[indice]

    def listarElenco(self):
        elenco = "Mocinha: " + self.listaDeMocinhos[0] + "\n"
        elenco += "Mocinho: " + self.listaDeMocinhos[1] + "\n"
        elenco += "Vila: " + self.listaDeViloes[0] + "\n"
        elenco += "Vilao: " + self.listaDeViloes[1] + "\n"

        indice = self.getQuantidadeCoadjuvantes()
        while(indice > 0):

            elenco += "Codjuvante: " + self.listaDeCoadjuvantes[indice -1] + "\n"
            indice -= 1

        return elenco

    def getAleatorio(self):
        total = 4 + self.getQuantidadeCoadjuvantes() - 1
        aleatorio = random.randint(0,total)
        if (aleatorio == 0):
            return self.listaDeMocinhos[0]
        elif (aleatorio == 1):
            return self.listaDeMocinhos[1]
        elif (aleatorio == 2):
            return self.listaDeViloes[0]
        elif (aleatorio == 3):
            return self.listaDeViloes[1]
        else:
            aleatorio = random.randint(0,self.getQuantidadeCoadjuvantes() - 1)
            return (self.listaDeCoadjuvantes[aleatorio])