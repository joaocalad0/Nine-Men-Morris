# Joao Calado - 24295
# Marco Francisco - 26963
from raiz.utils import alpha_para_index, index_para_alpha
from raiz.constantes import *


# Cria posicao no tabuleiro a partir de coluna e linha
# Garante que posicao valida antes de criar
def cria_posicao(coluna, linha):
    if (not eh_posicao([coluna, linha])):
        raise ValueError("cria_posicao: argumentos invalidos")
    return [coluna.lower(), linha]


#cria uma cópia de uma posicao
#converte dict para list
def cria_copia_posicao(pos):
    if(type(pos) == dict): pos = list(pos.values())
    return cria_posicao(pos[0], pos[1])


#retorna a coluna de uma posicao
def obter_pos_c(pos):
    return pos[0]

#retorna a linha de uma posicao como string
def obter_pos_l(pos):
    return str(pos[1])


#garante que o argumento da posicao e valida
def eh_posicao(arg):
    return ( isinstance(arg, list) and arg[0].isalpha() and str(arg[1]).isdigit() 
    and alpha_para_index(arg[0]) > 0 and alpha_para_index(arg[0]) <= TAMANHO_TABULEIRO 
    and int(arg[1]) > 0 and int(arg[1]) <= TAMANHO_TABULEIRO )


#Compara duas posicoes para ver se sao iguais
#apenas retorna True se ambas forem posicoes validas e tiverem mesma coluna e linha
def posicoes_iguais(p1, p2):
    return (
        eh_posicao(p1) 
        and eh_posicao(p2) 
        and p1[0] == p2[0] 
        and p1[1] == p2[1]
    )


#converte uma posicao para string no formato "A1", "B2",
def posicao_para_str(pos):
    return f'{obter_pos_c(pos)}{obter_pos_l(pos)}'



def str_para_posicao(s):
    if (len(s) != 2):
        raise ValueError("str_para_posicao: argumento invalido")
    coluna = s[0]
    linha = s[1]
    if (not eh_posicao([coluna, linha])):
        raise ValueError("str_para_posicao: argumento invalido")
    return cria_posicao(coluna, linha)



def obter_posicoes_adjacentes(pos):
    # retorna um tuplo com as posicoes adjacentes
    col = alpha_para_index(obter_pos_c(pos))
    li = int(obter_pos_l(pos))
    posicoes_adj = [[col, li - 1], [col - 1, li], [col, li + 1], [col + 1, li]] # a ordem importa
    resultado = []
    for p in posicoes_adj:  
        if(p[0] >= 1 and p[0] <= TAMANHO_TABULEIRO and p[1] >= 1 and p[1] <= TAMANHO_TABULEIRO):
            resultado.append( cria_posicao(index_para_alpha(p[0]), str(p[1])) )
        
    return tuple(resultado)