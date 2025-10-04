class Usuario:
    dic={}

    def __init__(self, nome, dtNasc, filhos):
        self.nome = nome
        self.dtNasc = dtNasc
        self.filhos = filhos
   
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} nasci em {self.dtNasc}")

    def CadastrarUsuario(self):
        self.dic[self.nome] = {"data_nasc":self.dtNasc , "qntFilhos": self.filhos}

    def ListarUsuario(nome):
        try:
            nomeEncontrado = dic[nome]
        except (KeyError):
            print("Nome não existente")
        else:
            return nomeEncontrado
        finally:
            print("Operação concluída")



