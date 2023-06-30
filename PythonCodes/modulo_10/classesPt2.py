from datetime import datetime
class Funcionarios:
    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = int(ano_nascimento)

    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome

    def idade_funcionario(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = int(ano_atual - self.ano_nascimento)
        return self.ano_nascimento


# Criando Objeto
usuario1 = Funcionarios('Elena', 'Cabral', '1977')
usuario2 = Funcionarios('Carol', 'Silva', '1987')
usuario3 = Funcionarios('Alex', 'Santos', '1997')

#print(usuario1.ano_nascimento)
# Ou pode ser feito assim:
print(Funcionarios.idade_funcionario(usuario1))