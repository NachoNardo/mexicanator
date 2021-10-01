import docx
from episodio import *
from episodioFinal import *
from elenco import *
from mocinha import *
from mocinho import *
from vila import *
from vilao import *
from coadjuvante import *
from acao import *
from final import *
import random
from gerarDocx import *

def main():
    listaDeSelecao = selecao()
    casting = elenco(listaDeSelecao[0])
    roteiro = gerarRoteiro(casting, listaDeSelecao[1])
    docx = GerarDocx
    docx.inserirTítulo(docx)
    docx.inserirElenco(docx, casting.listarElenco())
    docx.gerar(docx, roteiro)
    print("Novela criada com sucesso!")

def selecao():
    numeroCoadjuvantes = int(input("Digite o número de coadjuvantes: "))
    numeroDeEpisodios = int(input("Digite o número de episódios: "))
    listaDeSelecao = [numeroCoadjuvantes, numeroDeEpisodios]
    return listaDeSelecao

def elenco(coadjuvantes):
    
    elenco = Elenco()

    arquivo = open("nomes_femininos.txt", "r")
    nomesFemininos = arquivo.readlines()
    
    arquivo = open("nomes_masculinos.txt", "r")
    nomesMasculinos = arquivo.readlines()
    
    arquivo = open("nomes_compostos.txt", "r")
    nomesCompostos = arquivo.readlines()
    
    tamanho = len(nomesFemininos)
    indice = random.randint(0,(tamanho-1))
    tamanho = len(nomesCompostos)
    indice2 = random.randint(0,(tamanho-1))
    
    mocinha = Mocinha(nomesFemininos[indice], nomesCompostos[indice2])
    elenco.listaDeMocinhos.append(mocinha.getNome().rstrip("\n") + mocinha.getNomeComposto().rstrip("\n"))

    tamanho = len(nomesMasculinos)
    indice = random.randint(0,(tamanho-1))
    tamanho = len(nomesCompostos)
    indice2 = random.randint(0,(tamanho-1))
    
    mocinho = Mocinho(nomesMasculinos[indice], nomesCompostos[indice2])
    elenco.listaDeMocinhos.append(mocinho.getNome().rstrip("\n")  + mocinho.getNomeComposto().rstrip("\n") )

    tamanho = len(nomesFemininos)
    indice = random.randint(0,(tamanho-1))
    tamanho = len(nomesCompostos)
    indice2 = random.randint(0,(tamanho-1))
    
    vila = Vila(nomesFemininos[indice], nomesCompostos[indice2])
    elenco.listaDeViloes.append(vila.getNome().rstrip("\n")  + vila.getNomeComposto().rstrip("\n") )

    tamanho = len(nomesMasculinos)
    indice = random.randint(0,(tamanho-1))
    tamanho = len(nomesCompostos)
    indice2 = random.randint(0,(tamanho-1))
    
    vilao = Vilao(nomesMasculinos[indice], nomesCompostos[indice2])
    elenco.listaDeViloes.append(vilao.getNome().rstrip("\n")  + vilao.getNomeComposto().rstrip("\n") )

    while(coadjuvantes>0):

        if ((coadjuvantes%2)==0):

            tamanho = len(nomesFemininos)
            indice = random.randint(0,(tamanho-1))
            tamanho = len(nomesCompostos)
            indice2 = random.randint(0,(tamanho-1))
            coadjuvante = Coadjuvante(nomesFemininos[indice].rstrip("\n") , nomesCompostos[indice2].rstrip("\n"))

        else:

            tamanho = len(nomesMasculinos)
            indice = random.randint(0,(tamanho-1))
            tamanho = len(nomesCompostos)
            indice2 = random.randint(0,(tamanho-1))
            coadjuvante = Coadjuvante(nomesMasculinos[indice], nomesCompostos[indice2])
            
        elenco.listaDeCoadjuvantes.append(coadjuvante.getNome().rstrip("\n")  + coadjuvante.getNomeComposto().rstrip("\n"))
        coadjuvantes -= 1

    return elenco

def gerarRoteiro(elenco, episodios):
    
    episodio = Episodio()
    episodioFinal = EpisodioFinal()
    temporada = []
    numeroEpisodio = 0

    while (numeroEpisodio < episodios):
        
        arquivo = open("locais.txt", "r")
        locais = arquivo.readlines()
    
        arquivo = open("acoes.txt", "r")
        acoes = arquivo.readlines()

        tamanho = len(acoes)
        indice = random.randint(0,(tamanho-1))
        tamanho = len(locais)
        indice2 = random.randint(0,(tamanho-1))
        acao = Acao(elenco.listaDeMocinhos[0], elenco.listaDeViloes[0], acoes[indice], locais[indice2])
        episodio.inserirAcao(acao.toString())

        tamanho = len(acoes)
        indice = random.randint(0,(tamanho-1))
        tamanho = len(locais)
        indice2 = random.randint(0,(tamanho-1))
        acao = Acao(elenco.listaDeMocinhos[1], elenco.listaDeViloes[1], acoes[indice], locais[indice2])
        episodio.inserirAcao(acao.toString())

        tamanho = len(acoes)
        indice = random.randint(0,(tamanho-1))
        tamanho = len(locais)
        indice2 = random.randint(0,(tamanho-1))
        acao = Acao(elenco.listaDeViloes[0], elenco.listaDeMocinhos[0], acoes[indice], locais[indice2])
        episodio.inserirAcao(acao.toString())

        tamanho = len(acoes)
        indice = random.randint(0,(tamanho-1))
        tamanho = len(locais)
        indice2 = random.randint(0,(tamanho-1))
        acao = Acao(elenco.listaDeViloes[1], elenco.listaDeMocinhos[1], acoes[indice], locais[indice2])
        episodio.inserirAcao(acao.toString())

        indice3 = elenco.getQuantidadeCoadjuvantes()

        while(indice3 > 0):
            
            tamanho = len(acoes)
            indice = random.randint(0,(tamanho-1))
            tamanho = len(locais)
            indice2 = random.randint(0,(tamanho-1))
            acao = Acao(elenco.listaDeCoadjuvantes[indice3 - 1], elenco.getAleatorio(), acoes[indice], locais[indice2])
            episodio.inserirAcao(acao.toString())
            indice3 -= 1
        
        temporada.append("Episódio " + str(numeroEpisodio + 1) + "\n" + episodio.toString())
        numeroEpisodio += 1

    arquivo = open("finais.txt", "r")
    finais = arquivo.readlines()

    tamanho = len(finais)
    indice = random.randint(0,(tamanho-1))
    final = Final(elenco.listaDeMocinhos[0], finais[indice])
    episodioFinal.inserirFinal(final.toString())

    tamanho = len(finais)
    indice = random.randint(0,(tamanho-1))
    final = Final(elenco.listaDeMocinhos[1], finais[indice])
    episodioFinal.inserirFinal(final.toString())

    tamanho = len(finais)
    indice = random.randint(0,(tamanho-1))
    final = Final(elenco.listaDeViloes[0], finais[indice])
    episodioFinal.inserirFinal(final.toString())

    tamanho = len(finais)
    indice = random.randint(0,(tamanho-1))
    final = Final(elenco.listaDeViloes[1], finais[indice])
    episodioFinal.inserirFinal(final.toString())

    temporada.append(episodioFinal.toString())

    return temporada

main()