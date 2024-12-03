class Cachorro:
    def __init__(self, nome, idade, raca): 
        self.__nome = nome                    #Atributos
        self.__idade = idade
        self.raca = raca

    def get_nome(self):
        return self.__nome
    
    def get_idade(self):
        return self.__idade
    
    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    def set_idade(self, nova_idade):
        if idade > 0:
            self.__idade = nova_idade
    def andar(self):
        return print('O cachorro está andando')
    
    def latir(self):
        return print ('O cachorro está latindo')
    
    def comer(self):
        return print ('O cachorro está comendo')
    
cachorro1 = Cachorro("Simba", 4, "Vira_lata") 
print(f"O nome do cachorro é {cachorro1.get_nome()}, idade é {cachorro1.get_idade()} e a raça do cachorro é {cachorro1.raca}")

cachorro1.set_nome('Toronto')
