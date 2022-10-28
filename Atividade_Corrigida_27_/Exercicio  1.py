# Crie um programa receba 5 produtos em variáveis constantes, iPhone, Samsung, Tablet, PS5, notebook ,
# com valores respectivos de R$ 2980, R$ 2540, R$ 1950, R$ 2100, R$ 2350.
# O usuário deverá informar a quantidade de cada produto que ele deseja comprar em sua loja,
# caso não queira nenhum produto deverá informar o valor 0 (zero) de quantidade. Mostrar resultados abaixo

iPhone = 2980
samsung = 2540
tablet = 1950
pS5 = 2100
notebook = 2350

print("O Valor do iPhone é R$: ", iPhone)
totalIphone = iPhone * float((input("Deseja compar quantos? ")))
print("O Valor do samsung é R$: ", samsung)
totalsamsung = samsung * float((input("Deseja compar quantos? ")))
print("O Valor do tablet é R$: ", tablet)
totaltablet = tablet * float((input("Deseja compar quantos? ")))
print("O Valor do pS5 é R$: ", pS5)
totalpS5 = pS5 * float((input("Deseja compar quantos? ")))
print("O Valor do notebook é R$: ", notebook)
totalnotebook = notebook * float((input("Deseja compar quantos? ")))
totalgeral = totalnotebook + totalIphone +totaltablet + totalpS5 + totalsamsung
# Ao final da compra mostre o valor total de todos os produtos.
print("Valor total de venda dos produtos: R$ ", totalgeral)
# O valor da parcela dividido em 3X sem juros.
print("Valor da parcela dividido em 3x sem juros: R$ ", totalgeral/3)
# O valor da parcela dividido em 6X com acréscimo de 5%.
print("Valor da parcela dividido em 6x com juros 5%: R$ ", (((totalgeral/100)*5)+totalgeral)/6)
# print("Valor da parcela dividido em 6x com juros 5%: R$ ", ((totalgeral*1.05)/6)) #outra forma de calcular porcentagem
# E um valor com 10% de desconto para pagamento à vista.
print("Valor com desconto de 10% à vista: R$ ", (totalgeral-(totalgeral/100)*10))
# print("Valor com desconto de 10% à vista: R$ ", (totalgeral-(totalgeral * 0.10))) #outra forma de calcular porcentagem
