#Classe Atividade
class Atividade:
    #Metodo construtor para inicializar atributos 
    def __init__(self,nome:str,instrutor:str,data:str,duracao:str,capacidade:str,tipo_plano:str,ativo:str,id:int=None):
        self.nome = nome
        self.instrutor = instrutor
        self.data = data
        self.duracao = duracao
        self.capacidade = capacidade
        self.tipo_plano = tipo_plano
        self.ativo = ativo
        self.id = id
        