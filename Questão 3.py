#Peça um número inteiro positivo N e mostre todos os números de 1 até N usando repetição.
while True:
    numero = int(input("Digite um número inteiro e positivo: "))
    if numero > 0:
        i = 1
        while i <= numero:
            print(i)
            i = i + 1
        break
    else:
        print("Tente novamente com um número válido.")