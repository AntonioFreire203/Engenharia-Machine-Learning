#Classe Agendamento 
class Agendamento:
    #Metodo construtor para inicializar atributos 
    def __init__(self,atividade:str,membro:str,id=None):
        self.atividade = atividade
        self.membro = membro
        self.id = id
        