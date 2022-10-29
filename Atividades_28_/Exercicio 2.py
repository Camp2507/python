# Crie um programa para calcular as notas obtidas pelo aluno do
# ensino médio, deverá mostrar mensagem para ser digitado a
# nota da 1ª, 2ª, 3ª e 4ª prova e a nota do 1º, 2º, 3º e 4º trabalho.
# Após deverá mostrar na tela a média obtida no 1º, 2º, 3º e 4º bimestre.
# E depois o total informado se o aluno foi aprovado, esta em
# recuperação ou foi reprovado sem recuperação.

print("Lançamento e Calculamento de notas")

print("Valor da prova = 12")
print("Valor da trabalho = 13")

P1 = float(input("Digite nota da Prova 1° Bimestre: "))
P2 = float(input("Digite nota da Prova 2° Bimestre: "))
P3 = float(input("Digite nota da Prova 3° Bimestre: "))
P4 = float(input("Digite nota da Prova 4° Bimestre: "))
T1 = float(input("Digite nota do Trabalho 1° Bimestre: "))
T2 = float(input("Digite nota do Trabalho 2° Bimestre: "))
T3 = float(input("Digite nota do Trabalho 3° Bimestre: "))
T4 = float(input("Digite nota do Trabalho 4° Bimestre: "))

r1 = P1 + T1
r2 = P2 + T2
r3 = P3 + T3
r4 = P4 + T4
r5 = r1 + r2 + r3 + r4
print("Soma de todos os bimestres = ", r5)

if r5 >= 60:
    print("Aprovado")

elif r5 >= 40:
    print("Recuperação")
elif r5 < 40:
    print("Reprovado")