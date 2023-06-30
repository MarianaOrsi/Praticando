# Unpacking Lists

produtos = ['arroz', 'feijão', 'laranja', 'banana', 'maça', 'uva']

item1, item2, item3, *outros = produtos

print(item1)
print(item2)
print(item3)
print(outros)
