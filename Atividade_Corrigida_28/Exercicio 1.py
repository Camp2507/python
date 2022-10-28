# Crie um programa que pergunte em que turno você estuda.
# Peça para digitar M-matutino ou V-Vespertino ou N-Noturno.
# Mostre a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
# Em python a condição de caso aceita comparar com caractere, nome é match.

print("Programa para realização saudação do dia!")
turno = input("Digite seu turno, M para Manhã, T para Tarde e N para noite: ").upper()

match turno:
    case "M":
        print("Bom dia!")
    case "T":
        print("Boa tarde!")
    case "N":
        print("Boa noite!")
    case _:
        print("Valor Inválido!")