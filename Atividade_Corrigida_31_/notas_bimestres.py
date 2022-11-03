# Crie um programa para calcular as notas obtidas pelo aluno do
# ensino médio, deverá mostrar mensagem para ser digitado a
# nota do 1º, 2º, 3º e 4º bimestre. Após deverá mostrar na tela se o aluno
# foi aprovado, se está em recuperação ou foi reprovadosem chance de recuperação.
# Lembrando que cada bimestre vale 25 pontos num total anual de 100 pontos.

print("Programa para calcular notas bimestrais")

b1 = float(input("Digite a nota do 1º Bimestre (Valor maximo 25): "))
b2 = float(input("Digite a nota do 2º Bimestre (Valor maximo 25): "))
b3 = float(input("Digite a nota do 3º Bimestre (Valor maximo 25): "))
b4 = float(input("Digite a nota do 4º Bimestre (Valor maximo 25): "))

resultado = b1+b2+b3+b4
print("O resultado final do aluno foi: ", resultado)
if (resultado >= 60 and resultado <= 100):
    print("O aluno está aprovado! ")
elif(resultado >= 40 and resultado < 60):
    print("O aluno está em recuperação! ")
elif(resultado < 40 and resultado >= 0):
    print("O aluno está reprovado!")
else:
    print("Confirme os valores digitados, valor inválido!!!!")