# Exercício 2
# Pedir dois números inteiros e indicar quantos números pares há entre eles.

print("Exercício 2")

#Pedir numero inicial e final

numero_inicial = int(input("Introduza o número inicial: "))
numero_final = int(input("Introduza o número final: "))

# Contar os números pares
contador_pares = 0

# Percorrer todos os números entre o inicial e o final
for numero in range(numero_inicial, numero_final + 1):

    # Verificar se o número é par
    if numero % 2 == 0:
        contador_pares = contador_pares + 1

# Mostrar o resultado
print("Entre", numero_inicial, "e", numero_final, "há", contador_pares, "números pares.")

print()