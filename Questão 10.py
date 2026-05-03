#Defina um número fixo no código. 
#Peça ao usuário para adivinhar até acertar. Informe se o palpite é maior ou menor que o número correto.
numero = 67
print("--- Adivinhe o número secreto ---")
while True:
    palpite = int(input("Digite um número inteiro: "))
    if palpite > numero:
        print(f"O número secreto é menor")
    elif palpite < numero:
        print(f"O número secreto é maior")
    else:
        print(f"Parabéns, você acertou!")