# Faça um programa que leia o nome e a data de nascimento  e ao Final exiba o nome da pessoa e  a idade dessa pessoa
# expressa em dias, o programa deve perguntar ao final se deseja repetir a operação para outra pessoa. Considerar ano com 365 dias e mês com 30 dias.

print(" Sua idade em dias são ")
sim = "S"
while sim == "S":
	#sendo verdadeiro repete até ser falso
    nome = input("Digite um nome: ")
    Ddnascimento = int(input("Digite ano que você nasceu: "))
    ano = int(input("Digite o ano que você está: "))

    result = ano - Ddnascimento
    result2 = result * 365
    print("Seu nome é", nome, "e sua idade em dias aproximadamente são de", result2)

    sim = input("Deseja fazer uma nova pesquisa? s ou n ").upper()

print("fim")

# OBS: Quando chegou no final da aula que eu fui ver que eu tinha feito com o ano de nascimento achando  que era data de nascimento, como não daria tempo de refazer eu deixei desse jeito e mudei o nome.