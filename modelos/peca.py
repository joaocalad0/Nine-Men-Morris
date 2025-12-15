# Marco Francisco - 26963
# Joao Calado - 24295

# Função que cria uma "peca" se for valida.
# Aceita apenas 'X', 'O' ou ' '
def cria_peca(marca):
    if not eh_peca(marca):
        raise ValueError("cria_peca: argumento invalido")
    return marca # Retorna a marca se valida

# Cria uma copia da peca recebida.
# Neste caso, como as peças são imutaveis, equivalente a retornar o mesmo valor.
def cria_copia_peca(arg):
    return cria_peca(arg)

#Verifica se o argumento e uma peca valida ('X', 'O' ou ' ').
def eh_peca(arg):
    return arg in ["X", "O", ' ']

# Compara duas pecas para ver se sao iguais.
# Apenas retorna True se ambos forem peças validas e iguais.
def pecas_iguais(p1, p2):
    return (
        eh_peca(p1) 
        and eh_peca(p2) 
        and p1 == p2
    )

#converte a peca para string
def peca_para_str(marca):
    return f'[{marca}]'


#converte a peca para int
def peca_para_inteiro(marca):
    if marca == 'X':
        return 1
    elif marca == 'O':
        return -1
    else:
        return 0


#Converte um int de volta para peca:
# 1 -> 'X', -1 -> 'O', 0 -> ' '
def inteiro_para_peca(valor):
    if valor == 1:
        return cria_peca('X')
    elif valor == -1:
        return cria_peca('O')
    else:
        return cria_peca(' ')