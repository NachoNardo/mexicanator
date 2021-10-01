class EpisodioFinal:
    listaDefinais = []

    def inserirFinal(self, final):
        self.listaDefinais.append(final)
    
    def toString(self):
        
        episodioFinal = ""

        for final in self.listaDefinais:
            episodioFinal += "\n" + final

        return episodioFinal