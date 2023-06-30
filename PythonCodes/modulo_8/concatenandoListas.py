numeros = [1, 2, 3, 4, 5, 6, 7]
letras = ['a', 'b', 'c', 'd', 'e']

numeros.extend(letras)

print(numeros)

itens = [['item1', 'item2'], ['item3', 'item4']]
print(itens[0][1]) # Pegando o item2 dentro da primeira lista

# Listas com Zip

cores = ['amarelo', 'verde', 'azul', 'vermelho']
valores = [10, 20, 30, 40]

duas_listas = zip(valores, cores)
print(list(duas_listas))

""" A função zip() é usada para juntar duas ou mais listas em uma única lista de tuplas, 
onde cada tupla contém um elemento de cada uma das listas fornecidas. 
A função zip() é muito útil quando precisamos percorrer duas ou mais listas simultaneamente, 
pois elimina a necessidade de usar loops aninhados. """

# Para saber mais funções > https://docs.python.org/3/library/functions.html