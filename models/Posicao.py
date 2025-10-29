# João Calado - 24295

class Posicao:
    def __init__ (self,line: str, column: str):
        if (line != "A" and line != "B" and line != "C") or (column != "1" and column != "2" and column != "3"):
            raise ValueError("cria_posicao: argumentos invalidos")

        self.line = line
        self.column = column


    def cria_copia_posicao(self):
        return Posicao(self.line, self.column)


    def obter_pos_c(self):
        return self.column


    def obter_pos_l(self):
        return self.line


    def eh_posicao(arg):
        if isinstance(arg, posicao):
            return True
        else:
            return False

    def posicoes_iguais(p1, p2):
        if isinstance(p1, posicao) and isinstance(p2, posicao):
            if p1.line == p2.line and p1.column == p2.column:
               return True
            else:
                return False
        else:
            return False


    def posicao_para_str(p):
        if isinstance(p, posicao):
            s = p.column + p.line
            return s
        else:
            raise ValueError("posicao_para_str: argumentos invalidos")

