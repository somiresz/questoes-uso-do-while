#Peça vários números ao usuário (encerra com 0) e informe qual foi o maior número digitado.
maior = None
while True:
    numero = float(input("Digite um número: "))
    if numero == 0:
        break
    if maior is None or numero > maior:
        maior = numero
print("O maior número digitado foi:", maior)