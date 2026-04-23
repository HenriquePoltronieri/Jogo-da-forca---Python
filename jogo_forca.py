from utils import (
    exibir_tentativas, exibir_palavra, exibir_letras_erradas,
    mensagem_vitoria, mensagem_derrota, MAX_ERROS
)
from palavras import sortear_palavra
from colorama import Fore, Style

class JogoForca:
    def __init__(self):
        self.palavra = sortear_palavra()
        self.letras_certas = set()
        self.letras_erradas = set()
        self.erros = 0

    def ja_tentou(self, letra):
        return letra in self.letras_certas or letra in self.letras_erradas

    def adivinhar(self, letra):
        if letra in self.palavra:
            self.letras_certas.add(letra)
            return True
        else:
            self.letras_erradas.add(letra)
            self.erros += 1
            return False

    def venceu(self):
        return all(letra in self.letras_certas for letra in self.palavra)

    def perdeu(self):
        return self.erros >= MAX_ERROS

    def exibir_estado(self):
        exibir_tentativas(self.erros)
        exibir_palavra(self.palavra, self.letras_certas)
        exibir_letras_erradas(self.letras_erradas)

    def jogar(self):
        print(Fore.CYAN + Style.BRIGHT + "\n=== JOGO DA FORCA ===" + Style.RESET_ALL)

        while not self.venceu() and not self.perdeu():
            self.exibir_estado()

            letra = input(Fore.WHITE + "\nDigite uma letra: " + Style.RESET_ALL).strip().lower()

            if len(letra) != 1 or not letra.isalpha():
                print(Fore.YELLOW + "Digite apenas uma letra válida!")
                continue

            if self.ja_tentou(letra):
                print(Fore.YELLOW + "Você já tentou essa letra!")
                continue

            if self.adivinhar(letra):
                print(Fore.GREEN + "Acertou!" + Style.RESET_ALL)
            else:
                print(Fore.RED + "Errou!" + Style.RESET_ALL)

        self.exibir_estado()

        if self.venceu():
            mensagem_vitoria()
        else:
            mensagem_derrota(self.palavra)
