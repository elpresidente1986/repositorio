#Exercicio 1
#Pedir duas avaliações (entre 0 e 20) 
#calcular a média deles
#Caso sejam iguais, indicar também a igualdade.


print("Exercicio 1")

#Pedir duas avaliações

avaliacao_1 = float(input("Introduz a primeira nota entre 0 e 20: "))
avaliacao_2 = float(input("Introduz a primeira nota entre 0 e 20: "))

#Analisar se as notas estão entre 0 e 20

if avaliacao_1 >= 0 and avaliacao_1 <= 20 and avaliacao_2 >= 0 and avaliacao_2 <= 20:

    #calcular a média deles

    media = (avaliacao_1 + avaliacao_2) / 2

    #Mostrar o resultado

    print ("A média das notas é:", media)

    #Verificar igualdade das notas 

    if avaliacao_1 == avaliacao_2:
        print ("As notas de avaliação são iguais.")

else:

    print("As notas devem ser entre 0 e 20.")

print()