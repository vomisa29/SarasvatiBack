from modelo import modeloSarasvati as ms
from modeloMatchingCreativo import modelo_sarasvati_matematico as m_mat

a=m_mat()
a.ejecutar()

varPrueba = ms(tipo="modelo_matematico")
print(varPrueba.ejecutar_modelo())