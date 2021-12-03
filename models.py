class Jogo:
    def __init__(self, nome, categoria, console, id=None): #id com None fica opcional
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.console = console

class Usuario:
    def __init__(self, id, usuario, senha):
        self.id = id
        self.usuario = usuario
        self.senha = senha
