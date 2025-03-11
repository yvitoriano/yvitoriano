from fases import FaseInicial
from inventario import Inventario
class Jogo:
    def __init__(self):
        self.__nome_jogador = input("Qual o seu nome, jogador? ")  # Nome do jogador
        self.__inventario = Inventario()  # Criando o inventário
        self.__fase_atual = FaseInicial(self.__nome_jogador, self.__inventario)

    def jogar(self):
        while self.__fase_atual:
            self.__fase_atual = self.__fase_atual.executar()
            if not self.__fase_atual:
                jogar_novamente = input("\nQuer jogar novamente? (sim/nao)").strip().lower()
                if jogar_novamente == "sim":
                    self.__inventario = Inventario()  # Reiniciar inventário
                    self.__fase_atual = FaseInicial(self.__nome_jogador, self.__inventario)

if __name__ == "__main__":
    jogo = Jogo()
    jogo.jogar()
