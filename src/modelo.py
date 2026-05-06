from src.modeloMatchingCreativo import modelo_sarasvati_matematico as clase_modelo

class modeloSarasvati:
    def __init__(self,tipo):
        self.modelo=self.get_modelo(tipo)
        
    def get_modelo(self,tipo:str):
        modelos={
            "modelo_matematico":self.modelo_matematico,
            "modelo_ml":self.modelo_ml
        }
        return modelos.get(tipo,"El modelo no existe")
    
    
    def ejecutar_modelo(self,info_mipyme,info_creativos):
        if type(self.modelo) != str:
            print("Ejecutando Modelo:")
            return self.modelo(info_mipyme,info_creativos)
        else:
            return self.modelo
        
    def modelo_matematico(self,info_mipyme,info_creativos):
        modelo=clase_modelo(info_mipyme,info_creativos)
        modelo_rta = modelo.ejecutar()
        return modelo_rta
    
    def modelo_ml(self):
        return "modelo_ml"