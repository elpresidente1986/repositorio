# Exercicio 1
# Pedir dois números inteiros
# Fazer a divisão dos valores
# Verificar o erro de divisão por zero

print("Exercicio 2")

try:
    # Pedir numero
    numero_1 = int(input("Introduza o primeiro numero: "))
    numero_2 = int(input("Introduza o segundo numero: "))

    # Calcular a divisão
    resultado = numero_1 / numero_2

    # Mostrar o resultado
    print("O resultado é:", resultado)

except:
    print("Erro: Dados invalidos.")

print()