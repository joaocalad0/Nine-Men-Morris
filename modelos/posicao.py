# João Calado - 24295

def cria_posicao(column: str, row: str):
    if (not column.isalpha()) or (not str(row).isdigit()):
        raise ValueError("cria_posicao: argumentos invalidos")
    return {"row": int(row), "column": column.lower()}

def cria_copia_posicao(pos):
    return cria_posicao(obter_pos_c(pos), obter_pos_l(pos))

def obter_pos_c(pos):
    return pos["column"]

def obter_pos_l(pos):
    return str(pos["row"])

def eh_posicao(arg):
    return isinstance(arg, dict) and "row" in arg and "column" in arg

def posicoes_iguais(p1, p2):
    return (
        eh_posicao(p1) 
        and eh_posicao(p2) 
        and p1["row"] == p2["row"] 
        and p1["column"] == p2["column"]
    )

def posicao_para_str(pos):
    return f'{obter_pos_c(pos)}{obter_pos_l(pos)}'

def obter_posicoes_adjacentes(pos):
    # retorna um tuplo com as posicoes adjacentes
    pass