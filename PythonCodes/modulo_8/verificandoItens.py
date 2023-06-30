# Verificando itens em uma lista

cor_cliente = input('Digite a cor desejada: ')
cores = ['roxo', 'amarelo', 'verde', 'vermelho', 'azul', 'preto']

if cor_cliente.lower() in cores:
    print('Temos essa cor em estoque')
else:
    print('Não temos essa cor em estoque')

# OBS: o lower() serve para mesmo que o cliente digite em letra maiuscula,
#o sistema vai interpretar em letras minusculas
#isso ajuda a não ocorrer erro devido o python ser case sensitive