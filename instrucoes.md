Jogo da forca:

Adivinhar uma palavra letra por letra
Tem número limitado de erros

Estrutura

forca/
├── main.py
├── jogo_forca.py
├── palavras.py
├── utils.py
├── requirements.txt
└── venv/


main.py
inicia o jogo
Biblioteca essencial: Random
Sugestão: 
pip install colorama unidecode
from colorama import Fore, Style
print(Fore.GREEN + "Acertou!" + Style.RESET_ALL)
print(Fore.RED + "Errou!" + Style.RESET_ALL)

Remover acento
from unidecode import unidecode
palavra = "ação"
print(unidecode(palavra)) # vira "acao"

teste antes:
from colorama import Fore

print(Fore.GREEN + "Funcionou!")



