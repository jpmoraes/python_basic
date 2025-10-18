import Usuario as us

nome = input("Nome: ")
dataNasc = input("Data de nascimento: ").strip()
dd = dataNasc[0:2]
mm = dataNasc[2:4]
aaaa = dataNasc[4:8]

data_formatada = "/".join([dd, mm, aaaa])
qntFilhos = int(input("Qnt de filhos: "))

if (qntFilhos <0):
            raise Exception("Qnt de filhos não valido")

# CRIA O OBJETO
user01 = us.Usuario()

# ATRIBUI VALORES AOS ATRIBUTOS
user01.nome_usuario = nome
user01.dtNasc = data_formatada
user01.filhos = qntFilhos

# CHAMA OS MÉTODOS
user01.cadastrar_usuario()
user01.apresentar()

# BUSCA UM USUÁRIO
nomeBuscado = input("Qual nome você busca? ").strip()
dadosEncontrados = user01.listar_usuario(nomeBuscado)

if dadosEncontrados:
    print(f"Data de nascimento encontrada: {dadosEncontrados}")
