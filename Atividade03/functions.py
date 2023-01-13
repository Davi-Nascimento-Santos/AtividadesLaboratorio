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

def cadastraDisciplina(escola):
    while True:
        try:
            equal = False
            cod = int(input("Digite o código da disciplina: "))
            for i in escola:
                if cod == i[0]:
                    print("Código já cadastrado")
                    equal = True
            if equal == False:
                break
        except:
            print("ERRO! Digite um valor correto!")
    while True:
        equal = False
        disciplina = str(input("Digite o nome da disciplina: "))
        for i in escola:
            if disciplina == i[1]:
                print("Disciplina já cadastrada")
                equal = True
        if equal == False:
            break
    while True:
        try:
            semestre = float(input("Digite o semestre da disciplina "))
            break
        except:
            print("ERRO! Digite um valor correto!")
    professores = []
    alunos = []
    while True:
        try:
            cargaHoraria = int(input("Digite a carga horária da disciplina: "))
            if 15 <= cargaHoraria <= 120:
                break
            else:
                print("ERRO! Digite uma carga horária válida [15, 120]!")
        except:
            print("ERRO! Digite um valor correto!")
    diaSemana = []
    cont =0
    while True:
        while True:
            try:
                dia = int(input(f"Digite o {cont+1}º dia da semana: "))
                if 1 <= dia <= 6: 
                    diaSemana.append(dia)
                    break
                else:
                    print("ERRO! Digite um dia válido [1, 6]!")
            except:
                print("ERRO! Digite um valor correto!")
        cont+=1
        if cont==3:
            break
        while True:
            continua = str(input("Quer adicionar mais um dia [S]/[N]? " )).upper()
            if continua == "S" or continua == "N":
                break
            else:
                print("ERRO! Selecione uma das duas opções!")
        if continua == "N":
            break
    while True:
        try:
            horario = int(input("Digite o horário da disciplina: "))
            if 1 <= horario <= 7:
                break
            else:
                print("ERRO! Digite um horário válido [1, 7]!")
        except:
            print("ERRO! Digite um valor correto!")
    diasHorarios = (diaSemana, horario)

    return cod, disciplina, semestre, professores, alunos, cargaHoraria, diasHorarios

def cadastrarProfessor(escola):
    if len(escola) != 0:
        while True:
            try:
                cod = int(input("Digite o código da disciplina: "))
            except:
                print("ERRO! Digite um valor correto!")
            equal = False
            for i in escola:
                if i[0] == cod:
                    equal = True
                    if len(i[3])==0:
                        while True:
                            try:
                                codProf = int(input("Digite o código do professor: "))
                                break
                            except:
                                print("Erro! Digite um valor correto!")
                        nomeprof = str(input("Digite o nome do professor: "))
                        professor = (codProf, nomeprof)
                        i[3].append(professor)
                        break
                    else:
                        while True:
                            repete = False
                            try:
                                codProf = int(input("Digite o código do professor: "))
                            except:
                                print("ERRO! Digite um valor correto!")
                            for c in i[3]:
                                if codProf == c[0]:
                                    repete = True
                                    break
                            if repete == False:
                                break
                            else:
                                print("ERRO! Código de professor já existe!")
                        nomeprof = str(input("Digite o nome do professor: "))
                        professor = (codProf, nomeprof)
                        i[3].append(professor)
            if equal == False:
                print("ERRO! Código de disciplina não existe!")
                if len(escola) != 0:
                    print("Disciplinas existentes ")
                    for c in escola:
                        print(f"Código: {c[0]}, Disciplina: {c[1]}")
            else:
                break
    else:
        print("ERRO! Não há nenhuma disciplina cadastrada, cadastre uma disciplina primeiro!")

def listarDisciplinas(escola):
    if len(escola) != 0:
        print()
        print("Disciplinas cadastradas:")
        for i in escola:
            print(f"Código: {i[0]}  Nome: {i[1]}")
    else:
        print("ERRO! Não existem disciplinas cadastradas, cadastre uma disciplina primeiro!")
def pesquisarDisciplina(escola):
    if len(escola) != 0:
        cod = int(input("Digite o código da disciplina a ser pesquisada: "))
        equal = False
        for i in escola:
            if i[0] == cod:
                equal = True
                print(f"Código: {i[0]}")
                print(f"Disciplina: {i[1]}")
                print(f"Semestre: {i[2]}")
                if len(i[3]) > 1:
                    for c in i[3]:
                        print(f"Código do professor: {c[0]}")
                        print(f"Nome do professor: {c[1]}")
                elif len(i[3]) == 1:
                    print(f"Código do professor: {i[3][0][0]}")
                    print(f"Nome do professor: {i[3][0][1]}")
                else:
                    print("Disciplina sem professor!")
                print(f"Carga horária: {i[5]}")
                print(f"Dias e horários: {i[6]}")
        if equal == False:
            print("ERRO! Código de disciplina não existe!")
    else:
        print("ERRO! Não há nenhuma disciplina cadastrada, cadastre uma disciplina primeiro!")

def matricularAlunoDisciplina(escola):
    if len(escola) != 0:
        cod = int(input("Digite o código da discplina que deseja colocar o aluno: "))
        equal = False
        disciplina = None
        for i in escola:
            if i[0] == cod:
                equal = True
                disciplina = i
                break
        if equal == True:
            while True:
                repete = False
                matAluno = int(input("Digite a matrícula do aluno: "))
                for c in disciplina[4]:
                    if c[0] == matAluno:
                        repete = True
                        break
                if repete == False:
                    nomeAluno = str(input("Digite o nome do aluno: "))
                    cursoAluno = str(input("Digite o curso do aluno: "))
                    aluno = (matAluno, nomeAluno, cursoAluno, [])
                    disciplina[4].append(aluno)
                    break
                else:
                    print("ERRO! Matrícula já existe!")
        else:
            print("ERRO! Disciplina não existe!")
    else:
        print("ERRO! Não existem disciplinas, cadastre uma primeiro!")
def lancarNotasAluno(escola):
    if len(escola) != 0:
        while True:
            while True:
                try:
                    cod = int(input("Digite o código da disciplina: "))
                    break
                except:
                    print("ERRO! Digite um valor correto!")
            equal = False
            disciplina = None
            for i in escola:
                if i[0] == cod:
                    equal = True
                    disciplina = i
                    break
            if len(disciplina[4]) == 0:
                print("ERRO! Não existem alunos, matricule um aluno primeiro")
                break
            if equal == True:
                while True:
                    while True:
                        try:
                            codAluno = int(input("Digite o código do aluno: "))
                            break
                        except:
                            print("ERRO! Digite um valor correto")
                    repete = False
                    for c in disciplina[4]:
                        if c[0] == codAluno:
                            repete = True
                            for i in range(3):
                                while True:
                                    try:
                                        nota = float(input(f"Digite a {i+1}º nota: "))
                                        c[3].append(nota)
                                        break
                                    except:
                                        print("ERRO! Digite uma nota válida!")
                            break
                    if repete == False:
                        print("ERRO! Código do aluno não existe!")
                    else:
                        break
                break
            else:
                print("ERRO! O código da disciplina não existe")
    else:
        print("ERRO! não existe nenhuma disciplina, cadastre uma disciplina primeiro!")
        

def listarAlunos(escola):
    if len(escola) != 0:
        try:
            cod = int(input("Digite o código da disciplina: "))
            equal = False
            disciplina = None
            for i in escola:
                if i[0] == cod:
                    equal = True
                    disciplina = i
                    break
            if equal == True:
                if len(disciplina[4]) != 0:
                    print(f"Disciplina: {disciplina[0]}")
                    for c in disciplina[4]:
                        print(f"Código do aluno: {c[0]}")
                        print(f"Nome: {c[1]}")
                        print(f"Curso: {c[2]}")
                        print()
                else:
                    print("ERRO! Não existem alunos, cadastre um aluno primeiro!")
            else:
                print("ERRO! Disciplina não existe!")
        except:
            print("ERRO! Digite um valor correto!")
    else:
        print("ERRO! Não existem disciplinas, cadastre uma disciplina primeiro!")

def listarNotasAlunos(escola):
    if len(escola) != 0:
        while True:
            try:
                cod = int(input("Digite o código da disciplina: "))
                break
            except:
                print("ERRO! Digite um valor correto!")
        equal = False
        disciplina = None
        for i in escola:
            if i[0] == cod:
                equal = True
                disciplina = i
                break
        if equal == True:
            if len(disciplina[4]) != 0:
                for c in disciplina[4]:
                    print(f"Nome: {c[1]}, Notas: ", end="")
                    if len(c[3]) != 0:
                        for n in c[3]:
                            print(f"{n} ", end=", ")
                        print()
                    else:
                        print("sem notas")
            else:
                print("ERRO! Não existem alunos cadastrados, cadastre um aluno primeiro!")
        else:
            print("ERRO! Código não existe!")
    else:
        print("ERRO! Não existem disciplinas cadastradas, cadastre uma lista primeiro!")

