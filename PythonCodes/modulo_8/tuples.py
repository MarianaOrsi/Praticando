# Tuples
    # Tuples são como as listas, servem para armazenar mais de uma informação e manter a sequencia dos dados,
    # porém, não podem ser alteradas. Uma lista Tuple é imutável, não podemos alterar, incluir ou excluir dados.
    # Além disso, uma tuple é criada com ( ) ao invés de [ ]

# Veja o exemplo:

cores_list = ['amarelo', 'verde', 'azul', 'vermelho']
cores_tuple = ('amarelo', 'verde', 'azul', 'vermelho')

cores_list.append('roxo')
# cores_tuple.append('rosa') # Error: 'tuple' object has no attribute 'append'
print(cores_tuple)

# Se caso for criar um código onde os itens nunca vão mudar, utilize uma tuple para criar
# Se caso for criar um código onde os itens vão mudar, utilize uma lista