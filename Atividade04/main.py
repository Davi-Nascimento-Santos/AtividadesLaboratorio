from classes import *
from functions import *

escola = list()
turma = disciplina()
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
        turma.cadastrarDisciplina()
        pertence = False
        for disciplina in escola:
            if disciplina.codigo == turma.codigo:
                pertence = True
                break
        if pertence == False:
            escola.append(turma)
    elif opcao == 2:
        codigo = leitura("I", "Digite o código da disciplina: ")
        pertence = False
        for disciplina in escola:
            if disciplina.codigo == codigo:
                disciplina.show()
                pertence = True
                break
        if pertence == False:
            print("ERRO! Disciplina não encontrada!")

    elif opcao == 3:
        for disciplina in escola:
            disciplina.show()
    elif opcao == 4:
        codigo = leitura("I", "Digite o código da disciplina: ")
        for disciplina in escola:
            if codigo == disciplina.codigo:
                disciplina.cadastrarProfessor()
                break
    elif opcao == 5:
        codigo = leitura("I", "Digite o código da disciplina: ")
        for disciplina in escola:
            if codigo == disciplina.codigo:
                disciplina.cadastrarAluno()
                break
    elif opcao == 6:
        print()
    elif opcao == 7:
        print()
    elif opcao == 8:
        print()
    elif opcao == 9:
        break
    else:
        print("Erro! Digite um valor correto!")