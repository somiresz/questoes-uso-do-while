#Peça números ao usuário e some-os. 
#O programa deve parar quando o usuário digitar um número negativo. Ao final, mostre a soma total.
soma = 0
while True:
    numero = int(input("Digite um número (Números negativos param o programa): "))
    if numero < 0:
        break
    else:
        soma = soma + numero
print ("A soma total é:", soma)