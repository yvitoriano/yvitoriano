#Tuplas
#tupla = (1, 2, 3, 'Tiago', 10.5, ['numero 1', 'numero 2'])

#tupla = tupla + ('outro valor', 'outro valor 2')

#print(tupla)


#Dicionário : conjunto de chave e valor 
#Pessoa = { 'Nome': 'Yasmin', 'idade':16, 'endereco': { 'rua':'Rua arco-íris', 'numero': 123, 'bairro': 'flores'}}

#Pessoa['endereco']['bairro'] = 'flores'
#Pessoa['idade'] = 30
#print(Pessoa['Nome'])

#clear ()
#get()

Restaurante = {'Menu':
                {'Comidas':{
                    'Entrada': 'Torradinhas',
                    'Prato Principal': 'Macarrão',
                    'Sobremesa': 'Sorvete'}, 
                 'Bebidas':{
                     'Destilados': 'Rum',
                     'Sucos': {
                        'Com leite': 'Goiaba',
                        'Sem leite': 'Laranja'}
                    }
                } 
              }


for i in Restaurante:
    print(i['Comidas'])