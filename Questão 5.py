#Peça números ao usuário continuamente e informe se cada número é par ou ímpar. 
#O programa só deve parar quando o usuário digitar 0.
while True:
    numero = int(input("Digite um número: "))
    if numero == 0:
        break
    elif numero % 2 == 0:
        print("Seu número é par:")
    elif numero % 2 != 0:
        print("Seu número é ímpar:")