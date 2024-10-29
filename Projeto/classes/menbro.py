#Classe Membro
class Membro :
    #Metodo construtor para inicializar atributos 
    def __init__(self,nome:str,sobrenome:str,data_nascimento:str,endereco:str,telefone:str,email:str,tipo_plano:str,data_inicio:str,ativo:str,id:int=None):
        self.nome =nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.tipo_plano = tipo_plano
        self.data_inicio = data_inicio
        self.ativo = ativo
        self.id = id
        