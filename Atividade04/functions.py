def leitura(letra, frase):
    dado = None
    if letra.upper()=='S':
        dado = str(input(frase))
    elif letra.upper()=='F':
        dado = float(input(frase))
    elif letra.upper()== 'I':
        dado = int(input(frase))
    return dado
