# Lambda Function
    # É uma função (pequena) sem nome
    # Pode ter vários argumentos mas somente uma expressão
    # Muito utilizada dentro de outras funções
    # Código mais 'clean'

somar10 = lambda x , y: x + y + 10 # soma 2 com 4 e com 10 = 16
print(somar10(2, 4))

# Lambda dentro de uma função:

def somar(x):
    func2 = lambda argumento: x + 10
    return func2(x) * 4
print(somar(5))


"""Funções lambda são uma ferramenta poderosa na programação Python, que permite a criação de funções anônimas, 
ou seja, sem necessidade de dar um nome para elas. Elas são úteis quando precisamos de uma função simples, 
que será utilizada apenas uma vez e não precisa ser reutilizada em outro lugar do código"""