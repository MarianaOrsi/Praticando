# Dicionários
    # Utiliza o index no formato de Keys e Values
    # Aceita strings, integer, floar, boolean...

#         Key    Value
#aluno = {'nome': 'Ana', 'idade': 16, 'nota_final': 'A', 'aprovação': True}
#print(aluno['nome'])

# Atualizando Dicionários:

#aluno.update({'nome': 'Alex', 'idade': 15, 'nota_final': 'B'}) # Atualizando Aluno
#print(aluno)

#aluno.update({'endereco': 'Rua da Alegria, nº 07'}) # Incluindo endereço do Aluno
#print(aluno.get('sobrenome', 'Esse dado não existe')) # Retorna uma mensagem para um dado que não existe
#del aluno['idade'] # Remove a idade do dicionário
#print(aluno)

# For looping dentro de Dicionários:

#for keys, values in aluno.items():
 #   print(keys, values)

# Criando Listas dentro de Dicionários:

aluno02 = {
    'nome': 'Marina',
    'idade': 16,
    'nota_final': 'A',
    'aprovação': True,
    'materias': ['Inglês', 'Biologia', 'Artes']
}
print(aluno02.keys())
print(aluno02.values())
print(aluno02.items())

