nome=input("insira seu nome")
tamanho=len(nome)
if tamanho < 5:
    sobre=input('insira seu sobrenome')
    tamanho2=len(sobre)
    tamanho3=tamanho+tamanho2
    print(nome, sobre, tamanho3)
else:
    print(nome,tamanho)