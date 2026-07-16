print("Bem vindo a calculadora de numeros inteiros")
a=int(input("Digite o primeiro valor:"))
b=int(input("Digite o segundo valor:"))
escolha=input("Escolha a operaçao:")
soma = a+b
divisao= a/b
subtraçao= a-b
multiplicaçao= a*b
if escolha == "soma":
    print(soma)
    print("O valor da soma e:",soma)
elif escolha == "divisao":
    print(divisao)
    print("O valor da divisao e:",divisao)
elif escolha == "subtraçao":
    print(subtraçao)
    print("O valor da subtraçao e:",subtraçao)
elif escolha == "multiplicaçao":
    print(multiplicaçao)
    print("O valor da multiplicaçao e:",multiplicaçao)
else:
    print("Erro")
