# Crie um programa em que o usuário deve digitar números inteiros para uma matriz
# de 5 linhas e 5 colunas. Após a digitação dos números, o usuário deve digitar um
# número aleatório e verificar se ele se encontra na matriz. Ao final, os índices da
# linha e da coluna devem ser impressos se o elemento for encontrado; caso contrário, a
# mensagem “elemento não encontrado” deve ser mostrada na tela.

lista = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

for i in range(5):
    for j in range(5):
        lista[i][j] = int(input("Digite um número inteiro: "))

n1 = int(input("Digite um numero inteiro para localizar na matriz"))
encontrado = False

for i in range(5):
    for j in range(5):
        if lista[i][j] == n1:
            print("Numero encontrado: ", n1, " na posição ", i , j)
            encontrado = True

if encontrado is False:
    print("Não foi encontrado na busca seu numero: ", n1)

print(lista)

#matriz em pythn é Lista de Lista, ou seja, lista = [[],[],[],[],[]] #matriz de 5 linhas e 5 colunas
#
# lista = [
#          [0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0]
#          ]