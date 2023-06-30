# comentário inline

print('olá python')

'''
multiplos comentários

'''

# aprendendo variaveis int floar e str:
x = str(2)
y = int(5)
z = float(10)

print(x)
print(y)
print(z)


# concatenação - Convertendo Numeros para String:
# opção 1:
nome = 'Mari'
idade = 27
cidade = 'São Paulo'

print(' A cliente ' + nome + ' tem ' + str(idade) + ' anos e mora na cidade de ' + cidade)

# opção 2:
nome2 = 'Lila'
idade2 = str(38)
cidade2 = 'Guarulhos'

print(' A cliente ' + nome2 + ' tem ' + idade2 + ' anos e mora na cidade de ' + cidade2)


# Adicionando Input:
nome3 = input('Digite o seu nome: ')
idade3 = input('Digite sua idade: ')
cidade3 = input('Digite a sua cidade: ')

print(' A cliente ' + nome3 + ' tem ' + str(idade3) + ' anos e mora na cidade de ' + cidade3)


# Para saber o tipo da variavel:
print(type(nome2))

