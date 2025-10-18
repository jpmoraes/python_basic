class Usuario:
    dic_usuarios = {}  

    def __init__(self):  # Atributos da instância
        self.__nome = None
        self.dtNasc = None
        self.filhos = None        

    # Getter
    @property
    def nome_usuario(self):
        return self.__nome

    # Setter
    @nome_usuario.setter
    def nome_usuario(self, novo_nome):
        self.__nome = novo_nome

   
    def apresentar(self):
        print(f"Olá, meu nome é {self.__nome} e nasci em {self.dtNasc}")

   
    def cadastrar_usuario(self):
        if self.__nome is None:
            print("Nome do usuário não pode ser None.")
            return
        Usuario.dic_usuarios[self.__nome] = {
            "data_nasc": self.dtNasc,
            "qnt_filhos": self.filhos
        }

    
    def listar_usuario(self, nome):
        try:
            dados_encontrados = Usuario.dic_usuarios[nome]["data_nasc"]
        except KeyError:
            print("Nome não existente.")
        else:
            return dados_encontrados
        finally:
            print("Operação concluída.")
