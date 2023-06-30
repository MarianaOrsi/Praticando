# Listas são uteis para:
    # Armazenar mais de uma informação em variáveis
    # Manter a sequencia dos dados em uma variável
# doc listas: https://docs.python.org/3/tutorial/datastructures.html

cidades = ['São Paulo', 'Rio de Janeiro', 'Salvador', 'Goiania']

# Para alterar o dado de uma lista:
cidades[0] = 'Belo Horizonte' # Troca São Paulo por Belo Horizonte
cidades.append('Porto Alegre') # Coloca Porto Alegre ( append vai sempre no final da lista)
cidades.remove('Salvador') # Remove Salvador da lista
cidades.insert(3, 'Curitiba') # Coloca Curitiba na posição 3 da lista
cidades.sort() # Organiza por ordem alfabética

print(cidades)