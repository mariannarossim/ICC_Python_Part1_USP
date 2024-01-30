
print("Conversor de numeros!!!!")
segundos_totais = float(input("Digite o numero que você deseja converter em dias, horas, minutos e segundos: "))

# Calcula dias, horas, minutos e segundos
dias = segundos_totais // (24 * 3600)
segundos_restantes = segundos_totais % (24 * 3600)
horas = segundos_restantes // 3600
segundos_restantes %= 3600
minutos = segundos_restantes // 60
segundos = segundos_restantes % 60

# Imprime o resultado formatado
print(f"{dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos.")
