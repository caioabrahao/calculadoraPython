def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


print("Calculadora em Python 0.1")

print("Escolha sua operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
print("5. Sair")

escolha = input("Escolha:")


while "0" < escolha < "5":

    if escolha == "1":
        val1 = float(input("Primeiro valor:"))
        val2 = float(input("Segundo valor:"))
        print(val1, "+", val2, "=", add(val1, val2))
        exit()

    if escolha == "2":
        val1 = float(input("Primeiro valor:"))
        val2 = float(input("Segundo valor:"))
        print(val1, "-", val2, "=", subtract(val1, val2))
        exit()

    elif escolha == "3":
        val1 = float(input("Primeiro valor:"))
        val2 = float(input("Segundo valor:"))
        print(val1, "*", val2, "=", multiply(val1, val2))
        exit()

    elif escolha == "4":
        val1 = float(input("Primeiro valor:"))
        val2 = float(input("Segundo valor:"))
        while val2 <= 0:
            if val2 <= 0:
                print("Não é possível dividir por 0")
                val2 = float(input("Segundo valor:"))
        print(val1, "/", val2, "=", divide(val1, val2))
        exit()

    elif escolha == "5":
        print("\n Saindo...")
        exit()

else:
    print("Opção Inválida! Tente novamente.")


