from functions import *
escola = list()
while True:
    show()
    while True:
        try:
            opcao = int(input("Digite a opção: "))
            if 1 <= opcao <= 9:
                break
            else:
                print("ERRO! Selecione um das opções!")
        except:
            print("ERRO! Digite um valor correto!")
    if opcao == 1:
        escola.append(cadastraDisciplina(escola))
    elif opcao == 2:
        pesquisarDisciplina(escola)
    elif opcao == 3:
        listarDisciplinas(escola)
    elif opcao == 4:
        cadastrarProfessor(escola)
    elif opcao == 5:
        matricularAlunoDisciplina(escola)
    elif opcao == 6:
        lancarNotasAluno(escola)
    elif opcao == 7:
        listarAlunos(escola)
    elif opcao == 8:
        listarNotasAlunos(escola)
    elif opcao == 9:
        break
print(escola)