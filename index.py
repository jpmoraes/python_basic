dic = {}

def CadastrarUsuario():

  nome = input("Nome: ")
  dataNasc = input("Data de nascimento: ").strip()

  dd = dataNasc[0:2]
  mm = dataNasc[3:5]
  aaaa = dataNasc[6:10]

  data_formatada = "/".join([dd, mm, aaaa])

  qntFilhos = int(input("Qnt de filhos: "))

  if (qntFilhos <0):
      raise Exception("Idade não validada")

  dic[nome] = {"data_nasc": data_formatada, "qntFilhos": qntFilhos}


def ListarUsuario(nome):
    try:
      nomeEncontrado = dic[nome]
    except (KeyError):
      print("Nome não existente")
    else:
      return nomeEncontrado
    finally:
      print("Operação concluída")
    

while True:
  print("1. Cadastrar Usuário ")
  print("2. Buscar Usuário ")
  print("0. Sair")

  op = int(input())

  if(op == 1):
    CadastrarUsuario()
  elif(op == 2):

    nome = input("Qual nome você busca? ")

    resultado = ListarUsuario(nome)

    print(f"Dados encotrados: {resultado}")

  elif(op == 0):
    break
  else:
    print(dic)