# João Calado - 24295

class Position:
    def __init__ (self,line: str, column: str):
        if (line != "a" and line != "b" and line != "b") or (column != "1" and column != "2" and column != "3"):
            raise ValueError("cria_posicao: argumentos invalidos")

        self.line = line
        self.column = column


    def createPositionCopy(self):
        return Position(self.line, self.column)


    def getPosCol(self):
        return self.column


    def getPosRow(self):
        return self.line


    def isPosicao(arg):
        return isinstance(arg, Position)

    def arePositionsEqual(p1, p2):
        return isinstance(p1, Position) and isinstance(p2, Position) and p1.line == p2.line and p1.column == p2.column


    def positionToStr(p):
        if not isinstance(p, Position):
            raise ValueError("posicao_para_str: argumentos invalidos")
        return p.column + p.line

    def getAdjacentPositions(self):
        pass