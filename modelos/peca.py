
def cria_peca(marca: str):
    peca = {"marca": marca}
    if not eh_peca(peca):
        raise ValueError("cria_peca: argumento invalido")
    return peca
def cria_copia_peca(peca):
    return cria_peca(peca["marca"])
def eh_peca(arg):
    return "marca" in arg and arg["marca"] in ["X", "O", ' ']
def pecas_iguais(p1, p2):
    return (
        eh_peca(p1) 
        and eh_peca(p2) 
        and p1["marca"] == p2["marca"]
    )
def peca_para_str(peca):
    return f'[{peca["marca"]}]'
def peca_para_inteiro(peca):
    return (1 if peca["marca"] == 'X' 
            else 
                (-1 if peca["marca"] == 'O' 
                 else 0)
            )