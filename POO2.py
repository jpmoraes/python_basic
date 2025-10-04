class Usuario:
    def __init__(self, nome, dtNasc, filhos):
        self.nome = nome   
        self.dtNasc = dtNasc 
        self.filhos = filhos

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} nasci em {self.dtNasc}")
    

user01= Usuario("JP", "00/00/0000", 2)

user01.apresentar()
