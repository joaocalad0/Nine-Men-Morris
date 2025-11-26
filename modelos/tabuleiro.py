# Marco Francisco - 26963
from raiz.utils import alpha_para_index, index_para_alpha
from raiz.constantes import *

from modelos.posicao import *
from modelos.peca import *
    
def cria_tabuleiro():
    """ cria_tabuleiro: {} -> tabuleiro
    Cria um tabuleiro vazio."""
    return [
        [ ' ' for _ in range(TAMANHO_TABULEIRO) ] for _ in range(TAMANHO_TABULEIRO)
    ]

def cria_copia_tabuleiro(tab):
    """ cria_copia_tabuleiro: tabuleiro -> tabuleiro
    Cria uma cópia do tabuleiro."""
    novo_tab = cria_tabuleiro()
    for i in range(TAMANHO_TABULEIRO):
        for j in range(TAMANHO_TABULEIRO):
            novo_tab[i][j] = tab[i][j]
    return novo_tab

def obter_peca(tab, pos):
    """ obter_peca: tabuleiro x posicao -> peca
    Devolve a peça que está na posição pos do tabuleiro."""
    return tab[int(obter_pos_l(pos)) - 1][alpha_para_index(obter_pos_c(pos)) - 1]

def obter_vetor(tab, valor):
    """ obter_vetor: tabuleiro x str -> tuplo
    Devolve o tuplo correspondente à linha ou coluna do tabuleiro."""
    if not valor.isdigit() and not valor.isalpha(): return False
    if valor.isalpha():
        col = alpha_para_index(valor) - 1
        return tuple( tab[i][col] for i in range(TAMANHO_TABULEIRO) )
    else:
        linha = int(valor) - 1    
        return tuple( tab[linha][i] for i in range(TAMANHO_TABULEIRO) )
    
def coloca_peca(tab, peca, pos):
    """ coloca_peca: tabuleiro x peca x posicao -> tabuleiro
    Coloca a peça numa posição do tabuleiro."""
    tab[int(obter_pos_l(pos)) - 1][alpha_para_index(obter_pos_c(pos)) - 1] = peca
    return tab
def remove_peca(tab, pos):
    """ remove_peca: tabuleiro x posicao -> tabuleiro
    Remove a peça de uma posição do tabuleiro."""
    tab[int(obter_pos_l(pos)) - 1][alpha_para_index(obter_pos_c(pos)) - 1] = ' '
    return tab
def move_peca(tab, pos_antes, pos_depois):
    """ move_peca: tabuleiro x posicao x posicao -> tabuleiro
    Move a peça de uma posição para outra no tabuleiro."""
    peca = obter_peca(tab, pos_antes)
    tab = remove_peca(tab, pos_antes)
    tab = coloca_peca(tab, peca, pos_depois)
    return tab
def eh_tabuleiro(arg):
    """ eh_tabuleiro: qualquer -> booleano
    Devolve True se o argumento for um tabuleiro válido e False caso contrário."""
    return isinstance(arg, tuple) and len(arg) == TAMANHO_TABULEIRO and all(
        isinstance(linha, list) and len(linha) == TAMANHO_TABULEIRO 
        for linha in arg
    )

def eh_posicao_livre(tab, pos):
    """ eh_posicao_livre: tabuleiro x posicao -> booleano
    Devolve True se a posição do tabuleiro estiver livre e False caso contrário."""
    return obter_peca(tab, pos) == ' '

def tabuleiros_iguais(tab1, tab2):
    """ tabuleiros_iguais: tabuleiro x tabuleiro -> booleano
    Devolve True se os tabuleiros forem iguais e False caso contrário."""
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
    """ tabuleiro_para_str: tabuleiro -> str
    Devolve a representação em string do tabuleiro."""
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
    """ tuplo_para_tabuleiro: tuplo -> tabuleiro
    Devolve o tabuleiro correspondente ao tuplo dado."""
    novo_tab = cria_tabuleiro()
    for i in range(TAMANHO_TABULEIRO):
        for j in range(TAMANHO_TABULEIRO):
            novo_tab[i][j] = inteiro_para_peca(tuplo[i][j]) if type(tuplo[i][j]) == int else tuplo[i][j]
    return novo_tab
def obter_ganhador(tab):
    """ obter_ganhador: tabuleiro -> peca
    Devolve a peça do jogador que ganhou o jogo ou a peça vazia se não houver vencedor."""
    soma_linhas = [0 for _ in range(TAMANHO_TABULEIRO)]
    soma_colunas = [0 for _ in range(TAMANHO_TABULEIRO)]

    for i in range(TAMANHO_TABULEIRO):
        for j in range(TAMANHO_TABULEIRO):
            valor = peca_para_inteiro(obter_peca(tab, cria_posicao(index_para_alpha(j + 1), str(i + 1))))
            soma_linhas[i] += valor
            soma_colunas[j] += valor

    todas_somas = soma_linhas + soma_colunas # junta todas as listas de somas
    o_peca = cria_peca('O')
    x_peca = cria_peca('X')

    if peca_para_inteiro(x_peca) * PECAS_POR_JOGADOR in todas_somas:
        return x_peca
    elif peca_para_inteiro(o_peca) * PECAS_POR_JOGADOR in todas_somas:
        return o_peca
    else:
        return cria_peca(' ')
def obter_posicoes_livres(tab) -> tuple:
    """ obter_posicoes_livres: tabuleiro -> tuplo
    Devolve um tuplo com as posições livres do tabuleiro."""
    res = []
    for i in range(TAMANHO_TABULEIRO):
        for j in range(TAMANHO_TABULEIRO):
            pos = cria_posicao(index_para_alpha(j + 1), str(i + 1))
            if eh_posicao_livre(tab, pos):
                res.append(pos)
    return tuple(res)
def obter_posicoes_jogador(tab, peca):
    """ obter_posicoes_jogador: tabuleiro x peca -> tuplo
    Devolve um tuplo com as posições ocupadas pela peça do jogador no tabuleiro."""
    res = []
    for i in range(TAMANHO_TABULEIRO):
        for j in range(TAMANHO_TABULEIRO):
            pos = cria_posicao(index_para_alpha(j + 1), str(i + 1))
            if obter_peca(tab, pos) == peca:
                res.append(pos)
    return tuple(res)