#Exercicio 4
#Solicitar um valor para a temperatura da água e indicar o seu estado físico (sólido, líquido ou gasoso). 

print("Exercicio 4")

temperatura = float(input("Qual a temperatura da água em graus Cº ? "))

if temperatura >= 0 and temperatura <100:
    print("A água está no estado líquido")
elif temperatura < 0:
    print("A água está no estado sólido")
else:
    print("A água está no estado gasoso")

print()
