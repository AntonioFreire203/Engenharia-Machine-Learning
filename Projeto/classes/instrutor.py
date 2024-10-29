#Classe Instrutor 
class Instrutor:
    #Metodo construtor para inicializar atributos 
    def __init__(self,nome:str,sobrenome:str,data_nascimento:str,endereco:str,telefone:str,id=None):
        self.nome =nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.telefone = telefone
        self.id = id
    