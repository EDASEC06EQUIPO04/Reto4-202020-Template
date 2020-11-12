"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * Contribución de:
 *
 * Dario Correal
 *
 """


import sys
import config
from App import controller
from DISClib.ADT import stack
import timeit
assert config
from DISClib.Algorithms.Graphs import scc

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones  y  por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Variables
# ___________________________________________________


initialStation = None
recursionLimit = 20000
servicefile = '201801-1-citibike-tripdata.csv'
servicefile2 = '201801-2-citibike-tripdata.csv'
#servicefile3 = '201801-3-citibike-tripdata.csv'
#servicefile4 = '201801-4-citibike-tripdata.csv'

# ___________________________________________________
#  Menu principal
# ___________________________________________________


def printMenu():
    print("\n")
    print("****************************************************")
    print("RETO No. 4 CitiBike")
    print("[ 1 ] Inicializar Analizador")
    print("[ 2 ] Cargar información de citibyke en newyork")
    print("[ 3 ] Cantidad de clusters de viajes")
    print("[ 4 ] Ruta turistica circular")
    print("[ 5 ] Estaciones criticas ")
    print("[ 6 ] Ruta turistisca por resistencia")
    print("[ 7 ] Recomendador de Rutas")
    print("[ 8 ] Ruta de interes turistico")
    print("[ 9 ] Identificacion de estaciones para publicidad")
    print("[10 ] Identificacion de bicicletas para mantenimiento")
    print("[ 0 ] Salir")
    print("****************************************************")


def optionTwo():
    print("\nCargando información ....")
    controller.loadServices(cont)
    numedges = controller.totalConnections(cont)
    numvertex = controller.totalStops(cont)
    print('Numero de vertices: ' + str(numvertex))
    print('Numero de arcos: ' + str(numedges))
    print('El limite de recursion actual: ' + str(sys.getrecursionlimit()))
    sys.setrecursionlimit(recursionLimit)
    print('El limite de recursion se ajusta a: ' + str(recursionLimit))


def optionThree():
    print('El número de componentes conectados es: ' + str(controller.connectedComponents(cont)))
    id1=int(input("inserte ID1\n"))
    id2=int(input("inserte ID2\n"))
    #TESTED WITH 
    #146
    #168
    #controller.connectedwithID(cont,id1,id2)



def optionFour():
    controller.minimumCostPaths(cont, initialStation)


def optionFive():
    pass

def optionSix():
    pass


def optionSeven():
    pass

def optionEight():
    pass

def optionNine():
    pass

def optionTen():
    pass



"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n>')

    if int(inputs[0]) == 1:
        print("\nInicializando....")
        # cont es el controlador que se usará de acá en adelante
        cont = controller.init()

    elif int(inputs[0]) == 2:
        executiontime = timeit.timeit(optionTwo, number=1)
        print("Tiempo de ejecución: " + str(executiontime))

    elif int(inputs[0]) == 3:
        executiontime = timeit.timeit(optionThree, number=1)
        print("Tiempo de ejecución: " + str(executiontime))

    elif int(inputs[0]) == 4:
        msg = "Estación Base: BusStopCode-ServiceNo (Ej: 75009-10): "
        initialStation = input(msg)
        executiontime = timeit.timeit(optionFour, number=1)
        print("Tiempo de ejecución: " + str(executiontime))

    elif int(inputs[0]) == 5:
        destStation = input("Estación destino (Ej: 15151-10): ")
        executiontime = timeit.timeit(optionFive, number=1)
        print("Tiempo de ejecución: " + str(executiontime))

    elif int(inputs[0]) == 6:
        destStation = input("Estación destino (Ej: 15151-10): ")
        executiontime = timeit.timeit(optionSix, number=1)
        print("Tiempo de ejecución: " + str(executiontime))

    elif int(inputs[0]) == 7:
        executiontime = timeit.timeit(optionSeven, number=1)
        print("Tiempo de ejecución: " + str(executiontime))
    
    elif int(inputs[0]) == 8:
        executiontime = timeit.timeit(optionEight, number=1)
        print("Tiempo de ejecución: " + str(executiontime))
    
    elif int(inputs[0]) == 9:
        executiontime = timeit.timeit(optionNine, number=1)
        print("Tiempo de ejecución: " + str(executiontime))
    
    elif int(inputs[0]) == 10:
        executiontime = timeit.timeit(optionTen, number=1)
        print("Tiempo de ejecución: " + str(executiontime))

    else:
        sys.exit(0)
sys.exit(0)
