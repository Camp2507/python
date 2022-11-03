# Crie um programa para calcular as notas obtidas pelo aluno do ensino médio, deverá mostrar
# mensagem para ser digitado a nota da 1ª, 2ª, 3ª e 4ª prova e a nota do 1º, 2º, 3º e 4º trabalho.
# Após deverá mostrar na tela a média obtida no 1º, 2º, 3º e 4ºbimestre.
# E depois o total informado se o aluno foi aprovado, esta em recuperação ou foi reprovado sem recuperação
print("Programa para calcular notas provas e trabalhos bimestrais")

p1 = float(input("Digite a nota da prova 1º Bimestre (Valor maximo 25): "))
t1 = float(input("Digite a nota do trabalho 1º Bimestre (Valor maximo 25): "))
p2 = float(input("Digite a nota da prova 2º Bimestre (Valor maximo 25): "))
t2 = float(input("Digite a nota do trabalho 2º Bimestre (Valor maximo 25): "))
p3 = float(input("Digite a nota da prova 3º Bimestre (Valor maximo 25): "))
t3 = float(input("Digite a nota do trabalho 3º Bimestre (Valor maximo 25): "))
p4 = float(input("Digite a nota da prova 4º Bimestre (Valor maximo 25): "))
t4 = float(input("Digite a nota do trabalho 4º Bimestre (Valor maximo 25): "))


b1 = (p1+t1)/2
b2 = (p2+t2)/2
b3 = (p3+t3)/2
b4 = (p4+t4)/2

print("A Média do 1º Bimestre é: ", b1)
print("A Média do 2º Bimestre é: ", b2)
print("A Média do 3º Bimestre é: ", b3)
print("A Média do 4º Bimestre é: ", b4)

resultado = b1 + b2 +b3 +b4
print("O resultado final do aluno foi: ", resultado)
if (resultado >= 60 and resultado <= 100):
    print("O aluno está aprovado! ")
elif(resultado >= 40 and resultado < 60):
    print("O aluno está em recuperação! ")
elif(resultado < 40 and resultado >= 0):
    print("O aluno está reprovado!")
else:
    print("Confirme os valores digitados, valor inválido!!!!")