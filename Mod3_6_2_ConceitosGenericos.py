# Exercício 2
# Criar uma função chamada maior.
# A função recebe dois números e devolve o maior deles ou a igualdade.

#

print("Exercício 2")

# Função para verificar o maior número

def maior(numero_1, numero_2):
    if numero_1 > numero_2:
        return numero_1

    elif numero_2 > numero_1:
        return numero_2

    else:
        return "igualdade"

# Pedir dois numeros ao utilizador

numero_1 = int(input("Introduza o primeiro numero: "))
numero_2 = int(input("Introduza o segundo numero: "))

# Chamar a função e guardar

resultado = maior(numero_1, numero_2)

#Verificar o resultado

if resultado == "igualdade":
    print("Os números introduzidos são iguais.")
else:
    print("O maior número é:", resultado)


print()