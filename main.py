from colorama import Fore, Style, init
from jogo_forca import JogoForca

init(autoreset=True)

def menu():
    print(Fore.CYAN + Style.BRIGHT + "\n=== MENU PRINCIPAL ===" + Style.RESET_ALL)
    print("1. Jogar")
    print("2. Sair")
    return input(Fore.WHITE + "\nEscolha uma opção: " + Style.RESET_ALL).strip()

def main():
    print(Fore.GREEN + Style.BRIGHT + "Bem-vindo ao Jogo da Forca!" + Style.RESET_ALL)

    while True:
        opcao = menu()

        if opcao == "1":
            jogo = JogoForca()
            jogo.jogar()
        elif opcao == "2":
            print(Fore.CYAN + "\nAté mais! 👋" + Style.RESET_ALL)
            break
        else:
            print(Fore.YELLOW + "Opção inválida!")

if __name__ == "__main__":
    main()
