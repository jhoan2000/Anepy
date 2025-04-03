# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 21:57:31 2023

@author: Yhoan Smith Mosquera Peñaloza, Juliana Andrea Gonzalez Romaña
"""

__author__ = "Yhoan Smith Mosquera Peñaloza, Juliana Andrea Gonzalez Romaña"
__copyright__ = "UTCH"
__credits__ = '["UTCH","Facultad de Ingeniería", "Yhoan Smith Mosquera Peñaloza", "Juliana Andrea Gonzalez Romaña"]'
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Team CodigoFacilito"
__email__ = "jhoanpa57@gmail.com"
__status__ = "Producción"


"""ESTE MONUDULO JUNTO A ABIR TXT SIRVE PARA CONVERSION DE TXT A LISTA PYTHON"""

from abrir_txt import cargar_elementos, cargar_nodos, cargar_fuerzas
from abrir_txt import cargar_fuerzas_w, cargar_restricciones


E  = 219498.39
tbl_Elem = [
    
  # Elem, Ni, Nf, b, h, E,
    ["1", 1, 2, 20, 30, E],
    ["2", 2, 3, 20, 30, E],
    ["3", 3, 4, 20, 20, E],
    #["4", 3, 4, 40, 40, E],
    ]

tbl_Nod = [
    #Nodo, cx, cy
    [1, 0, 200],
    [2, 150, 200],
    [3, 300, 200],
    [4, 300, 0],
    ]

tbl_Fuer = [
    #Nod, fx, fy, Mz
    #[1,0, -1000, -75000],
    [2,0, -2000, 0]
  
    ]

tbl_Fuer_W = [
    #Elem, Wi, Wf
    ["3",-500, -500],

    ]

tbl_Rest = [
        #Tipo de Apoyo, Nodo
        # Simple
        # Articulado
        # Empotrado
    ["Empotrado", 1],
    ["Articulado", 4,],

    ]
unidades = "m, KN, MPa"


class files:
    def __init__(self, name):
        self.name  = name
    def crear(self):
        archivo = open(str(self.name)+".txt", 'w',encoding='utf-8') # Crear archivo
        archivo.close()
    def abrir(self):
        archivo = open(self.name, 'rt')
        #lectura = archivo.read()      
        return archivo
    def añadir(self,contenido):
        #print(contenido)
        archivo = open(self.name, 'a')
        archivo.write(contenido) # Primera escritura
        
        archivo.close()
    def leer_linea(self, linea):
        archivo = open(str(self.name)+".txt")
        #print(archivo.readlines(linea))
        archivo.close()
        
        

"""ABRE FICHERO"""
#file = files("EJERCICIO 10-6 LIBRO QUISPE")


def guardar_datos(name, tbl_Elem, tbl_Nod, tbl_Fuer, tbl_Fuer_W , tbl_Rest, unidades):
    file = files(name)
    # Elementos 
    for n in range(len(tbl_Elem)): 
        for i in range(6): 
            file.añadir(str(tbl_Elem[n][i])) # Se envia cada dato del elemento individual
            file.añadir(",") # Se agrega separador
            if i == 5:
                file.añadir('0')# Se agrega un dato de mas para evitar error
        file.añadir("\n") # Genera el salto de linea
    
    # Nodos
    file.añadir("N\n")
    for n in range(len(tbl_Nod)):
        for i in range(3): 
            file.añadir(str(tbl_Nod[n][i]))
            file.añadir(",")
            if i == 2 :
                file.añadir('0')
        file.añadir("\n")
    
    # Fuerzas
    file.añadir("F\n")
    for n in range(len(tbl_Fuer)):
        for i in range(4): 
            file.añadir(str(tbl_Fuer[n][i]))
            file.añadir(",")
            if i == 3 :
                file.añadir('0')
        file.añadir("\n")
        
    # Fuerzas W
    file.añadir("FW\n")
    for n in range(len(tbl_Fuer_W)):
        for i in range(3): 
            file.añadir(str(tbl_Fuer_W[n][i]))
            file.añadir(",")
            if i == 2 :
                file.añadir('0')
        file.añadir("\n")
    
    # Restricciones
    file.añadir("RST\n")
    for n in range(len(tbl_Rest)):
        for i in range(2): 
            file.añadir(str(tbl_Rest[n][i]))
            file.añadir(",")
            if i == 1 :
                file.añadir('0')
        file.añadir("\n")
        
    file.añadir("Unidades\n")
    file.añadir(str(unidades))
    #file.añadir("\n")
    



def abir_datos(name):
    file = files(name) # Se llama la clase archivo
    
    # Listas parciales de almacenamiento de los datos
    tbl_Elem_p = []
    tbl_Nod_p = []
    tbl_Fuer_p = []
    tbl_Fuer_W_p = []
    tbl_Rest_p = []
    unidades = ""
    
    archivo = file.abrir() # Se abre el archivo
    
    # Se inicial las variables de control de datos
    # Cuando se identifica el separador de datos se modifican los valores en cadena
    # hasta cargar todos los datos
    elem = True 
    nod = False
    fuer = False
    fuer_w = False
    rest = False
    unidad = False
    
    for d in archivo: # recorre cala linea el archivo
        #tbl_Elem_p.append(l)    
        datos = cargar_elementos(d) # # enviala linea de datos y los regresa en forma de lista
        
        if datos != [] and elem == True: # Variable de control de datos para los elementos
            tbl_Elem_p.append(datos)
            
        if d == "N\n": # Cuando se detecta un separador en una linea se rope el condicional anterior 
            elem = False # y se crea una candena hasta culminar
            nod = True
    
        datos = cargar_nodos(d)  
        if datos != [] and nod == True:
            tbl_Nod_p.append(datos)
                
        if d == "F\n" :
            nod = False
            fuer = True
            
        datos = cargar_fuerzas(d) 
        #print(datos)
        if datos != [] and fuer == True:
    
            tbl_Fuer_p.append(datos)
            
            
        if d == "FW\n" :
            fuer = False
            fuer_w = True
        datos = cargar_fuerzas_w(d)
        
        if datos != [] and fuer_w == True :
            #print(d)
            tbl_Fuer_W_p.append(datos)
            
        if d == "RST\n" :
            fuer_w = False
            rest = True
        datos = cargar_fuerzas_w(d)
        
        if datos != [] and rest == True :
            #print(d)
            tbl_Rest_p.append(datos)
            
        if d =="Unidades\n":
            rest = False
            unidad = True
        if datos != [] and unidad == True :
            unidades = d
            #print(d)
        
        
    # Se regresan las tablas conformadas por string, posteriormente se convierten al type corre.. 
    return tbl_Elem_p ,tbl_Nod_p, tbl_Fuer_p, tbl_Fuer_W_p, tbl_Rest_p, unidades
            

#guardar_datos('C:/Users/Estudiante/Desktop/abc.j&y', tbl_Elem, tbl_Nod, tbl_Fuer, tbl_Fuer_W, tbl_Rest, unidades)

#print(abir_datos('C:/Users/Estudiante/Desktop/abc.j&y')[5])
