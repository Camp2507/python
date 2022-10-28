# Crie um programa para realizar as operações de uma tabuada de
# multiplicação, onde será solicitado ao usuário digitar qual
# numero será a tabuada e qual intervalo do inicio e fim da tabuada,
# exibir na tela o resultado conforme intervalo.
# Repetição usando “PARA”
print("Tabuada do numero desejado!")

tabuada = int(input("Digite o numero da tabuada: "))
inicio = int(input("Digite o inicio do intervalo da tabuada: "))
fim = int(input("Digite o fim do intervalo da tabuada: "))

for i in range(inicio, fim + 1):
    print("Tabuada do numero ", tabuada, " resultado: ", tabuada, " * ", inicio, "= ", tabuada * inicio)
    # print("Tabuada resultado: ", tabuada * inicio)
    inicio = inicio + 1