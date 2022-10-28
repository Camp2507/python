#Crie um programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N-Noturno.
# Mostre a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
#Em python a condição de caso aceita comparar com caractere, nome é match.match suaVariável:
#case “valor":
#comando
#case _: #esse é o outro caso
#comandos

print("Digite o turno de estudo, 0 para Matutino, 1 para Vastutino, 2 para Noturno e 3")
turnos = (input(" Qual turno você estuda ?: "))

match turnos:

    case "0":
       print("bom dia")

    case "1":
       print("boa tarde")

    case "2":
       print("boa noite")

    case "3":
        print("Valor inválido")
