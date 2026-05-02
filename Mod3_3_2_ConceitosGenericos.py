#Exercicio 2
#Pedir dois números inteiros
#Escrever todos os números entre eles por ordem crescente



print("Exercicio 2")

#Pedir o numero inicial e final

numero_1 = int(input("Introduz o numero inicial (menor): "))
numero_2 = int(input("Introduz o numero inicial (maior): "))

#Mostrar todos os números entre o inicial e final

for numero in range(numero_1, numero_2 +1):
    print (numero)

print()