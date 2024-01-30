# Solicita ao usuário que insira um número inteiro
numero = int(input("Digite um número inteiro: "))

# Extrai o dígito das dezenas
digito_dezenas = (numero // 10) % 10

# Imprime o resultado
print(f"O dígito das dezenas é {digito_dezenas}")
