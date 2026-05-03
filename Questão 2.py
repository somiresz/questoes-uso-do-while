#Peça ao usuário para digitar uma senha. 
#Continue solicitando até que ele acerte a senha correta. (defina uma senha fixa no código).
while True:
    senha = "1a2b3c4d1e"
    s = str(input("Digite a senha: "))
    if s == senha:
        print("Senha correta!")
        break
    else:
        print("Senha inválida, tente novamente.")