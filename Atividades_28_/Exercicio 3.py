# Crie um programa em que o usuário deve digitar números
# inteiros para uma matriz de 5 linhas e 5 colunas .
# Após a digitação dos números, o usuário deve digitar
# um número aleatório e verificar se ele se encontra na matriz.
# Ao final, os índices da linha e da coluna devem ser
# impressos se o elemento for encontrado; caso contrário,
# a mensagem “elemento não encontrado” deve ser mostrada na tela.

print("Procurar Matriz")
matriz = [[0,1,2,3,4],[0,1,2,3,4], [0,1,2,3,4], [0,1,2,3,4]]
mensagem = False
for i in range(5):
    for j in range(5):
        matriz[i][j] = int(input("Digite numeros para colocar na matriz: "))
numero = int(input("Digite um numero"))
print(matriz)
for i in range(5):
    for j in range(5):
     if [i][j] == numero:
         mensagem = True
     else:
         print("numero encontrado")
     if mensagem == False:
         print("numero não encontrado")