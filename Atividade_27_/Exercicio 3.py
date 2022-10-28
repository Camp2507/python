#Crie um programa de calculadora que realiza as operações de
#soma, multiplicação, divisão e subtração, será perguntado ao
#usuário se deseja continuar com o uso da calculadora, enquanto ele digitar
#(“S” – Sim) o programa irá reiniciar a calculadora.
#Repetição usando ”ENQUANTO”
#while == “valor”
#sendo verdadeiro repete até ser falso
sim = "S"
while sim == "S":
    
print("Calculadora")
print("Digite - para subtração")
print("Digite + Para soma")
print("Digite * Multiplicação")
print("Digite / Divisão")
print("Digite s para reiniciar a calculadora")
num1 = float(input("Digite um numero real para calcular: "))



sim = input("Deseja continuar? s ou n: ").upper()