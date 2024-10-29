#Classe Plano de Assinatura 
class TipoPlano:
    #Metodo construtor para inicializar atributos 
    def __init__(self,plano:str,id:int =None):
        self.plano = plano
        self.id = id 