import pandas as pd
from firebase_class import firebaseDB

# -------------------------------------------------
# Se ejecutó para cargar los archivos a firebase
# -------------------------------------------------

def carga_datos_mipymes(datos_mipymes:pd.DataFrame,firebase_db:firebaseDB):
    for index, row in datos_mipymes.iterrows():
        row = row.to_dict()
        for column in row:
            if column in ["Apoyo creativo", "Dificultades Previas", "Top 3 al elegir", "Materiales listos", "Plazo"]:
                row[column] = row[column].split(",")
        id_= row["ID"]
        firebase_db.create_record(f"/mipymes/{id_}",row)
        
    print("Datos cargados! :]")

def carga_datos_creativos(datos_creativos:pd.DataFrame,firebase_db:firebaseDB):
    for index, row in datos_creativos.iterrows():
        row = row.to_dict()
        for column in row:
            if column in ["Area principal","Criterios para aceptar", "Sectores con experiencia","Fricciones frecuentes","Herramientas","Portafolio","Que espera de Sarasvati","Servicios que puede cubrir"]:
                lista_elems=row[column].split(",")
                for i in range(0,len(lista_elems)):
                    lista_elems[i] = lista_elems[i].strip()
                row[column]=lista_elems
                    
        id_= row["ID"]
        firebase_db.create_record(f"/creativos/{id_}",row)
        
    print("Datos cargados! :]")

# datos_creativos = pd.read_excel("./src/datos_prueba/sarasvati_matching_insumos.xlsx", sheet_name="Creativos_20",skiprows=3,usecols=[x for x in range(0,17 )])
# datos_mipymes = pd.read_excel("./src/datos_prueba/sarasvati_matching_insumos.xlsx", sheet_name="MiPymes_5",skiprows=3,usecols=[x for x in range(0,15)])

# path = "./src/secrets/credentials.json"
# url_database="https://back-sarasvati-default-rtdb.firebaseio.com/"

# firebase_db = firebaseDB(path,url_database)


# carga_datos_creativos(datos_creativos,firebase_db)
# carga_datos_mipymes(datos_mipymes,firebase_db)