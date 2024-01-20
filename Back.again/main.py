print("Bem vindo a calculadora\n\n")
duracao = 1
while(duracao == 1):
        print("Qual será o tipo de calculo?\n\n")
        print("Multiplicação - 1\nDivisão - 2\nSoma - 3\nSubtração - 3")
        print("\n")

        operacao = int(input("Qual sua escolha: "))

        while(operacao == str or operacao < 0 or operacao > 4 ):
                operacao = int(input())

        n1 = int(input("Digita o 1° numero: "))
        n2 = int(input("Digita o 2° numero: "))

        if(operacao == 1):
                retorno =  n1 * n2
                print(f"\nSeu numero é {retorno}")
        elif(operacao == 2):
                retorno = n1 / n2
                print(f"\nSeu numero é {retorno}")
        elif(operacao == 3):
                retorno =  n1 + n2
                print(f"\nSeu numero é {retorno}")
        elif(operacao == 4):
                retorno =  n1 - n2    
                print(f"\nSeu numero é {retorno}")
        else:
                print("\nNumero não valido")

        print("\n\nQuer fazer um novo calculo?")
        duracao = int(input("Continuar - 1\nEncerrar - 2\n\nEscolha: "))