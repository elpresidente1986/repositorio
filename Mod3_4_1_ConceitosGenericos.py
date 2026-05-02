#Exercicio 1
#Pedir dois números inteiros 
#indicar o maior deles
#Caso sejam iguais, indicar também a igualdade.


print("Exercicio 1")

#Pedir dois números inteiros 

numero_1 = int(input("Introduz o primeiro numero: "))
numero_2 = int(input("Introduz o segundo numero: "))

#Verificar o maior deles

if numero_1 > numero_2:
    print ("O maior numero é: ", numero_1) 

elif numero_2 > numero_1:
    print ("O maior numero é: ", numero_2) 

else:

    print ("Os numeros são iguais") 

print()