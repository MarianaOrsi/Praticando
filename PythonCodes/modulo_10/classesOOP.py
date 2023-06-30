# OOP (Object-Oriented Programming)
    # Utilizadas para criar objetos (instances)
    # Objetos são partes dentro de uma classe (instancias)
    # O nome da classe sempre deve ser com a primeira letra maiuscula
    # Classes são utilizadas para agrupar dados e funções, podendo reutilizar
    # Exemplo:
        # Class: Frutas
        # Objects: Abacate, Banana, Morango...

# Criando a classe construtora
class Funcionarios:
    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento

# Criando Objeto
usuario1 = Funcionarios('Elena', 'Cabral', '07/07/1977')
usuario2 = Funcionarios('Carol', 'Silva', '10/08/1987')
usuario3 = Funcionarios('Alex', 'Santos', '15/09/1997')

print(usuario1.nome)
print(usuario2.data_nascimento)
print(usuario3.sobrenome)

"""# Criando os parametros do usuário1
usuario1.nome = 'Elena'
usuario1.sobrenome = 'Cabral'
data_nascimento = '07/07/1977'

# Print
print(usuario1.nome)


# Criando os parametros do usuário2
usuario2.nome = 'Carol'
usuario2.sobrenome = 'Silva'
usuario2.data_nascimento = '10/07/1987'"""