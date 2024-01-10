"""
Este módulo contém as configurações da aplicação Flask.
"""

import os

DEBUG = True

# Restante da configuração ...

# Uma forma segura de gerar uma SECRET_KEY é através do os.urandom
SECRET_KEY = os.urandom(24)

# Ou, você pode definir uma string fixa (não recomendado para produção):
# SECRET_KEY = 'minha_chave_secreta_super_secreta'

# Nova linha no final do arquivo
