class Piece:
    def __init__(self,s: str):
        if (s == "X" or s == "O" or s == '  '):
            self.piece = s
        else:
            raise ValueError("cria_peca: argumento invalido")


    def createPieceCopy(j):
        return Piece(j.piece)


    def isPiece(arg):
        return isinstance(arg, Piece)


    def arePiecesEqual(j1, j2):
        return isinstance(j1, Piece) and isinstance(j2, Piece) and j1.pice == j2.piece


    def pieceToStr(j):
        if not(isinstance(j, Piece)):
            raise ValueError("peca_para_str: argumento inválido")
        return f"[{j.piece}]"


    def pieceToInteger(j):
        if not(isinstance(j, Piece)):
            raise ValueError("peca_para_inteiro: argumento inválido")
        if j.piece not in ["X", "O", ' ']:
            raise ValueError("peca_para_inteiro: argumento invalido")
        return 1 if j.piece == 'X' else -1 if j.piece == 'O' else 0
