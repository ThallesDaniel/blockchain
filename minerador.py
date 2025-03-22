import hashlib
import random

'''
Código para minerar um bloco de dados, este codigo não funciona de fato,
é um protótipo inicial para entender a lógica de mineração de blocos.
'''

# Função para calcular o hash
def sha256(data):
    return hashlib.sha256(data.encode()).hexdigest()

# Função para verificar se o hash é válido
def is_valid_hash(hash, difficulty):
    return hash[:difficulty] == '0' * difficulty

# Definir a dificuldade
difficulty = 20

# Gerar um bloco de dados
block_data = "Dados do bloco" + str(random.randint(1, 10000))

# Gerar um nonce inicial
nonce = 0

# Loop para encontrar um hash válido
while not is_valid_hash(sha256(block_data + str(nonce)), difficulty):
    nonce += 1

# Imprimir o hash e o nonce encontrados
print("Hash:", sha256(block_data + str(nonce)))
print("Nonce:", nonce)
