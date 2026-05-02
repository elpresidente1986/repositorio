# Exercício 2
# Criar uma classe
# A  classe de nome Base, a qual contém como variáveis o comprimento e a largura
# Método para calcular a área do retângulo

print("Exercício 2")


# Criar a classe
class Base:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def calcular_area(self):
        return self.comprimento * self.largura

# Pedir os dados 
comprimento = float(input("Introduza o comprimento: "))
largura = float(input("Introduza a largura: "))

# Criar um objeto
retangulo = Base(comprimento, largura)

# Calcular a área
area = retangulo.calcular_area()

# Mostrar os dados
print()
print("A área do retângulo é:", area)

print()