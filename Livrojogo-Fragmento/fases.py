from base import Fase
from util import JogoUtil
from inventario import Inventario

class FaseInicial(Fase):
    def __init__(self, nome_jogador, inventario):
        self.__nome_jogador = nome_jogador
        self.__inventario = inventario
        self.__descricao = f'''
                                ------------ O FRAGMENTO DA MENTE ------------

        Em um futuro onde a tecnologia permite explorar sonhos e realidades paralelas, {self.__nome_jogador}, 
        um(a) ex-agente do FBI, desperta em uma cidade distorcida, preso(a) entre a realidade e a mente de alguém.
        Com um bilhete misterioso instruindo-o(a) a encontrar o Fragmento da Mente antes que seja tarde, ele(a) 
        deve atravessar camadas da mente, enfrentar ilusões e descobrir sua verdadeira identidade. Suas escolhas 
        definirão o percurso e o desfecho da missão: conseguirá recuperar o artefato antes que caia em mãos erradas?

        ///// INÍCIO DA MISSÃO ///// 
        {self.__nome_jogador} está dentro de um prédio abandonado, onde acredita que o Fragmento da Mente está escondido.
          Um som ecoa pelos corredores. No meio de tanto suspense o que irá fazer?
        '''
        self.__opcoes = ["Seguir na direção do som", "Ignorar o som e continuar explorando", "Ver inventário"]

    def executar(self):
        print("\nFASE INICIAL\n")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return HomemMisterioso(self.__nome_jogador, self.__inventario)
        elif escolha == 1:
            return FinalOlacoInfinito(self.__nome_jogador)
        elif escolha == 2:
            self.__inventario.exibir_inventario()
            return self  # Volta para a mesma fase


class HomemMisterioso(Fase):
    def __init__(self, nome_jogador, inventario):
        self.__nome_jogador = nome_jogador
        self.__inventario = inventario
        self.__descricao = f'''Você encontra um homem misterioso que oferece informações valiosas, mas em troca quer algo de você.
        O homem misterioso pede que você aposte um item no Cassino para conseguir a localização exata do Fragmento. 
        Você aceita, {self.__nome_jogador}?'''
        self.__opcoes = ["Apostar Dado Dourado no cassino", "Não quero testar a sorte, vou fugir do Homem", "Ver inventário"]

    def executar(self):
        print("\nHOMEM MISTERIOSO\n")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:  # Apostar Dado Dourado
            if "Dado Dourado" not in self.__inventario.itens:
                # Adiciona o item ao inventário
                self.__inventario.adicionar_item("Dado Dourado")
            print("\nVocê usou o Dado Dourado no cassino!")
            return CofreTrancado(self.__nome_jogador, self.__inventario)
        elif escolha == 1:  # Fugir do homem
            return FinalAsimulacaoContinua(self.__nome_jogador)
        elif escolha == 2:  # Exibir inventário
            self.__inventario.exibir_inventario()
            return self  # Volta para a mesma fase


class CofreTrancado(Fase):
    def __init__(self, nome_jogador, inventario):
        self.__nome_jogador = nome_jogador
        self.__inventario = inventario
        self.__descricao = "Você encontrou o cofre trancado, mas para abri-lo precisa de uma chave codificada."
        self.__opcoes = ["Tentar abrir o cofre", "Continuar procurando por outro caminho", "Ver inventário"]

    def executar(self):
        print("\nCOFRE TRANCADO\n")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:  # Tentando abrir o cofre
            if "Chave Codificada" not in self.__inventario.itens:
                print("\nVocê encontrou a Chave Codificada e agora a adicionou ao seu inventário!")
                self.__inventario.adicionar_item("Chave Codificada")
            else:
                print("\nVocê já tem a Chave Codificada no inventário.")
            return Fragmento(self.__nome_jogador, self.__inventario)
        elif escolha == 1:  # Caminho sem usar o item
            print("\nVocê decide continuar procurando, mas sem a chave, nada é desbloqueado.")
            return FinalDesconexaoTotal(self.__nome_jogador)
        elif escolha == 2:  # Exibir inventário
            self.__inventario.exibir_inventario()
            return self  # Volta para a mesma fase


class Fragmento(Fase):
    def __init__(self, nome_jogador, inventario):
        self.__nome_jogador = nome_jogador
        self.__inventario = inventario
        self.__descricao = '''Você desbloqueia o cofre e segura o Fragmento. Agora que tem o Fragmento, sua mente 
        se enche de lembranças apagadas. Você percebe que foi enganado por Noctis e que sua identidade é uma mentira. 
        Você destrói o Fragmento?'''
        self.__opcoes = ["Destruir o Fragmento", "Buscar mais respostas", "Ver inventário"]

    def executar(self):
        print("\nFRAGMENTO\n")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return FinalMemoriaroubada(self.__nome_jogador)
        elif escolha == 1:
            return Resposta(self.__nome_jogador, self.__inventario)
        elif escolha == 2:
            self.__inventario.exibir_inventario()
            return self  # Volta para a mesma fase


class Resposta(Fase):
    def __init__(self, nome_jogador, inventario):
        self.__nome_jogador = nome_jogador
        self.__inventario = inventario
        self.__descricao = '''Você mantém o Fragmento e segue em busca de mais respostas. Após procurar muito 
        descobre que o Fragmento pode alterar a realidade à sua vontade. Você quer utiliza-lo para reescrever 
        seu passado e controlar o mundo ao seu redor?'''
        self.__opcoes = ["Mudar toda a minha História e manipular todos", "Resistir a tentação e buscar a resposta de tudo", "Ver inventário"]

    def executar(self):
        print("\nRESPOSTAS\n")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return FinalControleAbsoluto(self.__nome_jogador)
        elif escolha == 1:
            return FinalDespertarnaVerdade(self.__nome_jogador)
        elif escolha == 2:
            self.__inventario.exibir_inventario()
            return self  # Volta para a mesma fase


class FinalDespertarnaVerdade(Fase):
    def __init__(self, nome_jogador):
        self.__nome_jogador = nome_jogador

    def executar(self):
        print(f'''\n #### GAME OVER ####
              {self.__nome_jogador} encontra o Fragmento da Mente e descobre que toda a missão era um teste para determinar se ele(a) era digno(a) de conhecer a verdadeira natureza da realidade. Desperta no mundo real, mas nada parece exatamente como antes, e se sente estranho(a).''')
        return None


class FinalOlacoInfinito(Fase):
    def __init__(self, nome_jogador):
        self.__nome_jogador = nome_jogador

    def executar(self):
        print(f'''\n #### GAME OVER ####
               {self.__nome_jogador} falha em recuperar o Fragmento e percebe que está preso(a) dentro de um loop eterno, revivendo os mesmos eventos sem parar, pra sempre.''')
        return None


class FinalAsimulacaoContinua(Fase):
    def __init__(self, nome_jogador):
        self.__nome_jogador = nome_jogador

    def executar(self):
        print(f'''\n #### GAME OVER ####
              Mesmo ao recuperar o Fragmento, {self.__nome_jogador} percebe que sua realidade ainda é uma simulação, e que há um nível mais profundo que ele(a) nunca poderá acessar.''')
        return None


class FinalMemoriaroubada(Fase):
    def __init__(self, nome_jogador):
        self.__nome_jogador = nome_jogador

    def executar(self):
        print(f'''\n  #### GAME OVER ####   
              O artefato é destruído, mas com ele, todas as suas memórias desaparecem. Você nunca mais saberá quem foi, {self.__nome_jogador}!''')
        return None


class FinalControleAbsoluto(Fase):
    def __init__(self, nome_jogador):
        self.__nome_jogador = nome_jogador

    def executar(self):
        print(f'''\n #### GAME OVER ####
        {self.__nome_jogador} se torna um ser onipotente, capaz de manipular todas as camadas do sonho e da realidade, assume controle total sobre a realidade e passa a manipular o mundo como se fosse um deus, e se torna o verdadeiro vilão/vilã da história.''')
        return None


class FinalDesconexaoTotal(Fase):
    def __init__(self, nome_jogador):
        self.__nome_jogador = nome_jogador

    def executar(self):
        print(f'''\n #### GAME OVER ####
        {self.__nome_jogador} falha em distinguir a ilusão da realidade, enlouquecendo e se tornando apenas mais uma projeção no mundo dos sonhos, esquecido(a) para sempre.''')
        return None
