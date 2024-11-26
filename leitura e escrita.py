#Leitura e escrita de arquivos 

#open('nome do arquivo','modo')

#criação de PDF
#escreve = open('new.txt','w')
#escreve.write('Escrever qualquer coiaa no arquivo')
#escreve.clone()

ler = open('new.txt','r')
x = ler.read()
print(x)
ler.close()
ler = open('new.text','r')
for i in ler:
    print(i, end='')

apensar = open('new.txt', 'a')
apensar.write('Texto ................')
apensar.close()
ler = open('new.txt')
close()


