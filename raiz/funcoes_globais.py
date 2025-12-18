from modelos.tabuleiro import *

# ------------------------- FUNcoES AUXILIARES GENeRICAS -------------------------
def obter_todas_posicoes_ordenadas():
    """Retorna todas as posicoes do tabuleiro na ordem de leitura"""
    posicoes = []
    for linha in range(1, TAMANHO_TABULEIRO + 1):
        for col in range(1, TAMANHO_TABULEIRO + 1):
            pos = cria_posicao(
                index_para_alpha(col), 
                str(linha)
            )
            posicoes.append(pos)
    return tuple(posicoes)

def obter_cantos_gen():
    """Retorna os cantos do tabuleiro de forma generica"""
    if TAMANHO_TABULEIRO < 1:
        return ()
    
    primeira_col = index_para_alpha(1)
    ultima_col = index_para_alpha(TAMANHO_TABULEIRO)
    primeira_linha = '1'
    ultima_linha = str(TAMANHO_TABULEIRO)
    
    cantos = [
        cria_posicao(primeira_col, primeira_linha),  # canto superior esquerdo
        cria_posicao(primeira_col, ultima_linha),    # canto inferior esquerdo
        cria_posicao(ultima_col, primeira_linha),    # canto superior direito
        cria_posicao(ultima_col, ultima_linha)       # canto inferior direito
    ]
    
    return tuple(cantos)

def obter_centro_gen():
    """Retorna a posicao central do tabuleiro (ou a mais proxima se tamanho par)"""
    if TAMANHO_TABULEIRO < 1:
        return None
    
    # Para tabuleiros impares, ha um centro exato
    if TAMANHO_TABULEIRO % 2 == 1:
        centro_idx = (TAMANHO_TABULEIRO + 1) // 2
        col_centro = index_para_alpha(centro_idx)
        linha_centro = str(centro_idx)
        return cria_posicao(col_centro, linha_centro)
    
    # Para tabuleiros pares, retorna a posicao mais central (ex: para 4x4, retorna b2)
    centro_idx = TAMANHO_TABULEIRO // 2
    col_centro = index_para_alpha(centro_idx)
    linha_centro = str(centro_idx)
    return cria_posicao(col_centro, linha_centro)

def obter_laterais_gen():
    """Retorna posicoes laterais (nao cantos, nao centro) de forma generica"""
    todas_pos = obter_todas_posicoes_ordenadas()
    cantos = set(obter_cantos_gen())
    centro = obter_centro_gen()
    
    laterais = []
    for pos in todas_pos:
        # Nao e canto
        if pos in cantos:
            continue
        # Nao e centro
        if centro and posicoes_iguais(pos, centro):
            continue
        laterais.append(pos)
    
    return tuple(laterais)

def obter_posicoes_prioridade(tab, peca):
    """
    Retorna posicoes em ordem de prioridade para a fase de colocacao
    Seguindo: vitoria -> bloqueio -> centro -> cantos -> laterais
    """
    adversario = cria_peca('O') if peca_para_str(peca) == '[X]' else cria_peca('X')
    
    # 1. VIToRIA
    for pos in obter_todas_posicoes_ordenadas():
        if eh_posicao_livre(tab, pos):
            tab_teste = cria_copia_tabuleiro(tab)
            coloca_peca(tab_teste, peca, pos)
            if not pecas_iguais(obter_ganhador(tab_teste), cria_peca(' ')):
                return pos
    
    # 2. BLOQUEIO
    for pos in obter_todas_posicoes_ordenadas():
        if eh_posicao_livre(tab, pos):
            tab_teste = cria_copia_tabuleiro(tab)
            coloca_peca(tab_teste, adversario, pos)
            if not pecas_iguais(obter_ganhador(tab_teste), cria_peca(' ')):
                return pos
    
    # 3. CENTRO
    centro = obter_centro_gen()
    if centro and eh_posicao_livre(tab, centro):
        return centro
    
    # 4. CANTOS
    for canto in obter_cantos_gen():
        if eh_posicao_livre(tab, canto):
            return canto
    
    # 5. LATERAIS
    for lateral in obter_laterais_gen():
        if eh_posicao_livre(tab, lateral):
            return lateral
    
    # Fallback: primeira posicao livre (em ordem de leitura)
    for pos in obter_todas_posicoes_ordenadas():
        if eh_posicao_livre(tab, pos):
            return pos
    
    return None

# ------------------------- FASE DE COLOCAcaO AUTO -------------------------
def fase_colocacao_auto(tab, peca):
    """
    Implementa a estrategia automatica da fase de colocacao de forma generica.
    Funciona para qualquer tamanho de tabuleiro definido em TAMANHO_TABULEIRO.
    """
    return obter_posicoes_prioridade(tab, peca)

# ------------------------- ALGORITMO MINIMAX -------------------------
def minimax(tab, peca, profundidade, seq_movimentos=None):
    """
    Algoritmo minimax recursivo para escolher o melhor movimento.
    Retorna (valor, sequencia_de_movimentos)
    """
    if seq_movimentos is None:
        seq_movimentos = []
    
    # Verificar terminal ou profundidade maxima
    ganhador = obter_ganhador(tab)
    if not pecas_iguais(ganhador, cria_peca(' ')) or profundidade == 0:
        valor = peca_para_inteiro(ganhador)
        return valor, seq_movimentos
    
    adversario = cria_peca('O') if peca_para_str(peca) == '[X]' else cria_peca('X')
    
    # Inicializar melhor resultado
    melhor_resultado = -float('inf') if peca_para_str(peca) == '[X]' else float('inf')
    melhor_seq = []
    
    # Obter todas as posicoes do jogador atual
    pos_jogador = obter_posicoes_jogador(tab, peca)
    
    # Explorar todos os movimentos possiveis
    for pos_origem in pos_jogador:
        pos_adjacentes = obter_posicoes_adjacentes(pos_origem)
        
        for pos_destino in pos_adjacentes:
            if eh_posicao_livre(tab, pos_destino):
                # Criar novo tabuleiro com o movimento
                novo_tab = cria_copia_tabuleiro(tab)
                move_peca(novo_tab, pos_origem, pos_destino)
                
                # Chamada recursiva
                movimento = (pos_origem, pos_destino)
                novo_resultado, nova_seq = minimax(
                    novo_tab, adversario, profundidade - 1, 
                    seq_movimentos + [movimento]
                )
                
                # Avaliar resultado (MAX para X, MIN para O)
                if peca_para_str(peca) == '[X]':  # Jogador X quer maximizar
                    if novo_resultado > melhor_resultado or not melhor_seq:
                        melhor_resultado = novo_resultado
                        melhor_seq = [movimento] + nova_seq[:1]  # manter so primeiro movimento
                else:  # Jogador O quer minimizar
                    if novo_resultado < melhor_resultado or not melhor_seq:
                        melhor_resultado = novo_resultado
                        melhor_seq = [movimento] + nova_seq[:1]
    
    # Se nao houver movimentos (pecas bloqueadas)
    if not melhor_seq and pos_jogador:
        # Retornar movimento "passar" (mover para mesma posicao)
        primeira_pos = pos_jogador[0]
        return 0, [(primeira_pos, primeira_pos)]
    
    return melhor_resultado, melhor_seq

# ------------------------- FUNcaO AUXILIAR MOVIMENTO FaCIL -------------------------
def movimento_facil(tab, peca):
    """
    Implementa a estrategia de nivel facil na fase de movimento:
    - Move a primeira peca que tenha uma posicao adjacente livre
    - Para a primeira posicao adjacente livre encontrada
    """
    pos_jogador = obter_posicoes_jogador(tab, peca)
    
    for pos_origem in pos_jogador:
        pos_adjacentes = obter_posicoes_adjacentes(pos_origem)
        
        for pos_destino in pos_adjacentes:
            if eh_posicao_livre(tab, pos_destino):
                return pos_origem, pos_destino
    
    # Se nao houver movimento possivel (todas bloqueadas)
    if pos_jogador:
        primeira_pos = pos_jogador[0]
        return primeira_pos, primeira_pos
    
    return None, None

# ------------------------- FUNcaO AUXILIAR MOVIMENTO NORMAL -------------------------
def movimento_normal(tab, peca):
    """
    Implementa a estrategia de nivel normal na fase de movimento:
    - Usa minimax com nivel normal
    - Se nao houver movimento de vitoria, usa estrategia facil
    """
    # Primeiro verificar se ha movimento de vitoria imediata
    pos_jogador = obter_posicoes_jogador(tab, peca)
    
    for pos_origem in pos_jogador:
        pos_adjacentes = obter_posicoes_adjacentes(pos_origem)
        
        for pos_destino in pos_adjacentes:
            if eh_posicao_livre(tab, pos_destino):
                # Testar movimento
                novo_tab = cria_copia_tabuleiro(tab)
                move_peca(novo_tab, pos_origem, pos_destino)
                
                if not pecas_iguais(obter_ganhador(novo_tab), cria_peca(' ')):
                    return pos_origem, pos_destino

    _, movimentos = minimax(tab, peca, NIVEIS['normal'])
    
    if movimentos and len(movimentos) > 0:
        primeiro_movimento = movimentos[0]
        if isinstance(primeiro_movimento, tuple) and len(primeiro_movimento) == 2:
            return primeiro_movimento
    
    # Fallback: usar estrategia facil
    return movimento_facil(tab, peca)

def obter_movimento_auto(tabuleiro, peca, nivel):
    """ obter_movimento_auto: tabuleiro x peca x str -> tuplo
    Devolve um tuplo com a posicao ou movimento escolhida automaticamente pelo computador."""
    # se for fase de colocacao
    if len(obter_posicoes_jogador(tabuleiro, peca)) < PECAS_POR_JOGADOR:
        pos = fase_colocacao_auto(tabuleiro, peca)
        return (pos,)
    elif nivel == 'facil':
        # Nivel facil: movimento simples
        return movimento_facil(tabuleiro, peca)
    elif nivel == 'normal':
        # Nivel normal: movimento normal
        return movimento_normal(tabuleiro, peca)
    elif nivel == 'dificil':
        # Nivel dificil: minimax com profundidade 2
        jogador = 'X' if pecas_iguais(peca, cria_peca('X')) else 'O'
        res = minimax(tabuleiro, jogador, NIVEIS[nivel])
        
        if res[1]:
            return res[1][0]  # Retorna primeiro movimento da sequencia
        else:
            return movimento_facil(tabuleiro, peca)  # Fallback para nivel facil

def obter_movimento_manual(tab, peca):
    """ obter_movimento_manual: tabuleiro x peca -> tuplo
    Devolve um tuplo com a posicao escolhida pelo jogador."""

    pecas_jogador = obter_posicoes_jogador(tab, peca)
    
    try:
        if len(pecas_jogador) < PECAS_POR_JOGADOR:
            escolha = input('Turno do jogador. Escolha uma posicao: ')
            pos = str_para_posicao(escolha)
            if not eh_posicao_livre(tab, pos):
                raise ValueError
            return (pos,)
        else:
            escolha = input('Turno do jogador. Escolha um movimento: ')
            partes = [escolha[:2], escolha[2:]] # divide em posicao inicial e final
            print (partes)
            if len(partes) != 2:
                raise ValueError
            pos_inicial = str_para_posicao(partes[0])
            pos_final = str_para_posicao(partes[1])
            if not (obter_peca(tab, pos_inicial) == peca and eh_posicao_livre(tab, pos_final) and
                    pos_final in obter_posicoes_adjacentes(pos_inicial)):
                raise ValueError
            return (partes[0], partes[1])
    except:
        raise ValueError("obter_movimento_manual: escolha invalida")
    

def moinho(peca_humano, nivel):
    """ moinho: str x str -> str
    Inicia um jogo de moinho entre o jogador humano e o computador."""
    
    peca_humano = str_para_peca(peca_humano)
    # Verificar argumentos
    if not eh_peca(peca_humano) or nivel not in NIVEIS:
        raise ValueError("moinho: argumentos invalidos")
    
    tabuleiro = cria_tabuleiro()
    peca_computador = cria_peca('O') if pecas_iguais(peca_humano, cria_peca('X')) else cria_peca('X')
    jogador_atual = cria_peca('X')
    
    print("Bem-vindo ao JOGO DO MOINHO. Nivel de dificuldade " + nivel + ".")
    print(tabuleiro_para_str(tabuleiro))
    
    # Loop infinito - jogo so termina quando algue ganha
    while True:
        if pecas_iguais(jogador_atual, peca_humano):
            movimento = obter_movimento_manual(tabuleiro, jogador_atual)
        else:
            print("Turno do computador (" + nivel + "):")
            movimento = obter_movimento_auto(tabuleiro, jogador_atual, nivel)
        
        # Aplicar movimento
        if len(movimento) == 1:
            coloca_peca(tabuleiro, jogador_atual, movimento[0])
        else:
            pos_inicial, pos_final = movimento
            move_peca(tabuleiro, pos_inicial, pos_final)
        
        print(tabuleiro_para_str(tabuleiro))
        
        ganhador = obter_ganhador(tabuleiro)
        if not pecas_iguais(ganhador, cria_peca(' ')):
            ganhador_str = peca_para_str(ganhador)
            print(ganhador_str)
            return ganhador_str  # '[X]' ou '[O]'
        
        jogador_atual = peca_computador if pecas_iguais(jogador_atual, peca_humano) else peca_humano