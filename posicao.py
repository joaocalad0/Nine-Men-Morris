from logging import exception
from turtledemo.chaos import line


# João Calado - 24295

class posicao:
    def cria_posicao(self,line: str, column: str):
        if (line != "A" and line != "B" and line != "C") or (column != "1" and column != "2" and column != "3"):
            raise ValueError("cria_posicao: argumentos invalidos")

        self.line = line
        self.column = column


    def cria_copia_posicao(self):

        return posicao(self.line, self.column)


    def obter_pos_c(self):
        return self.column


    def obter_pos_l(self):
        return self.line