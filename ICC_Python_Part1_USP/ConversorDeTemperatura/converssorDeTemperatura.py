# Função para converter Celsius para Fahrenheit
def celsius_para_fahrenheit(celsius):
    fahrenheit = celsius * (9 / 5) + 32
    return fahrenheit

# Função para converter Fahrenheit para Celsius
def fahrenheit_para_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * (5 / 9)
    return celsius

# Mensagem de boas-vindas
print("Olá, você está em um conversor de Temperaturas!!!!")

# Loop do menu
while True:
    # Menu de opções
    print("Escolha o tipo de conversão:")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        # Conversão de Celsius para Fahrenheit
        celsius = float(input("Digite o valor da temperatura em Celsius: "))
        fahrenheit = celsius_para_fahrenheit(celsius)
        print("O valor em Fahrenheit é:", fahrenheit, "F")
        break  # Sai do loop após a conversão ser feita
    
    elif opcao == "2":
        # Conversão de Fahrenheit para Celsius
        fahrenheit = float(input("Digite o valor da temperatura em Fahrenheit: "))
        celsius = fahrenheit_para_celsius(fahrenheit)
        print("O valor em Celsius é:", celsius, "C")
        break  # Sai do loop após a conversão ser feita
    else:
        print("Opção inválida. Por favor, escolha 1 ou 2.")

