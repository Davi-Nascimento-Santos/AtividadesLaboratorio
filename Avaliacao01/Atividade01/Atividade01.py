from random import randint
from time import time
def menu():
    print("----Menu----")
    print("F - Fácil")
    print("M - Médio")
    print("D - Difícil")
    print("Qual a sua opção?")

print("Bem vindo ao Jogo da Adivinhação")
nome = str(input("Qual o seu nome? "))
while(True):
    valorSorteado = randint(0, 10)
    tentativas=0
    valor=0    
    menu()
    opcao = str(input("")).upper()
    tentativasMax=0
    if opcao == "F":
        tentativasMax=10
    elif opcao == "M":
        tentativasMax=5
    elif opcao == "D":
        tentativasMax=3
    start = time()
    while(tentativas<tentativasMax):
        valor = int(input("Qual seu palpite? "))
        tentativas+=1
        if tentativas<tentativasMax:
            if valor == valorSorteado:
                break
            elif valor > valorSorteado:
                print("Você errou para cima... tente um número menor.")
            elif valor < valorSorteado:
                print("Você errou para baixo... tente um número maior.")
        else:
            print("Você perdeu a rodada!")
    stop = time()
    if valor==valorSorteado:
        print(f"Nome: {nome}")
        print(f"Número de jogadas: {tentativas}")
        print(f"Tempo de jogo: {(stop-start):.0f} segundos ")
        print(f"Parabéns! Você ganhou o jogo!\n")
    else:
        print(f"Nome: {nome}")
        print("Não foi dessa vez! Você perdeu a rodada!\n")
    continuar = str(input("Deseja continuar jogando S/N: ")).upper()
    if continuar=="N":
        break