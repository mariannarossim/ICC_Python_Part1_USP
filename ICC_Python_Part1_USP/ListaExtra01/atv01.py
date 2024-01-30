import random


print("___________MENU___________")
print("__Segunda Via de Fatura__")

nome = input("Digite seu nome Completo: ")
dia = input("Digite o dia de vencimento: ")
mes = input("Digite o mês de vencimento: ")
val = input("Digite o valor da fatura: ")

print("Ola,", nome, "!!!!")
print("A sua fatura com vencimento em:", dia, "/", mes, "no", "R$", val, "está fechada!!!!\nSegue o código de pagamento:", random.randint(1000000, 9999999))
