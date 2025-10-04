class Usuario:
    def __init__(self, nome, dtNasc, filhos):
        self.nome = nome   
        self.dtNasc = dtNasc 
        self.filhos = filhos  
    

user01= Usuario("JP", "00/00/0000", 2)

print(f"Nome: {user01.nome}")
print(f"Modelo: {user01.dtNasc}")
print(f"Filhos: {user01.filhos}")
