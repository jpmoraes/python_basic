class Usuario:
    def __init__(self, nome, dtNasc, filhos):
        self.nome = nome   
        self.dtNasc = dtNasc 
        self.filhos = filhos

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} nasci em {self.dtNasc}")
    

