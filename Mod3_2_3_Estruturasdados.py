# Exercício 3
# Declarar uma lista com os meses do ano.
# Imprimir no ecrã os meses que têm apenas 30 dias.

print("Exercicio 3")

# lista com os meses do ano

meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"] 

#lista dos meses com 30 dias

meses_30 = [meses[3], meses[5], meses[8], meses[10]]

print(f"Os meses que têm 30 dias são: {', '.join(meses_30)}.")

print()