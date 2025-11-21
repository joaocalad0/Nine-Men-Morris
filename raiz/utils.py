def alpha_para_index(alpha): 
    """Converte uma letra para o índice inteiro correspondente."""
    return ord(alpha) - ord('a') + 1 # 1 = 'a'

def index_para_alpha(index):
    """Converte um índice inteiro para a letra correspondente."""
    return chr(ord('a') + index - 1) # 'a' = 1