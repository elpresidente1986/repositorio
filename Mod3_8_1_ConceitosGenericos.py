# Exercicio 1
# Pedir um número inteiro entre 1 e 120 
# Verificar se está entre 0 e 120
# Se não mostrar erro.

print("Exercicio 1")

try:
    # Pedir numero
    numero = int(input("Introduza um número inteiro entre 0 e 120: "))

    # Verificar se o numero está no intervalo
    if numero >= 0 and numero <= 120:
        print("Número válido.")
    else:
        print("Erro: O numero deve tem de ser entre 0 e 120.")

except ValueError:
    print("Erro: Tem de introduzir um número inteiro.")

print()