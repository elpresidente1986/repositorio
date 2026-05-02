# Exercício 2
# Ler dois números inteiros e indicar se são pares ou ímpares.

print("Exercício 2")

#Pedir dois números inteiros 

numero_1 = int(input("Introduz um numero: "))
numero_2 = int(input("Introduz um novo numero: "))

#Verificar se o primeiro número é par ou ímpar

if numero_1 % 2 == 0:
    print ("O primeiro número introduzido é par.") 
else:
    print("O primeiro número introduzido é ímpar.")

if numero_2 % 2 == 0:
    print ("O segundo número introduzido é par.") 
else:
    print("O segundo número introduzido é ímpar.")

print()