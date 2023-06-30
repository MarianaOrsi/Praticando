# Função Filter
    # Muito utilizado com listas
    # Aplicar uma função a um iterável (como uma list, tuple, dic)
    # Documentação > https://docs.python.org/3/library/functions.html#filter

valores = [10, 12, 34, 44, 57]

def remover20(x):
    return x > 20

print(list(filter(remover20, valores)))
# ou com lambda:
print(list(filter(lambda x: x > 20, valores)))