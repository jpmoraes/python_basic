class Usuario:
    def __init__(self, nome, dtNasc, filhos):
        self.nome = nome
        self.dtNasc = dtNasc
        self.filhos = filhos

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} nasci em {self.dtNasc}")

    def CadastrarUsuario(self):
        dic[self.nome] = {"data_nasc":self.dtNasc , "qntFilhos": self.filhos}

    def ListarUsuario(nome):
        try:
            nomeEncontrado = dic[nome]
        except (KeyError):
            print("Nome não existente")
        else:
            return nomeEncontrado
        finally:
            print("Operação concluída")


nome = input("Nome: ")
dataNasc = input("Data de nascimento: ").strip()
dd = dataNasc[0:2]
mm = dataNasc[3:5]
aaaa = dataNasc[6:10]

data_formatada = "/".join([dd, mm, aaaa])
qntFilhos = int(input("Qnt de filhos: "))

if (qntFilhos <0):
            raise Exception("Idade não validada")

user01= Usuario(nome, data_formatada, qntFilhos)

user01.CadastrarUsuario()
user01.apresentar()
