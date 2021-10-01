class Episodio:
    listaDeAcoes = []

    def inserirAcao(self, acao):
        self.listaDeAcoes.append(acao)
    
    def toString(self):
        
        episodio = ""

        for acao in self.listaDeAcoes:
            episodio += "\n" + acao

        return episodio
