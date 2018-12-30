from random import randint

def megaSena():
    numero = randint(1,50063860)
    if (numero == 1):
        print("Parabens, voce ganhou na Mega-Sena!")
        return 1
    else:
        print("Voce nao conseguiu, tente de novo :(")
        return 0

def main():
    opcao = 0
    while opcao != 3:
        print("----------------------------------------")
        print("-----------Simulador MegaSena-----------")
        print("----------------------------------------")
        print("Criado por Pablo Gonzalez - www.github.com/pablogonzalezz\n")
        print("Opcoes:\n")
        print("1 - Jogar na MegaSena\n")
        print("2 - Jogar na MegaSena ate ganhar\n")
        print("3 - Sair\n")

        opcao = input("O que deseja fazer?")

        if opcao == 1:
            megaSena()
        if opcao == 2:
            acerto = 0
            count = 0
            while acerto == 0:
                acerto = megaSena()
                count = count + 1
                print("Essa eh a tentativa " + str(count))
                
                

if(__name__=="__main__"):
    main()