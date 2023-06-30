from sys import getsizeof

# Generation Expression
    # Uma forma mais rápida para listas, dicionários e etc
    # Menos memória alocada
    # Valores em bytes

numeros = [x * 10 for x in range(10)] # de 10 em 10 por 10 vezes: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print(numeros)
print(getsizeof(numeros)) # para saber quantos bytes está consumindo na memória