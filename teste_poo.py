class Aluno:
    def __init__(self,nome,matricula,idade,cpf):
        self.nome = nome
        self.__matricula = matricula
        self.idade = idade
        self.__cpf = cpf 

    def get_matricula(self):
        return self.__matricula
    
    def get_cpf(self):
        return self.__cpf
    
    def set_matricula(self, )
