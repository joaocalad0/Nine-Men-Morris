from modelos.tabuleiro import *

def obter_movimento_manual(tab, peca):
    """ obter_movimento_manual: tabuleiro x peca -> tuplo
    Devolve um tuplo com a posição escolhida pelo jogador."""

    pecas_jogador = obter_posicoes_jogador(tab, peca)
    if len(pecas_jogador) < PECAS_POR_JOGADOR:
        escolha = input('Turno do jogador. Escolha uma posicao: ')
        try:
            pos = str_para_posicao(escolha)
            if not eh_posicao_livre(tab, pos):
                raise ValueError
            return (pos,)
        except:
            raise ValueError("obter_movimento_manual: escolha invalida")
    else:
        escolha = input('Turno do jogador. Escolha um movimento: ')
        try:
            partes = escolha.split()
            if len(partes) != 2:
                raise ValueError
            pos_inicial = str_para_posicao(partes[0])
            pos_final = str_para_posicao(partes[1])
            if not (obter_peca(tab, pos_inicial) == peca and eh_posicao_livre(tab, pos_final) and
                    pos_final in obter_posicoes_adjacentes(pos_inicial)):
                raise ValueError
            return (pos_inicial, pos_final)
        except:
            raise ValueError("obter_movimento_manual: escolha invalida")
def moinho(peca_humano, nivel):
    """ moinho: peca x inteiro -> str
    Inicia um jogo de moinho entre o jogador humano e o computador."""
    if not (pecas_iguais(peca_humano, cria_peca('X')) or pecas_iguais(peca_humano, cria_peca('O'))):
        raise ValueError("moinho: argumentos invalidos")
    tabuleiro = cria_tabuleiro()
    peca_computador = cria_peca('O') if pecas_iguais(peca_humano, cria_peca('X')) else cria_peca('X')
    jogador_atual = cria_peca('X')  # X sempre começa

    while True:
        if pecas_iguais(jogador_atual, peca_humano):
            movimento = obter_movimento_manual(tabuleiro, peca_humano)
        else:
            print(f'Turno do computador ({nivel}):')
            movimento = obter_movimento_auto(tabuleiro, peca_computador, nivel)

        if movimento is None:
            break  # Nenhum movimento possível

        pos_inicial, pos_final = movimento
        move_peca(tabuleiro, pos_inicial, pos_final)

        ganhador = obter_ganhador(tabuleiro)
        if not pecas_iguais(ganhador, cria_peca(' ')):
            return f"Jogador {peca_para_str(ganhador)} ganhou!"

        # Alterna jogador
        jogador_atual = peca_computador if pecas_iguais(jogador_atual, peca_humano) else peca_humano

    return "Empate!"

def valor_tabuleiro(tabuleiro):
    """
    Calcula o valor do tabuleiro para avaliação no minimax
    Retorna +1 se X ganha, -1 se O ganha, 0 caso contrário
    """
    return peca_para_inteiro(obter_ganhador(tabuleiro))
    
def obter_movimento_auto(tabuleiro, peca, nivel):
    """
    Função principal para obter movimento automático conforme o nível
    """
    peca = 'X' if pecas_iguais(peca, cria_peca('X')) else 'O'
    
    if nivel == 'facil':
        return movimento_facil(tabuleiro, peca)
    elif nivel in NIVEIS.keys():
        """
        Nível normal: minimax com profundidade 1
        """
        jogador = 'X' if pecas_iguais(peca, cria_peca('X')) else 'O'
        _, seq_movimentos = minimax(tabuleiro, jogador, NIVEIS[nivel], ())
        
        if seq_movimentos:
            return seq_movimentos[0]  # Retorna primeiro movimento da sequência
        else:
            return movimento_facil(tabuleiro, peca)  # Fallback para nível fácil
    else:
        return None
    
def minimax(tabuleiro, jogador, profundidade, seq_movimentos):
    """
    Implementação do algoritmo minimax para o Jogo do Moinho
    
    Args:
        tabuleiro: estado atual do tabuleiro
        jogador: peça do jogador atual ('X' ou 'O')
        profundidade: nível máximo de recursão
        seq_movimentos: sequência de movimentos realizados até agora
    
    Returns:
        tuple: (valor_do_tabuleiro, sequência_de_movimentos)
    """
    
    # Verifica condição de parada
    ganhador = obter_ganhador(tabuleiro)
    if ganhador is not " " or profundidade == 0:
        valor = valor_tabuleiro(tabuleiro)
        return valor, seq_movimentos
    
    # Inicializa melhor resultado
    if jogador == 'X':
        melhor_resultado = float('-inf')  # X quer maximizar
    else:
        melhor_resultado = float('inf')   # O quer minimizar
    
    melhor_seq_movimentos = None
    
    # Obtém peças do jogador atual
    peca_jogador = cria_peca(jogador)
    posicoes_jogador = obter_posicoes_jogador(tabuleiro, peca_jogador)
    
    # Para cada peça do jogador atual
    for pos_peca in posicoes_jogador:
        # Para cada posição adjacente
        posicoes_adj = obter_posicoes_adjacentes(pos_peca)
        
        for pos_destino in posicoes_adj:
            # Se a posição está livre
            if eh_posicao_livre(tabuleiro, pos_destino):
                # Cria cópia do tabuleiro
                tabuleiro_copia = cria_copia_tabuleiro(tabuleiro)
                
                # Realiza o movimento
                move_peca(tabuleiro_copia, pos_peca, pos_destino)
                
                # Cria novo movimento
                novo_movimento = (pos_peca, pos_destino)
                nova_seq = seq_movimentos + (novo_movimento,)
                
                # Chama recursivamente para o outro jogador
                outro_jogador = 'O' if jogador == 'X' else 'X'
                novo_resultado, nova_seq_completa = minimax(
                    tabuleiro_copia, outro_jogador, profundidade - 1, nova_seq
                )
                
                # Atualiza melhor movimento
                if melhor_seq_movimentos is None:
                    melhor_resultado = novo_resultado
                    melhor_seq_movimentos = nova_seq_completa
                elif jogador == 'X' and novo_resultado > melhor_resultado:
                    melhor_resultado = novo_resultado
                    melhor_seq_movimentos = nova_seq_completa
                elif jogador == 'O' and novo_resultado < melhor_resultado:
                    melhor_resultado = novo_resultado
                    melhor_seq_movimentos = nova_seq_completa
    
    return melhor_resultado, melhor_seq_movimentos

def movimento_facil(tabuleiro, peca):
    """
    Nível fácil: primeira peça com posição adjacente livre
    """
    posicoes = obter_posicoes_jogador(tabuleiro, peca)
    
    for pos in posicoes:
        adjacentes = obter_posicoes_adjacentes(pos)
        for adj in adjacentes:
            if eh_posicao_livre(tabuleiro, adj):
                return (pos, adj)
    
    # Se não há movimentos possíveis, retorna movimento nulo
    if posicoes:
        return (posicoes[0], posicoes[0])
    return None