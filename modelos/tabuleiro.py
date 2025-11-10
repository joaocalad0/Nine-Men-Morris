# Marco Francisco - 26963
#a   b   c\n1 [X]-[ ]-[ ]\n   | \ | / |\n2 [ ]-[ ]-[ ]\n   | / | \ |\n3 [ ]-[ ]-[ ]
import main.constantes as const
    
def alpha_para_index(alpha: str): 
    return ord(alpha) - ord('a')

def index_para_alpha(index: int):
    return chr(ord('a') + index)

def cria_tabuleiro():
    return tuple(
        [ ' ' for _ in range(const.TAMANHO_TABULEIRO) ] for _ in range(const.TAMANHO_TABULEIRO)
    )

def cria_copia_tabuleiro(tab):
    novo_tab = cria_tabuleiro()
    for i in range(const.TAMANHO_TABULEIRO):
        for j in range(const.TAMANHO_TABULEIRO):
            novo_tab[i][j] = tab[i][j]
    return novo_tab

def obter_peca(tab, pos):
    return tab[pos["row"] - 1][alpha_para_index(pos["column"])]

def obter_vetor(tab, value):
    if not value.isdigit() and not value.isalpha(): return False
    if value.isalpha():
        index = alpha_para_index(value)
        return tuple( tab[i][index] for i in range(const.TAMANHO_TABULEIRO) )
    else:
        row = int(value) - 1
        return tuple( tab[row][i] for i in range(const.TAMANHO_TABULEIRO) )
    
def coloca_peca(tab, peca, pos):
    pass
def remove_peca(tab, pos):
    pass
def move_peca(tab, pos_from, pos_to):
    pass
def eh_tabuleiro(arg):
    return isinstance(arg, tuple) and len(arg) == const.TAMANHO_TABULEIRO and all(
        isinstance(linha, list) and len(linha) == const.TAMANHO_TABULEIRO for linha in arg
    )
def eh_posicao_livre(tab, pos):
    return obter_peca(tab, pos) == ' '
def tabuleiros_iguais(tab1, tab2):
    return (
        eh_tabuleiro(tab1) 
        and eh_tabuleiro(tab2) 
        and all(
            tab1[i][j] == tab2[i][j] 
            for i in range(const.TAMANHO_TABULEIRO) 
            for j in range(const.TAMANHO_TABULEIRO)
        )
    )
def tabuleiro_para_str(tab):
    output = '   ' + ( '   '.join(index_para_alpha(i) for i in range(const.TAMANHO_TABULEIRO)) ) + '\n'
    for row in range(const.TAMANHO_TABULEIRO):
        output += str(row + 1) + ' '
        for col in range(const.TAMANHO_TABULEIRO):
            piece = tab[row][col]
            output += f'[{piece}]'
            if col < const.TAMANHO_TABULEIRO - 1:
                output += '-'
        output += '\n'
        if row < const.TAMANHO_TABULEIRO - 1:
            output += '   '
            for col in range(const.TAMANHO_TABULEIRO):
                output += ' | '
                if col < const.TAMANHO_TABULEIRO - 1:
                    output += '\\ / ' if row % 2 == 0 else '/ \\ '
            output += '\n'
    return output
def tuplo_para_tabuleiro(tuplo):
    novo_tab = cria_tabuleiro()
    for i in range(const.TAMANHO_TABULEIRO):
        for j in range(const.TAMANHO_TABULEIRO):
            novo_tab[i][j] = tuplo[i][j]
    return novo_tab
def obter_ganhador(tab):
    pass
def obter_posicoes_livres(tab):
    pass
def obter_posicoes_jogador(tab, peca):
    pass