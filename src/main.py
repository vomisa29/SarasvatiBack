from fastapi import FastAPI
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware

from src.modelo import modeloSarasvati
from src.db_service.firebase_service import firebaseService



app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


firebase_service = firebaseService()

@app.get("/")
def read_root():
    return {"Raiz","Api"}

@app.post("/mipymes/")
async def create_mipyme(request:Request):
    body = await request.json()
    id_respuesta = firebase_service.put_mipyme(body)
    return id_respuesta


@app.get("/modelo_matematico/{item_id}")
async def read_item(item_id: str | None = None):
    creativos_modelo, creativos = get_creativos_modelo()
    mipyme_modelo = get_mipyme_modelo(item_id)
    modelo = modeloSarasvati(tipo="modelo_matematico")
    lista_tuplas_rta= modelo.ejecutar_modelo(mipyme_modelo,creativos_modelo)
    
    rta_modelo=[]
    lista_creativos=list(creativos.values())
    for indice, costo in lista_tuplas_rta:
        # Dead Weight
        creativo=lista_creativos[indice-1]
        creativo_simple={
            "alias":creativo["Alias"],
            "areas_principales":creativo["Area principal"],
            "presupuesto":creativo["Rango precio"]
        }
        rta_modelo.append((creativo_simple,costo))
    return {"Respuesta Modelo": rta_modelo,
            "id":item_id}
    


def get_creativos_modelo():
    creativos = firebase_service.get_creativos()
    cubo_creativos = firebase_service.crear_cubo_creativos(creativos)
    creativos_modelo = firebase_service.cubo_a_dict_modelo(cubo_creativos)
    return creativos_modelo, creativos

def get_mipyme_modelo(Id:str):
    mipyme = firebase_service.get_mipyme(Id)
    mipyme_arreglada=firebase_service.transform_mipyme_model(mipyme)
    mipyme_modelo=firebase_service.matriz_a_dict_modelo(mipyme_arreglada)
    return mipyme_modelo
