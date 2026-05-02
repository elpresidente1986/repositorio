# Exercício 1
# Cria três funções distintas
#Invocar cada uma delas consoante a hora do dia
#

print("Exercício 1")

#Cria três funções distintas

def bom_dia():
    print ("Bom dia")

def boa_tarde():
    print ("Boa tarde")

def boa_noite():
    print ("Boa noite")

# Pedir ao utilizador para inserir uma hora

hora = int(input("Introduza uma hora entre 0 e 23: "))

#Verificar e chamar a função correspondente
if hora >= 6 and hora < 12:
    bom_dia()

elif hora >= 12 and hora < 20:
    boa_tarde()

elif hora >= 20 and hora <= 23:
    boa_noite()

elif hora >= 0 and hora < 6:
    boa_noite()

else:
    print("Hora introduxida é inválida. Introduza um valor entre 0 e 23.")

print()