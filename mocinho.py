from personagem import *

class Mocinho(Personagem):
    tipo = 0

    def __init__(self, nome, nomeComposto):
        super().__init__(nome, nomeComposto)
        self.tipo = 2