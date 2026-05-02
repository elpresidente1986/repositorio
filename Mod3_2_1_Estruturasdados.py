#Exercicio 1
#Cria uma lista com 5 notas.
# Aceder ao primeiro e último elemento.
# Adicionar um valor à lista.
# Remover um elemento específico.
# Calcular a média dos valores.

print("Exercicio 1")

#Lista com 5 notas

notas = [12,15,18,10,20]

# Aceder ao primeiro e último elemento.

nota_primeira = notas[0]

nota_ultima = notas[-1]

print("Lista inicial:", notas)
print("Primeira nota:", nota_primeira)
print("Última nota:", nota_ultima)

# Adicionar um valor à lista
notas.append(16)

print( "Segue a listagem com a nova nota inserida:", notas)

# Remover um elemento específico da lista
notas.remove(10)

print("Lista após remover a nota:", notas)

# Calcular a média dos valores
media = sum(notas) / len(notas)

print("Média das notas:", media)

print()