class Personagem:
    __nome = ""
    __nomeComposto = ""

    def __init__(self, nome, nomeComposto):
        self.__nome = nome
        self.__nomeComposto = nomeComposto

    def setNome(self, nome):
        self.__nome = nome
    
    def getNome(self):
        return self.__nome

    def setNomeComposto(self, nomeComposto):
        self.__nomeComposto = nomeComposto

    def getNomeComposto(self):
        return self.__nomeComposto