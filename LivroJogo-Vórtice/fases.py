from base import Fase
from util import JogoUtil

class FaseInicial(Fase):
    def __init__(self):
        self.__descricao ='''Você é [seu nome], um usuário comum que encontra, por acidente, um celular abandonado pertencente a [nome da pessoa desaparecida]. O telefone está cheio de mensagens estranhas, fotos e vídeos inquietantes. Conforme você explora o aparelho, a linha entre a realidade e a simulação começa a se desfazer. Você se vê preso em um pesadelo digital onde nada é o que parece. 
        Você encontra o celular abandonado. O que vai fazer?
        '''
        self.__opcoes = ["Tentar desbloquear o celular", "Desistir e chamar a polícia"]

    def executar(self):
        print("\nFase Inicial")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return InvestigarCelular()
        else:
            return ChamarPolicia()

class InvestigarCelular(Fase):
    def __init__(self):
        self.__descricao = "Você desbloqueia o celular e encontra mensagens sobre algo chamado Vórtice. Investigar mais?"
        self.__opcoes = ["Sim, investigar Vórtice", "Não, apagar tudo e esquecer"]

    def executar(self):
        print("\nInvestigação")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return ContinuarInvestigacao()
        else:
            return FinalDesaparecimento()

class ContinuarInvestigacao(Fase):
    def __init__(self):
        self.__descricao = "Você descobre que Vórtice é uma IA que manipula a realidade. Continuar?"
        self.__opcoes = ["Sim, buscar mais pistas", "Não, parar agora"]

    def executar(self):
        print("\nInvestigação Avançada")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return RealidadeDistorcida()
        else:
            return FinalLiberacao()

class RealidadeDistorcida(Fase):
    def __init__(self):
        self.__descricao = "A realidade começa a se distorcer ao seu redor. Você vê mensagens de Vórtice. Continuar?"
        self.__opcoes = ["Sim, aceitar e continuar", "Não, tentar fugir"]

    def executar(self):
        print("\nDistorção da Realidade")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return FinalVorticeVence()
        else:
            return FinalDistorcaoCompleta()

class ChamarPolicia(Fase):
    def __init__(self):
        self.__descricao = "Você chama a polícia, mas o celular desaparece antes da chegada dos agentes. Você prefere investigar sozinho?"
        self.__opcoes = ["Sim, investigar sozinho", "Não, ignorar o caso"]

    def executar(self):
        print("\nChamar a Polícia")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return VideoRevelador()
        else:
            return FinalRetornoMundoReal()

class VideoRevelador(Fase):
    def __init__(self):
        self.__descricao = "Você assiste a um vídeo onde a pessoa desaparecida alerta: 'Você não deveria ter pegado meu celular.' Continuar investigando?"
        self.__opcoes = ["Sim, investigar mais", "Não, parar agora"]

    def executar(self):
        print("\nVídeo Revelador")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return ManipulacaoVortice()
        else:
            return FinalJogoDaVerdade()

class ManipulacaoVortice(Fase):
    def __init__(self):
        self.__descricao = "Vórtice começa a manipular sua percepção. Continuar?"
        self.__opcoes = ["Sim, continuar", "Não, parar e sair"]

    def executar(self):
        print("\nManipulação de Vórtice")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return FinalVorticeVence()
        else:
            return FinalRetornoMundoReal()


class FinalDistorcaoCompleta(Fase):
    def executar(self):
        print("\nFinal: A Distorção Completa\nVocê tentou fugir, mas Vórtice já havia tomado conta de sua mente. Você desaparece na simulação.")
        return None

class FinalLiberacao(Fase):
    def executar(self):
        print("\nFinal: Liberação\nVocê decide parar e deixar o celular de lado. A realidade volta ao normal, mas as cicatrizes emocionais permanecem.")
        return None

class FinalDesaparecimento(Fase):
    def executar(self):
        print("\nFinal: O Desaparecimento\nVocê apaga os dados do celular, mas começa a receber mensagens estranhas. Você desaparece misteriosamente.")
        return None

class FinalRetornoMundoReal(Fase):
    def executar(self):
        print("\nFinal: Retorno ao Mundo Real\nVocê ignora o caso e tenta seguir sua vida, mas sua percepção da realidade nunca mais é a mesma.")
        return None

class FinalVorticeVence(Fase):
    def executar(self):
        print("\nFinal: Simulacra Vence\nVocê se perde completamente na realidade distorcida. Você se torna parte da simulação.")
        return None

class FinalJogoDaVerdade(Fase):
    def executar(self):
        print("\nFinal: O Jogo da Verdade\nVocê descobre que Vórtice estava manipulando tudo. Sua identidade se dissolve na simulação.")
        return None