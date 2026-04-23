from colorama import Fore, Style, init

init(autoreset=True)

MAX_ERROS = 7

def exibir_tentativas(erros):
    restantes = MAX_ERROS - erros
    print(Fore.YELLOW + f"\nTentativas restantes: {restantes}/{MAX_ERROS}")

def exibir_palavra(palavra, letras_certas):
    exibicao = ""
    for letra in palavra:
        if letra in letras_certas:
            exibicao += Fore.GREEN + letra + " "
        else:
            exibicao += Fore.WHITE + "_ "
    print("\n" + exibicao + Style.RESET_ALL + "\n")

def exibir_letras_erradas(letras_erradas):
    if letras_erradas:
        print(Fore.RED + "Letras erradas: " + ", ".join(sorted(letras_erradas)))

def mensagem_vitoria():
    print(Fore.GREEN + Style.BRIGHT + "\nParabéns! Você acertou a palavra!" + Style.RESET_ALL)

def mensagem_derrota(palavra):
    print(Fore.RED + Style.BRIGHT + f"\nGame over! A palavra era: {palavra.upper()}" + Style.RESET_ALL)
