import numpy as np
import random
import plotly.express as px
from tqdm import tqdm

from poblacion_inicial import poblacion_inicial
from seleccionPadres import seleccionPadres
from cruzamiento import cruzamiento
from funcion_objetivo import funcion_objetivo
from mutacion import mutacion

# configuración semilla numeros aleatorios
## aquí su código ##

# instancia el problema: obtener peso_objetos, precio_objetos
numero_objetos = 30
peso_maximo = 60
## aquí su código ##

# parámetros genético: obtener tamaño_poblacion, k (individuos candidatos a padres), tasa_mutacion
maximo_iteraciones = numero_objetos*1000
## aquí su código ##

# construir poblacion inicial: obtener poblacion, peso_poblacion, funciones_objetivo_pop
print("\n Generando poblacion inicial factible...\n")
## aquí su código ##

# obtener incumbente desde población: obtener incumbente, solucion_incumbente, peso_incumbente, historia_incumbente
print("\n Obteniendo incumbente inicial...\n")
## aquí su código ##

#print(f"Incumbente_inicial: {incumbente}")
#print(f"Solución incumbente_inicial: {solucion_incumbente}")

# inicio evolución
#with tqdm(total=len(range(maximo_iteraciones))) as pbar:
#    for i in range(maximo_iteraciones):
        # seleccionar padres
        #padres = seleccionPadres(k,funciones_objetivo_pop,poblacion,tamaño_poblacion,numero_objetos) 

        # Cruzamiento
        #hijos = cruzamiento(padres)

        # selección del mejor hijo
        #func_obj = funcion_objetivo(hijos,precio_objetos,peso_objetos,peso_maximo)
        
        # mejor hijo como el que tenga mejor función objetivo
        #mejor_hijo = 

        # mutación
        #mejor_hijo_mutado = mutacion(mejor_hijo,tasa_mutacion,numero_objetos)
        #func_obj_mutado,_ = funcion_objetivo([mejor_hijo_mutado], precio_objetos,peso_objetos,peso_maximo)
        
        # extraer el valor de la función objetivo del objeto de retorno de "funcion_objetivo" 
        #func_obj_mutado = 

        # verificar si solución existe en población
        #ingresa = False
        #indices = np.where((poblacion == mejor_hijo_mutado).all(axis=1))  # verifica cada vector de la población con el mejor hijo mutado.
        #if len(indices[0]) == 0:
            #peso_hijo_mutado = 
            # verificar si es factible por peso y si es mejor que incumbente para ingresar a población
            #if peso_hijo_mutado < peso_maximo and func_obj_mutado > incumbente:
            #    ingresa = True

        # actualización de la población
        #if ingresa:
            # encontrar miembro de la población con menor función objetivo
            #posicion_menor = 
            # actualizar miembro de la población con menor función objetivo con el mejor hijo mutado y su función objetivo
            #poblacion[posicion_menor] = 
            #funciones_objetivo_pop[posicion_menor] = 

        # actualizar incumbente
        #incumbente = 
        #solucion_incumbente = 
        # anexar incumbente a la historia_icumbente
        #historia_incumbente...
        
        #pbar.set_description(f"fo_incumbente: {incumbente}") # activar para la barra de progreso
        #pbar.update() # activar para la barra de progreso
    

#solucion_incumbente = 
#peso_incumbente = 
#print(f"\n Solución incumbente: {solucion_incumbente} \n")
#print(f"peso incumbente: {peso_incumbente} \n")

# gráfico de mejoramiento de función objetivo
#fig = px.line(historia_incumbente)
#fig.show()