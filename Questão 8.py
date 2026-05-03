#Peça um número e mostre a tabuada dele de 1 a 10.
numero = int(input("Digite um número para mostrar a tabuada de 1 a 10: "))
i = 1
while i <= 10:
    resultado = numero * i
    print(numero, "x", i, "=", resultado)
    i = i + 1