#Exercicio 3
#Pedir um número inteiro e determinar se esse número é primo.

#Definição: Número primo é um número natural maior que 1, divisível apenas por 1 e por ele mesmo.

print("Exercicio 3")

# Pedir um número inteiro ao utilizador

numero = int(input("Introduz um número: "))

# Começamos por assumir que o número é primo
primo = True

# Numeros menores que 2 nao sao primos
if numero < 2:
    primo = False
else:
    # Verificar se existe algum divisor entre 2 e o número anterior
    for divisor in range(2, numero):
        if numero % divisor == 0:
            primo = False

# Mostrar o resultado
if primo:
    print("O número introduzido é primo.")
else:
    print("O número introduzido não é primo.")

print()