def area(a):
    return a ** 2

def perimetro(p):
    return p * 4

while True:
    print("__________MENU__________")
    print("Olá, escolha se você deseja saber o perímetro ou área do quadrado!")
    print("1 - Área")
    print("2 - Perímetro")

    opcao = input("Digite a opção: ")

    if opcao == '1':
        a = float(input("Digite o valor do lado do quadrado para calcular a área: "))
        ar = area(a)
        print("A área é:", ar)
        break

    elif opcao == '2':
        p = float(input("Digite o valor do lado do quadrado para calcular o perímetro: "))
        pr = perimetro(p)
        print("O perímetro é:", pr)
        break

    else:
        print("Opção inválida, por favor, digite novamente!")


    

