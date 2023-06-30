# Set (Listas)
    # Não utiliza index (fora de ordem)
    # Evita itens duplicados
    # Similar a listas

lista01 = [10, 20, 30, 40, 50]
lista02 = [10, 20, 60, 70]

num1 = set(lista01)
num2 = set(lista02)

print(num1 | num2) # Union > Unifica as duas listas (fora de ordem) retirando os repetidos
print(num1 - num2) # Difference > mostra somente os valores da lista01 que não estão na lista02, no caso {40, 50, 30}
print(num1 ^ num2) # Symmetric Difference > retira todos os duplicados nas duas listas
print(num1 & num2) # And > mostra o que é duplicado nas duas listas, no caso {10, 20}
print(len(num1)) # O len mostra quantos itens a lista possui


set1 = {1, 2, 3, 4, 5, 6} # o Set pode ser criado diretamente usando { }
set1.update([7, 8, 9, 10])
set1.discard(9)

print(set1)

setStr1 = {'a', 'b', 'c'}
setStr2 = {'a', 'd', 'e'}
setStr3 = {'c', 'd', 'f'}

setStr4 = setStr1.difference(setStr3)
print(setStr4)