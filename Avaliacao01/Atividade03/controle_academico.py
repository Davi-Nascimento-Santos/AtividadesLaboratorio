from functions import *
escola = list()
disciplinas = open("disciplinas.txt", 'a')
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
        preenchido = True
        if len(escola) != 0:
            for disciplina in escola:
                if len(disciplina[3]) != 0:
                    if len(disciplina[4]) != 0:
                        for aluno in disciplina[4]:
                            if len(aluno[3]) != 0:
                                preenchido = True
                            else:
                                preenchido = False
                                print("ERRO! Cadastre as notas dos alunos!")
                                break
                    else:
                        preenchido = False
                        print("ERRO! Cadastre os alunos!")
                else:
                    preenchido = False
                    print("ERRO! Cadastre os professores!")
                    break
        else:
            preenchido = False
            print("ERRO! Cadastre as disciplinas!")

        if preenchido==True:
            for disciplina in escola:
                disciplinas.write(str(disciplina))
                disciplinas.write("\n")
            disciplinas.close()
            break

print(escola)