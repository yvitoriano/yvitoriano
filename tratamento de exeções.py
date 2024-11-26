#Tratamento de exeções
import sys
#L = [1,2,0,'a']

#for i in L:
 #   try:
 #       print(1/i)
 #   except ZeroDivisionError:
 #       print('Não é possivel dividir 1 por', i)
#        print(sys.exc_info()[0])
  #  except TypeError:
   #     print('Não é possível dividir um número por uma string')
    #    print(sys.exc_info()[0])

def usuario(nome, idade):
    # Não é necessário pedir o nome e idade aqui, porque já são passados como argumentos
    try:
        if nome.endswith('a') and idade < 18:
            raise ValueError('Erro: Acesso negado')
        else:
            print(f'Bem-vindo, {nome}!')
    except ValueError as erro:
        print(erro)

# Chama a função e passa os argumentos diretamente
nome = str(input('Insira seu nome: '))
idade = int(input('Insira sua idade: '))

usuario(nome, idade)  # Aqui chamamos a função com os argumentos nome e idade

