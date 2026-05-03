#Continuar pedindo uma nota entre 0 e 10
while True:
    nota = int(input("Digite uma nota entre 0 e 10 para ser registrada: "))
    if nota >=0 and nota <=10:
        print(f"Sua nota ({nota}) foi registrada!")
        break
    else:
        print("Sua nota não está entre 0 e 10, digite o número correto.")