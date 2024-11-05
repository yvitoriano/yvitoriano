#estruturas condicionais 
# if e else 
# match case 

presenca = float(input("Digite a frequência do aluno: "))
nota = int(input("Digite a nota do aluno: "))

if presenca >= 75:
    if nota >=6:
       print("APROVADO")

    elif ( 3 > nota > 6):
       print("RECUPERAÇÃO")

    else:  
       print("REPROVOU")

else:
   print("Aluno Reprovou por falta")