import random

def gerar_soma():
    num1 = random.randint(5, 20)
    num2 = random.randint(5, 20)
    resposta_correta = num1 + num2

    print(f"Qual é a soma de {num1} e {num2}?")
    while True:
        try:
            resposta_usuario = int(input("Sua resposta: "))
            break
        except ValueError:
            print("insira um número inteiro.")

    verificar_resposta(resposta_usuario, resposta_correta)

def gerar_subtracao():
    num1 = random.randint(25, 50)
    num2 = random.randint(1, 25)
    resposta_correta = num1 - num2

    print(f"Qual é a subtração de {num1} - {num2}?")
    while True:
        try:
            resposta_usuario = int(input("Sua resposta: "))
            break
        except ValueError:
            print("insira um número inteiro.")

    verificar_resposta(resposta_usuario, resposta_correta)

def verificar_resposta(resposta_usuario, resposta_correta):
    if resposta_usuario == resposta_correta:
        print("Resposta correta!")
    else:
        print(f"A resposta está incorreta! A resposta correta é {resposta_correta}.")

def menu():
    while True:
        print("\nMenu:")
        print("1 - Soma de dois números")
        print("2 - Subtração de dois números")
        print("0 - Sair")

        try:
            opcao = int(input("Escolha uma opção: "))

            if opcao == 1:
                gerar_soma()
            elif opcao == 2:
                gerar_subtracao()
            elif opcao == 0:
                print("Saindo do programa...")
                break
            else:
                print("Opção inválida! escolha uma opção válida.")
        except ValueError:
            print("Entrada inválida! insira um número inteiro.")

if __name__ == "__main__":
    menu()