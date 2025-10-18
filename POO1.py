class Usuario:
    def __init__(self, nomeEntrada, dtNascEntrada, filhosEntrada):
        self.nome = nomeEntrada   
        self.dtNasc = dtNascEntrada 
        self.filhos = filhosEntrada  
    

user01= Usuario("JP", "00/00/0000", 2)

print(f"Nome: {user01.nome}")
print(f"Modelo: {user01.dtNasc}")
print(f"Filhos: {user01.filhos}")

user02 = Usuario("Maria", "00/00/0000", 3)