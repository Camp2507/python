# Crie um programa que leia um conjunto de nomes de 20 estudantes inscritos na prova do ENEM. Com esses nomes, realizar uma
# ordenação crescente usando uma função para facilitar a localização do nome na lista que será afixada no quadro de avisos da escola.
# def nomeDaFuncao(): linhas de comando da função Se tiver parâmetros é só colocar no parênteses (parm1, param2)
# Para chamar a função é nomeDaFuncao() se tiver que passar parâmetros é só colocar no parêntese (param1, param2)
def Ordenacao(vetor):
    for i in range(len(vetor)):
        for j in range(i+1, len(vetor)):
            if vetor[i] > vetor[j]:
                x = vetor [i]
                vetor[i] = vetor[j]
                vetor[j] = x

    return vetor

vetor =[]
for i in  range(3):
    vetor.append(input("Digite um nome do aluno do Enem: ").capitalize())

vetorOrdenado = Ordenacao(vetor)
print(vetorOrdenado)
