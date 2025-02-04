from base import Fase
from utilidades import JogoUtil

class FaseInicial(Fase):
    def __init__(self):
        self.__descricao = '''A aventura começa! 
        Ao chegar no hospital você entra em busca de um medicamento.
        você encontra uma recepçãp do lado esquerdo, mas a porta está 
        trancada. Tem outro caminho no lado direito que leva a uma ala 
        psiquiátrica. Qual caminho você vain  escolher'''
        self.__opcoes = ["Seguir pela esquerda", "Seguir pela direita"]
    
    def executar(self):
        print("\nFase Inicial")
        print(self.__descricao)
        JogoUtil.exibir_opções(self.__opcoes)
        escolha = JogoUtil.fazer_escolher(self.__opcoes)

        if escolha == 0:
            return Parte2()
        else:
            return Parte3()
   
class Parte2(fase):
    def __init__(self):
        self.__descricao = '''Você encontra uma recepção porém está trancada'''
        self.__opcoes = ["entrar pelo duto de ar", "Seguir para a ala cirúrgica"]
    
    def executar(self):
        print("\nFase Inicial")
        print(self.__descricao)
        JogoUtil.exibir_opções(self.__opcoes)
        escolha = JogoUtil.fazer_escolher(self.__opcoes)

        if escolha == 0:
            return Parte2()
        else:
            return Parte4()
        
class Parte3(fase):
    def __init__(self):
        self.__descricao = '''Você encontra um caminho que leva a 
        ala psiquiátrica'''
        self.__opcoes = ["Porta1", "Porta2"]
    
    def executar(self):
        print("\nFase Inicial")
        print(self.__descricao)
        JogoUtil.exibir_opções(self.__opcoes)
        escolha = JogoUtil.fazer_escolher(self.__opcoes)

        if escolha == 0:
            return Parte6()
        else:
            return Parte7()

class Parte4(fase):
    
    def executar(self):
        print('''\nVocê tenta entrar, mas nâo consegue
              você tenta entrar pelo duto de ar 
              mas não aguenta seu peso. Você cai e morre!''')
    
        return None
    
class Parte5(fase):
    
    def executar(self):
        print('''\n Você se depara com diversos experimentos 
              com pessoas. lá você cai em uma armadilha e morre!''')
    
        return None

