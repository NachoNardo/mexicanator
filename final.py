class Final():
    __personagem = "" 
    __acao = "" 

    def __init__(self, personagem, acao):
        self.__personagem = personagem
        self.__acao = acao
    
    def getPersonagem(self):
        return self.__personagem

    def getAcao(self):
        return self.__acao

    def toString(self):
        return (self.getPersonagem() + self.getAcao())