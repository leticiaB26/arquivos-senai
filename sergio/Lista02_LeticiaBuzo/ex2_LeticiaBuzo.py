import random

def definir_num_secreto():
    """Solicita ao usuário para escolher um número baixo e um número alto e gera um número aleatório entre esses dois valores."""
    while True:
        try:
            baixo = int(input("Escolha um número baixo: "))
            alto = int(input("Escolha um número alto: "))
            if baixo >= alto:
                print("O número baixo deve ser menor que o número alto. Tente novamente.")
            else:
                num_secreto = random.randint(baixo, alto)
                return num_secreto
        except ValueError:
            print("Por favor, insira apenas números inteiros.")

def pedir_palpite():
    """Dá a instrução 'Estou pensando em um número...' e pede ao usuário para adivinhar o número."""
    print("Estou pensando em um número...")
    while True:
        try:
            palpite = int(input("Qual é o seu palpite? "))
            return palpite
        except ValueError:
            print("Por favor, insira apenas números inteiros.")

def verificar_palpite(num_secreto):
    """Verifica se o palpite do usuário é o mesmo que o num_secreto e fornece feedback até o palpite estar correto."""
    while True:
        palpite = pedir_palpite()
        if palpite < num_secreto:
            print("Seu palpite está muito baixo. Tente novamente.")
        elif palpite > num_secreto:
            print("Seu palpite está muito alto. Tente novamente.")
        else:
            print("Parabéns, você acertou!")
            break

def main():
    """Função principal que chama as funções auxiliares para jogar o jogo de adivinhação."""
    num_secreto = definir_num_secreto()
    verificar_palpite(num_secreto)

if __name__ == "__main__":
    main()