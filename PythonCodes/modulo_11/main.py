#import funcoes
"""funcoes.somar()
funcoes.multi()"""

from funcoes import somar, multi
somar()
multi()

"""

import funcoes > importa todas as funções dentro do arquivo funcoes.py

from funcoes import somar, multi > importa somente as funções que forem mencionadas após o import, 
neste caso, está importando as funções somar e multi do arquivo funcoes.py

"""

from items.cadastro import cliente
cliente()
# Importa o cadastro.py que está no pacote items
# O arquivo __init__.py é apenas para mostrar ao python que a pasta items é um package