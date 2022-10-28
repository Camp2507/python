# Crie um programa de calculadora que realiza as operações de
# soma, multiplicação, divisão e subtração, será perguntado
# ao usuário se deseja continuar com o uso da calculadora,
# enquanto ele digitar (“S” – Sim) o programa irá reiniciar a calculadora.
# Repetição usando ”ENQUANTO”
print("calculadora matemática wile!")
sim = "S"
while sim == "S":
	#sendo verdadeiro repete até ser falso
    print("Programa para calcular operações matemáticas")
    num1 = float(input("Digite o primeiro número inteiro: "))
    num2 = float(input("Digite o segundo número inteiro: "))

    resultado = num1 + num2
    resultado1 = num1 - num2
    resultado2 = num1 * num2
    resultado3 = num1 / num2
    resultado4 = num1 % num2
    resultado5 = num1 ** num2

    print("A soma de número 1 + número 2 é: ", resultado)
    print("A subtração de número 1 - número 2 é: ", resultado1)
    print("A multiplicação de número 1 * número 2 é: ", resultado2)
    print("A divisão de número 1 / número 2 é: ", resultado3)
    print("O resto da divisão de número 1 / número 2 é: ", resultado4)
    print("a potência de número 1 pelo número 2 é: ", resultado5)

    sim = input("Deseja continuar? s ou n ").upper()

print("fim")