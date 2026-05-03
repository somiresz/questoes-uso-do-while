#Peça várias notas ao usuário (encerra quando digitar -1) e calcule a média das notas válidas.
soma = 0
quantidade = 0
while True:
    nota = float(input("Digite sua nota: "))
    print("Para encerrar o pedido de notas, digite (-1) para prosseguir para média das notas.")
    if nota == -1:
        break
    soma = soma + nota
    quantidade = quantidade + 1
if quantidade > 0:
    media = soma/quantidade
    print("A média das notas é:", media)
else:
    print("Nenhuma nota válida foi registrada.")
