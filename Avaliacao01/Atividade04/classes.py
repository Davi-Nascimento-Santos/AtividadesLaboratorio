from functions import *

class professor():
    nome = None
    codigo = None

    def __init__(self):
        self.nome = leitura("S", "Digite o nome do professor: ")
        self.codigo = leitura("I", "Digite o código do professor: ")


class aluno():

    def __init__(self):
        self.matricula = leitura("I", "Digite a matricula do aluno: ")
        self.nome = leitura("S", "Digite o nome do aluno: ")
        self.curso = leitura("S", "Digite o curso do aluno: ")
        self.notas = []


class disciplina():
    def __init__(self):
        self.codigo = leitura("I", "Digite o código da disciplina: ")
        self.nome = leitura("S", "Digite o nome da disciplina: ")
        self.semestre = leitura("F", "Digite o semestre da disciplina: ")
        self.professores = []
        self.alunos = []
        self.diasHorarios = []
        self.cargaHoraria = leitura("I", "Digite a carga horária: ")
        quant = leitura("I", "Digite a quantidade de dias: ")
        dias = []
        for c in range(quant):
            dias.append(leitura("I", f"Digite o {c+1} dia: "))
        self.diasHorarios.append(dias)
        self.diasHorarios.append(leitura("I", "Digite o horário da disciplina: "))
            
    def cadastrarProfessor(self):
        prof = professor()
        pertence = False
        if len(self.professores)>0:
            for c in self.professores:
                if c.codigo == prof.codigo:
                    print("ERRO! Professor já cadastrado!")
                    pertence = True
        if pertence == False:
            self.professores.append(prof)

    def cadastrarAluno(self):
        estudante = aluno()
        pertence = False
        if len(self.alunos)>0:
            for c in self.alunos:
                if c.matricula == estudante.matricula:
                    print("ERRO! Aluno já cadastrado!")
                    pertence = True
        if pertence == False:
            self.alunos.append(estudante)
    def show(self):
        print(f"Código: {self.codigo}")
        print(f"Disciplina: {self.nome}")
        print(f"Semestre: {self.semestre}")
        if len(self.professores)>0:
            print("-----Professores-----")
        for c in self.professores:
            print(f"Código: {c.codigo}, Nome: {c.nome}")
        if len(self.alunos)>0:
            print("-----Alunos-----")
        for c in self.alunos:
            print(f"Matrícula: {c.matricula}, Nome: {c.nome}, Curso: {c.curso}")
        print(f"Dias: {self.diasHorarios[0]}")
        print(f"Horário: {self.diasHorarios[1]}")
        
