#Peça números ao usuário até que ele digite 0. 
#Ao final, informe quantos números positivos e quantos negativos foram digitados.
positivos = 0
negativos = 0
print("-- Se digitar 0, o pedido de número irá parar. --")
while True:
    numero = int(input("Digite um número: "))
    if numero == 0:
        break
    if numero > 0:
        positivos = positivos + 1
    else:
        negativos = negativos + 1
print("Quantidade de positivos:", positivos)
print("Quantidade de negativos:", negativos)