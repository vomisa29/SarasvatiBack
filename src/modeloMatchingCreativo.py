from pyomo.environ import *
from  pyomo.opt  import  SolverFactory


class modelo_sarasvati_matematico():

    def __init__(self,infoMypime,infoCreativos):
        self.infoCreativos=infoCreativos
        self.infoMypime=infoMypime

    def ejecutar(self):
        #Modelo
        model = ConcreteModel()

        #Conjuntos
        NUM_PARAMS = 3
        NUM_SUBPARAMS = 10
        model.C = RangeSet(len(self.infoCreativos)/(NUM_PARAMS*NUM_SUBPARAMS))
        
        #Parametros        
        
        model.P = RangeSet(NUM_PARAMS)
        
        
        model.Sp = RangeSet(NUM_SUBPARAMS)

        # Coeficientes (suman 1)
        coef={}
        for i in range(NUM_PARAMS):
            coef[i+1]=0.33
        
        model.coef = Param(model.P, initialize = coef)

        model.infoCreativos = Param(model.C,model.P,model.Sp,initialize=self.infoCreativos)

        model.infoMypime = Param(model.P,model.Sp,initialize=self.infoMypime)

        #Variables de Decisión
        model.X = Var(model.C, within=Binary)

        #Función Objetivo
        model.obj = Objective(expr=sum(model.X[c]*((model.infoCreativos[c,p,sp] - model.infoMypime[p,sp])**2 * model.coef[p]) for c in model.C for p in model.P for sp in model.Sp),sense=minimize)

        #Restricciones
        def numMiPymes(model):
            return sum(model.X[c] for c in model.C) == 3
        model.numMiPymes = Constraint(rule=numMiPymes)

        #Solver
        solver = SolverFactory("glpk")
        solver.solve(model)
        
        # Respuesta
        lista_tuplas_rta=[]
        for c in model.C:
            if value(model.X[c]) != 0:
                lista_tuplas_rta.append((c,round(calculo_costo(model,c),2)))

        return lista_tuplas_rta

def calculo_costo(model,c):
    return sum(((model.infoCreativos[c,p,sp] - model.infoMypime[p,sp])**2 * model.coef[p]) for p in model.P for sp in model.Sp)



    