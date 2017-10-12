import random



def jogar():

    imprime_mensagem_inicial()
    palavra_secreta = ler_arquivo()
    letras_acertadas = getLetrasAcertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0
    tentativas = 7

    while(not enforcou and not acertou):

        chute = chutar()

        if(chute in palavra_secreta):
            marcar_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1

        enforcou = (erros == tentativas)
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
        desenha_forca(erros)


    imprimir_mensagem_final(acertou, palavra_secreta)

def imprime_mensagem_inicial():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def ler_arquivo():
    with open("palavras.txt", 'r') as arquivo:
        palavras = []
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].lower()

    return palavra_secreta

def getLetrasAcertadas(palavra_secreta):
    return ['_' for letra in palavra_secreta]

def chutar():
    return input("Qual letra? ").strip().lower()


def marcar_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0;
    for letra in palavra_secreta:
        if (chute.lower() == letra.lower()):
            letras_acertadas[index] = letra
        index += 1


def imprimir_mensagem_final(acertou, palavra_secreta):
    if (acertou):
        imprimir_vencedor()
    else:
        imprimir_perdedor(palavra_secreta)

def imprimir_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprimir_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    jogar()
