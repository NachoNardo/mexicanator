from personagem import *

class Coadjuvante(Personagem):
    tipo = 0

    def __init__(self, nome, nomeComposto):
        super().__init__(nome, nomeComposto)
        self.tipo = 5