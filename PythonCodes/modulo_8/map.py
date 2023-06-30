# Map Function

    # O map vai aplicar uma função em cada item de uma lista de itens
    # Muito utilizado com listas
    # Aplicar uma função a um iterável (como uma list, tuple, dic) e retorna um objeto map que contém os resultados.
    # Documentação > https://docs.python.org/3/library/functions.html#map

lista1 = [1, 2, 3, 4]

"""def multiplicando(x):
    return x * 2

lista2 = map(multiplicando, lista1)
print(list(lista2))
# ou:
print(list(map(multiplicando, lista1)))"""


# Função Map com Lambda:
print(list(map(lambda x: x * 2, lista1)))