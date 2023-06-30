# Crie uma lista de frutas a partir do input fornecido pelo usuário

frutas_usuario = input('Digite o nome das frutas separando por virgula: ')

frutas_lista = frutas_usuario.split(', ')

print(frutas_lista)

"""O split permite dividir o conteúdo da variável de acordo com as condições 
especificadas em cada parâmetro da função ou com os valores predefinidos por padrão. 
Você passa para ele um texto e um separador, e ele retorna para você um array, 
com o texto desse separador dividido em  cada posição. """