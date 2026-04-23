import random
from unidecode import unidecode

PALAVRAS = [
    "python", "computador", "teclado", "monitor", "internet",
    "algoritmo", "variavel", "funcao", "classe", "objeto",
    "programa", "software", "hardware", "rede", "sistema",
    "banco", "dados", "arquivo", "modulo", "biblioteca",
]

def sortear_palavra():
    palavra = random.choice(PALAVRAS)
    return unidecode(palavra).lower()
