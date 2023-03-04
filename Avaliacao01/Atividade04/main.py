from classes import *
from functions import *

escola = list()
def show():
    print("--- Mine Controle Acadêmico ---")
    print("1. Cadastrar disciplina")
    print("2. Pesquisar disciplina")
    print("3. Listar disciplinas cadastradas")
    print("4. Cadastrar professor em disciplina")
    print("5. Matricular aluno em disciplina")
    print("6. Lançar notas do aluno em uma disciplina")
    print("7. listar alunos de uma disciplina")
    print("8. Listar notas dos alunos de uma disciplina")
    print("9. sair")

while True:
    show()
    opcao = leitura("I", "Digite uma opção: ")
    if opcao == 1:
        turma = disciplina()
        pertence = False
        for dis in escola:
            if dis.codigo == turma.codigo:
                pertence = True
                break
        if pertence == False:
            escola.append(turma)
    elif opcao == 2:
        codigo = leitura("I", "Digite o código da disciplina: ")
        pertence = False
        for dis in escola:
            if dis.codigo == codigo:
                dis.show()
                pertence = True
                break
        if pertence == False:
            print("ERRO! Disciplina não encontrada!")

    elif opcao == 3:
        for dis in escola:
            dis.show()
    elif opcao == 4:
        codigo = leitura("I", "Digite o código da disciplina: ")
        for dis in escola:
            if codigo == dis.codigo:
                dis.cadastrarProfessor()
                break
    elif opcao == 5:
        codigo = leitura("I", "Digite o código da disciplina: ")
        for dis in escola:
            if codigo == dis.codigo:
                dis.cadastrarAluno()
                break
    elif opcao == 6:
        codigo = leitura("I", "Digite o código da disciplina: ")
        for dis in escola:
            if dis.codigo == codigo:
                codAluno = leitura("I", "Digite o código do aluno: ")
                for alu in dis.alunos:
                    if alu.matricula == codAluno:
                        for c in range(3):
                            nota = leitura("F", f"Digite a {c+1}º nota: ")
                            alu.notas.append(nota)
    elif opcao == 7:
        print()
    elif opcao == 8:
        print()
    elif opcao == 9:
        break
    else:
        print("Erro! Digite um valor correto!")
