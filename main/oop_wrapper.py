import models.Position as Position


#Posicao
def cria_posicao(c,l):
    return Position.Position(c,l)
def cria_copia_posicao(p):
    return p.createPositionCopy(p.line, p.column)
def obter_pos_c(p):
    return p.getPosCol(p)
def obter_pos_l(p):
    return p.getPosRow(p)
def eh_posicao(arg):
    return arg.isPosicao(arg)
def posicoes_iguais(p1, p2):
    return p1,p2.arePositionsEqual(p1, p2)
def posicao_para_str(p):
    return p.positionToStr(p)

#Peca
def cria_peca(s):
    return s.createPice(s)
def criar_copia_peca(j):
    return j.createPieceCopy(j)
def eh_peca(arg):
    return arg.isPiece(arg)
def pecas_iguais(j1,j2):
    return j1,j2.arePiecesEqual(j1,j2)
def peca_para_str(j):
    return j.pieceToStr(j)
def peca_para_inteiro(j):
    return j.pieceToInteger(j)

#Tabuleiro