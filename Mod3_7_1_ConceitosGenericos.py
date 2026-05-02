# Exercício 1
# Criar uma classe
# A classe deve conter: nome, numero e nota.
# Mostrar os dados de um aluno numa disciplina.

print("Exercício 1")


# Criar a classe
class aluno:
    def __init__(self, nome, numero, nota):
        self.nome = nome
        self.numero = numero
        self.nota = nota

    def __str__(self):
        return f"Nome: {self.nome}\nNúmero: {self.numero}\nNota: {self.nota}"

# Pedir os dados ao utilizador
nome = input("Introduz o nome do aluno: ")
numero = int(input("Introduz o número do aluno: "))
nota = float(input("Introduz a nota do aluno: "))

# Criar um objeto
aluno_1 = aluno(nome, numero, nota)

# Mostrar os dados
print()
print("Dados do aluno:")
print(aluno_1)

print()