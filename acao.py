class Acao():
    __personagem1 = ""
    __personagem2 = ""
    __acao = ""
    __local = ""

    def __init__(self, personagem1, personagem2, acao, local):
        self.__personagem1 = personagem1
        self.__personagem2 = personagem2
        self.__acao = acao
        self.__local = local
    
    def getPersonagem1(self):
        return self.__personagem1

    def getPersonagem2(self):
        return self.__personagem2

    def getAcao(self):
        return self.__acao

    def getLocal(self):
        return self.__local

    def toString(self):
        return (self.getPersonagem1() + self.getAcao() + self.getPersonagem2() + self.getLocal())