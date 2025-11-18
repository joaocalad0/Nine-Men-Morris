# Marco Francisco - 26963
#a   b   c\n1 [X]-[ ]-[ ]\n   | \ | / |\n2 [ ]-[ ]-[ ]\n   | / | \ |\n3 [ ]-[ ]-[ ]
from raiz.utils import alpha_para_index, index_para_alpha
from raiz.constantes import *

from modelos.posicao import *
from modelos.peca import *
    
def cria_tabuleiro():
    return [
        [ ' ' for _ in range(TAMANHO_TABULEIRO) ] for _ in range(TAMANHO_TABULEIRO)
    ]

def cria_copia_tabuleiro(tab):
    novo_tab = cria_tabuleiro()
    for i in range(TAMANHO_TABULEIRO):
        for j in range(TAMANHO_TABULEIRO):
            novo_tab[i][j] = tab[i][j]
    return novo_tab

def obter_peca(tab, pos):
    return tab[int(obter_pos_l(pos)) - 1][alpha_para_index(obter_pos_c(pos)) - 1]

def obter_vetor(tab, valor):
    if not valor.isdigit() and not valor.isalpha(): return False
    if valor.isalpha():
        col = alpha_para_index(valor) - 1
        return tuple( tab[i][col] for i in range(TAMANHO_TABULEIRO) )
    else:
        linha = int(valor) - 1    
        return tuple( tab[linha][i] for i in range(TAMANHO_TABULEIRO) )
    
def coloca_peca(tab, peca, pos):
    tab[int(obter_pos_l(pos)) - 1][alpha_para_index(obter_pos_c(pos)) - 1] = peca
    return tab
def remove_peca(tab, pos):
    tab[int(obter_pos_l(pos)) - 1][alpha_para_index(obter_pos_c(pos)) - 1] = ' '
    return tab
def move_peca(tab, pos_antes, pos_depois):
    peca = obter_peca(tab, pos_antes)
    tab = remove_peca(tab, pos_antes)
    tab = coloca_peca(tab, peca, pos_depois)
    return tab
def eh_tabuleiro(arg):
    return isinstance(arg, tuple) and len(arg) == TAMANHO_TABULEIRO and all(
        isinstance(linha, list) and len(linha) == TAMANHO_TABULEIRO 
        for linha in arg
    )

def eh_posicao_livre(tab, pos):
    return obter_peca(tab, pos) == ' '

def tabuleiros_iguais(tab1, tab2):
    return (
        eh_tabuleiro(tab1) 
        and eh_tabuleiro(tab2) 
        and all(
            tab1[i][j] == tab2[i][j] 
            for i in range(TAMANHO_TABULEIRO) 
            for j in range(TAMANHO_TABULEIRO)
        )
    )
def tabuleiro_para_str(tab):
    tab_car_count = 0
    resultado = '   ' + ( '   '.join(index_para_alpha(i + 1) for i in range(TAMANHO_TABULEIRO)) ) + '\n'
    for linha in range(TAMANHO_TABULEIRO):
        resultado += str(linha + 1) + ' '
        for col in range(TAMANHO_TABULEIRO):
            piece = tab[linha][col]
            resultado += f'[{piece}]'
            if col < TAMANHO_TABULEIRO - 1:
                resultado += '-'
        if linha < TAMANHO_TABULEIRO - 1:
            resultado += '\n   '
            resultado += TABULEIRO_CAR[tab_car_count]
            tab_car_count += 1
    return resultado
def tuplo_para_tabuleiro(tuplo):
    novo_tab = cria_tabuleiro()
    for i in range(TAMANHO_TABULEIRO):
        for j in range(TAMANHO_TABULEIRO):
            novo_tab[i][j] = inteiro_para_peca(tuplo[i][j]) if type(tuplo[i][j]) == int else tuplo[i][j]
    return novo_tab
def obter_ganhador(tab):
    soma_linhas = [0 for _ in range(TAMANHO_TABULEIRO)]
    soma_colunas = [0 for _ in range(TAMANHO_TABULEIRO)]
    soma_diagonal1 = 0
    soma_diagonal2 = 0

    for i in range(TAMANHO_TABULEIRO):
        for j in range(TAMANHO_TABULEIRO):
            valor = peca_para_inteiro(obter_peca(tab, cria_posicao(index_para_alpha(j + 1), str(i + 1))))
            soma_linhas[i] += valor
            soma_colunas[j] += valor
            if i == j:
                soma_diagonal1 += valor
            if i + j == TAMANHO_TABULEIRO - 1:
                soma_diagonal2 += valor

    todas_somas = soma_linhas + soma_colunas + [soma_diagonal1, soma_diagonal2]

    if 3 in todas_somas:
        return cria_peca('X')
    elif -3 in todas_somas:
        return cria_peca('O')
    else:
        return cria_peca(' ')
def obter_posicoes_livres(tab) -> tuple:
    res = []
    for i in range(TAMANHO_TABULEIRO):
        for j in range(TAMANHO_TABULEIRO):
            pos = cria_posicao(index_para_alpha(j + 1), str(i + 1))
            if eh_posicao_livre(tab, pos):
                res.append(pos)
    return tuple(res)
def obter_posicoes_jogador(tab, peca):
    res = []
    for i in range(TAMANHO_TABULEIRO):
        for j in range(TAMANHO_TABULEIRO):
            pos = cria_posicao(index_para_alpha(j + 1), str(i + 1))
            if obter_peca(tab, pos) == peca:
                res.append(pos)
    return tuple(res)