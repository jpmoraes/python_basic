import Usuario as us

class Admin(us.Usuario):
    def __init__(self):
        super().__init__()  # herda atributos de Usuario
        self.__senha = None  # atributo privado da subclasse

    # Getter
    @property
    def senha_admin(self):
        return self.__senha

    # Setter
    @senha_admin.setter
    def senha_admin(self, nova_senha):
        self.__senha = nova_senha

    def apresentar(self):
        print(f"Olá, Admin {self.nome_usuario}, seja bem-vindo!")

    def criar_senha(self, nome, senha):
        if nome in us.Usuario.dic_usuarios:
            us.Usuario.dic_usuarios[nome]["senha"] = senha
            print(f"Senha criada para o admin {nome}.")
        else:
            print("Usuário não encontrado.")
