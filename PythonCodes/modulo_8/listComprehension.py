# Compreensão de lista (List comprehension)
    # Mais simples de se escrever
    # Utilizado quando você precisa criar uma nova lista a partir de uma existente
    # [expressao for iten in itens]

frutas1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']
"""frutas2 = []

for iten in frutas1:
    if 'n' in iten:
        frutas2.append(iten)

print(frutas2)"""

# Porém, com o list comprehension conseguimos resumir o código acima em apenas uma linha:

frutas2 = [iten for iten in frutas1 if 'b' in iten]
print(frutas2)


# List comprehension (com números):

"""valores = []

for x in range(6):
    valores.append(x * 10)
print(valores)"""

# Porém, novamente, com o list comprehension conseguimos resumir o código acima em apenas uma linha:

valores = [x * 10 for x in range(6)]
print(valores)

