# Crie um programa para calcular as notas obtidas pelo aluno do
# ensino médio, deverá mostrar mensagem para ser digitado a
# nota do 1º, 2º, 3º e 4º bimestre. Após deverá mostrar na
# tela se o aluno foi aprovado, se está em recuperação ou foi reprovado
# sem chance de recuperação.
# Lembrando que cada bimestre vale 25 pontos num total anual de 100 pontos.

print("Calculamento de notas")
B1 = float(input("Digite nota 1° Bimestre: "))
B2 = float(input("Digite nota 2° Bimestre: "))
B3 = float(input("Digite nota 3° Bimestre: "))
B4 = float(input("Digite nota 4° Bimestre: "))

resultado = B1 + B2 + B3 + B4

print("Soma de todos os bimestres = ", resultado)

if resultado >= 60:
    print("Aprovado")

elif resultado >= 40:
    print("Recuperação")
elif resultado < 40:
    print("Reprovado")