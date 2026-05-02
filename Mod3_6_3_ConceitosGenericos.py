# Exercício 3
# Criar uma função chamada tabuada.
# Pedir número e escrever a tabuada desse número entre 1 e 10.

print("Exercício 3")

# Função para mostrar a tabuada do número
def tabuada(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(numero, "x", i, "=", resultado)

# Pedir número
numero_1 = int(input("Introduz o número: "))

# Chamar a função
tabuada(numero_1)

print()