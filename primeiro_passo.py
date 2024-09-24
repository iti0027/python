print("Vamos fazer um teste lógico básico?")
nome = input("Escreva o seu nome: ")
idade = int(input("Escreva a sua idade: "))

if idade < 18:
    print("Você é de menor e ainda não pode tirar a habilitação")
else:
    print("Você é de maior idade e pode tirar a habilitação")