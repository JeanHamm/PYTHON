import random

print("-------- Gerador de Senhas --------\n\n")

abc= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

carcteres = int(input("Quantos caracteres a senha precisa: "))

senha = ''

for numero in range(0, carcteres):
    digito = str(random.randrange(0, 9))
    senha = senha + digito
        

   

print(f"\n\nSua senha é {senha}")
