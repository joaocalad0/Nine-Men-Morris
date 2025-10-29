import models.Posicao as Posicao

def cria_posicao(c,l):
    return Posicao.Posicao(c,l)
def cria_copia_posicao(p):
    return Posicao.cria_copia_posicao(p.line, p.column)
def obter_pos_c(p):
    return Posicao.obter_pos_c(p)
def obter_pos_l(p):
    return Posicao.obter_pos_l(p)
def eh_posicao(arg):
    return Posicao.eh_posicao(arg)
def posicoes_iguais(p1, p2):
    return Posicao.posicoes_iguais(p1, p2)
def posicao_para_str(p):
    return Posicao.posicao_para_str(p)