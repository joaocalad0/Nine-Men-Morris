from raiz.funcoes_globais import *

p2 = cria_posicao('b','3')
t = tuple(posicao_para_str(p) for p in obter_posicoes_adjacentes(p2))
print(obter_posicoes_adjacentes(p2))