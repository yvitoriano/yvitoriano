class Animal():
    def __init__(self, nome, peso):
        self.__nome = nome 
        self.__peso = peso

    def __str__(self):
        return 'Nome %s \n Peso: %f'%(self.__nome, self.__peso)
    
    def alimentar(self, comida):
        self.peso += comida
    
    #maior que 
    def __gt__(self, other):
        return self.__peso > other.__peso
    
    def __add__(self, other):
        return Animal(self.__nome + ' ' + other.__nome, self.__peso + other.__peso)
    @property
    def nome(self):
        print('Getter foi chamado')
        return self.nome 
    
    @nome.setter
    def nome (self, new_name):
        print('Setter foi chamado')
        if type(new_name) == type(str()):
            self.__nome = new_name
        else:
            print('O nome deve ser uma string')

#Leao = Animal('Leão',200)
#Tigre = Animal('Tigre', 150)
#animals = Leao + Tigre
#print(animals)

#Sobrecarga de operadores 
            
class Mamímefero(Animal):
    classe = 'Mamalia'

    def __str__(self):
        return super().__str__() + '\nMamífero\n'
    
class Ave(Animal):
    def __str__(self):
        return super().__str__() + "\nAve\n"
    
class Ave_Pequena(Ave):
    pass

Leao = Mamífero('Leao', 200)
Pica_pau = Ave("Pica pau" , 2)
print(Pica_pau)

