# Exercício 1
# Pedir número e escrever a tabuada desse número entre 1 e 10.

print("Exercício 1")

#Pedir numero 

numero_1 = int(input("Introduz o numero: "))

# Mostrar a tabuada do número

for i in range(1, 11):
    resultado = numero_1 * i
    print(numero_1, "x", i, "=", resultado)

print()