
def cria_peca(marca):
    if not eh_peca(marca):
        raise ValueError("cria_peca: argumento invalido")
    return marca

def cria_copia_peca(arg):
    return cria_peca(arg)

def eh_peca(arg):
    return arg in ["X", "O", ' ']
def pecas_iguais(p1, p2):
    return (
        eh_peca(p1) 
        and eh_peca(p2) 
        and p1 == p2
    )
def peca_para_str(marca):
    return f'[{marca}]'
def peca_para_inteiro(marca):
    if marca == 'X':
        return 1
    elif marca == 'O':
        return -1
    else:
        return 0
def inteiro_para_peca(valor):
    if valor == 1:
        return cria_peca('X')
    elif valor == -1:
        return cria_peca('O')
    else:
        return cria_peca(' ')