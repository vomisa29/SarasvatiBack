from db_service.firebase_class import firebaseDB

path = "./src/secrets/credentials.json"
url_database="https://back-sarasvati-default-rtdb.firebaseio.com/"

class firebaseService:
    def __init__(self):
        self.fb_db = firebaseDB(path,url_database)
        
    # --- MiPymes ---
    def get_mipyme(self,id):
        data = self.fb_db.read_record("/mipymes/" + id)
        
        if data == None:
            data = {}
        
        return data
    
    def put_mipyme(self, data):
        return self.fb_db.create_record("mipymes",data)
    
    def transform_mipyme_model(self,mipyme:dict):
        mypime_modelo=[]
        for elem in mipyme:
            if elem == "Apoyo creativo":
                lista_apoyos=["Diseño gráfico",
                               "Branding / identidad de marca",
                               "Contenido para redes sociales",
                               "Fotografía de producto o marca",
                               "Video / reels / animación",
                               "Estrategia de contenido o marketing",
                               "Diseño web o landing page",
                               "Copywriting / textos",
                               "Packaging / diseño de empaques",
                               "Otro"]# Motion graphics, Ilustración,
                lista_param_apoyo=[]
                for apoyo in lista_apoyos:
                    if apoyo in mipyme[elem]:#Si el apoyo es algo que quiere la MiPyme
                        lista_param_apoyo.append(1)
                    else:
                        lista_param_apoyo.append(0)
            
            elif elem == "Sector":
                lista_sectores=["Gastronomía / alimentos",
                                "Moda / belleza",
                                "Tecnología / software",
                                "Salud / bienestar",
                                "Educación",
                                "Servicios profesionales",
                                "Comercio / retail",
                                "Turismo / hotelería",
                                "Industria / manufactura",
                                "Otro"]
                lista_param_sectores=[]
                for sectores in lista_sectores:
                    if sectores == mipyme[elem]:
                        lista_param_sectores.append(1)
                    else:
                        lista_param_sectores.append(0)
                        
            elif elem == "Presupuesto":
                lista_presupuesto=["Menos de $500.000",
                                   "$500.000 – $1.000.000",
                                   "$1.000.000 – $3.000.000",
                                   "$3.000.000 – $5.000.000",
                                   "$5.000.000 – $10.000.000",
                                   "Más de $10.000.000",
                                   "no se",
                                   "###",
                                   "###",
                                   "###"]# Se usa ### como relleno
                lista_param_presupuesto=[]
                for presupuesto in lista_presupuesto:
                    if presupuesto == mipyme[elem]:
                        lista_param_presupuesto.append(1)
                    else:
                        lista_param_presupuesto.append(0)
            
        mypime_modelo.append(lista_param_apoyo)
        mypime_modelo.append(lista_param_sectores)
        mypime_modelo.append(lista_param_presupuesto)
                
        return mypime_modelo
    
    # --- Creativos ---
    def get_creativo(self, id):
        data = self.fb_db.read_record("/creativos/" + id)
        
        if data == None:
            data = {}
        
        return data
    
    def get_creativos(self):
        data = self.fb_db.read_record("/creativos")
        
        if data == None:
            data = {}
            
        return data
    
    def put_creativo(self, data):
        return self.fb_db.create_record("creativos",data)
    
    def transform_creativo_model(self,creativo):
        creativo_modelo=[]
        for elem in creativo:
            if elem == "Area principal":
                lista_areas=["Diseño gráfico",
                             "Branding / identidad de marca",
                             "Contenido para redes (Community Management)",
                             "Fotografía",
                             "Video",
                             "Estrategia de marketing / contenido",
                             "Diseño web / UI",
                             "Copywriting / redacción",
                             "Packaging",
                             "###"]# Motion graphics, Ilustración,
                lista_param_areas=[]
                lista_areas_creativo = creativo[elem]
                for area in lista_areas:                
                    if area in lista_areas_creativo or (area == "###" and ("Motion graphics" in lista_areas_creativo or "Ilustración" in lista_areas_creativo)):
                        lista_param_areas.append(1)
                    else:
                        lista_param_areas.append(0)
            elif elem == "Sectores con experiencia":
                lista_sectores = ["Gastronomía / alimentos",
                                  "Moda / belleza",
                                  "Tecnología",
                                  "Salud / bienestar",
                                  "Educación",
                                  "Servicios profesionales",
                                  "Comercio / retail",
                                  "Turismo / hotelería",
                                  "Cualquier sector",
                                  "Otro"]
                lista_param_sectores=[]
                lista_sectores_creativo = creativo[elem]
                for sector in lista_sectores:
                    if sector in lista_sectores_creativo:
                        lista_param_sectores.append(1)
                    else:
                        lista_param_sectores.append(0)
            elif elem == "Rango precio":
                lista_precios = ["Menos de $500.000 COP",
                                 "$500.000 – $1.000.000",
                                 "$1.000.000 – $3.000.000",
                                 "$3.000.000 – $5.000.000",
                                 "$5.000.000 – $10.000.000",
                                 "Más de $10.000.000",
                                 "Depende completamente del proyecto",
                                 "###",
                                 "###",
                                 "###"]
                lista_param_precios=[]
                lista_precios_creativo = creativo[elem]
                for sector in lista_precios:
                    if sector in lista_precios_creativo:
                        lista_param_precios.append(1)
                    else:
                        lista_param_precios.append(0)
                          
        creativo_modelo.append(lista_param_areas)
        creativo_modelo.append(lista_param_sectores)
        creativo_modelo.append(lista_param_precios)
        
        return creativo_modelo

    def crear_cubo_creativos(self,creativos):
        cubo_creativos = []
                
        for creativo_key in creativos:
            creativo=creativos[creativo_key]
            cubo_creativos.append(self.transform_creativo_model(creativo))
        
        return cubo_creativos
        
        
    # --- Funciones Auxiliares ---
    def matriz_a_dict_modelo(self,matriz_mipyme):
        mipyme_modelo = {}
        for i in range(0,len(matriz_mipyme)):# Num Parametros
            for j in range(0,len(matriz_mipyme[0])):# Sub parametros
                mipyme_modelo[i+1,j+1]=matriz_mipyme[i][j]
        return mipyme_modelo
    
    def cubo_a_dict_modelo(self,cubo_creativos):
        creativos_modelo={}
        for i in range(0,len(cubo_creativos)):# Num Creativos
            for j in range(0,len(cubo_creativos[0])):# Num Parametros
                for k in range(0,len(cubo_creativos[0][0])):# Sub parametros
                    creativos_modelo[i+1,j+1,k+1]=cubo_creativos[i][j][k]
        return creativos_modelo