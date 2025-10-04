import Usuario as us

nome = input("Nome: ")
dataNasc = input("Data de nascimento: ").strip()
dd = dataNasc[0:2]
mm = dataNasc[3:5]
aaaa = dataNasc[6:10]

data_formatada = "/".join([dd, mm, aaaa])
qntFilhos = int(input("Qnt de filhos: "))

if (qntFilhos <0):
            raise Exception("Idade não validada")

user01= us.Usuario(nome, data_formatada, qntFilhos)

user01.CadastrarUsuario()
user01.apresentar()