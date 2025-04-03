
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 14:36:21 2023

@author: Yhoan Smith Mosquera Peñaloza, Juliana Andrea Gonzalez Romaña
"""
"""Documentación del módulo.
Se utiliza para cargar los archivos a ANEPY, 
lee cada linea de texto y al final la regresa en foema de lista """

__author__ = "Yhoan Smith Mosquera Peñaloza, Juliana Andrea Gonzalez Romaña"
__copyright__ = "UTCH"
__credits__ = '["UTCH","Facultad de Ingeniería", "Yhoan Smith Mosquera Peñaloza", "Juliana Andrea Gonzalez Romaña"]'
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Team CodigoFacilito"
__email__ = "jhoanpa57@gmail.com"
__status__ = "Producción"


# Se carga cada elemento de forma individual del file y se transforma en una lista
def cargar_elementos(d):
        
    ch = '' # Caracter (numero, o texto) # obtiene cada caracter de forma individual
    datos = '' # almacena el numero completo
    Elem = [] # almacena cada parte
    cont = 0
    x = 0
    
    for i in range(6):
        try:
            if i == 0:
                
                while ch != ',': # concatena datos hasta encontrar un separador
                    ch = d[cont]
                    cont = cont + 1
                    if ch != ',':
                        datos = datos + ch # concatenacion de datos
                Elem.append(datos) #se agregan a una lista parcial
        
            elif i == 1 or i == 2:
                datos = ''
                ch = ''
                #print (cont)
                while ch != ',':
                    ch = d[cont]
                    cont = cont + 1
                    if ch != ',':
                        datos = datos + ch
                Elem.append(datos)
                
            elif i == 3 or i == 4 or i == 5:
                datos = ''
                ch = ''
                #print (cont)
                while ch != ',':
                    ch = d[cont]
                    cont = cont + 1
                    if ch != ',':
                        datos = datos + ch
                Elem.append(datos)
        except IndexError:
            pass
    return Elem


#d = '1, 1, 2, 20, 30, 219498.39,0'
#print(abrir_elementos(d ))
        
    # lista.append(datos)
    # datos=''
    
# Se carga cada nodo de forma individual del file y se transforma en una lista

def cargar_nodos(d):
    
    ch = '' # Caracter (numero, o texto) # obtiene cada caracter de forma individual
    datos = '' # almacena el numero completo
    Nod = [] 
    cont = 0
    x = 0
    for i in range(3):
        try: 
            if i == 0:
                while ch != ',': # concatena datos hasta encontrar un separador
                    ch = d[cont]
                    cont = cont + 1
                    if ch != ',':
                        datos = datos + ch # concatenacion de datos
                Nod.append(datos) #se agregan a una lista parcial
            
            elif i == 1 or i == 2:
                datos = ''
                ch = ''
                #print (cont)
                while ch != ',':
                    ch = d[cont]
                    cont = cont + 1
                    if ch != ',':
                        datos = datos + ch
                Nod.append(datos)
        except IndexError:
            pass
    #print(Nod)
    return Nod

# d = '1,0,200,0'

# print(cargar_nodos(d))

# Se carga cada fuerza de forma individual del file y se transforma en una lista

def cargar_fuerzas(d):
    
    
    ch = '' # Caracter (numero, o texto) # obtiene cada caracter de forma individual
    datos = '' # almacena el numero completo
    fuer = [] 
    cont = 0
    x = 0
    # print(d)
    for i in range(6):
        try:
            if i == 0:
                
                while ch != ',': # concatena datos hasta encontrar un separador
                    ch = d[cont]
                    cont = cont + 1
                    if ch != ',':
                        datos = datos + ch # concatenacion de datos
                fuer.append(datos) #se agregan a una lista parcial
        
            elif i == 1 or i == 2 or i == 3:
                datos = ''
                ch = ''
                # print (cont)
                while ch != ',':
                    ch = d[cont]
                    cont = cont + 1
                    if ch != ',':
                        datos = datos + ch
                fuer.append(datos)
            
        except IndexError:
            pass
    
    return fuer

# Se carga cada fw de forma individual del file y se transforma en una lista

def cargar_fuerzas_w(d):
    
    ch = '' # Caracter (numero, o texto) # obtiene cada caracter de forma individual
    datos = '' # almacena el numero completo
    fuer_w = [] 
    cont = 0
    x = 0
    for i in range(3):
        try: 
            if i == 0:
                while ch != ',': # concatena datos hasta encontrar un separador
                    ch = d[cont]
                    cont = cont + 1
                    if ch != ',':
                        datos = datos + ch # concatenacion de datos
                fuer_w.append(datos) #se agregan a una lista parcial
            
            elif i == 1 or i == 2:
                datos = ''
                ch = ''
                #print (cont)
                while ch != ',':
                    ch = d[cont]
                    cont = cont + 1
                    if ch != ',':
                        datos = datos + ch
                fuer_w.append(datos)
        except IndexError:
            pass
    #print(Nod)
    return fuer_w

# Se carga cada restriccion de forma individual del file y se transforma en una lista

def cargar_restricciones(d):

    
    
    ch = '' # Caracter (numero, o texto) # obtiene cada caracter de forma individual
    datos = '' # almacena el numero completo
    rst = [] 
    cont = 0
    x = 0
    for i in range(3):
        try: 
            if i == 0:
                while ch != ',': # concatena datos hasta encontrar un separador
                    ch = d[cont]
                    cont = cont + 1
                    if ch != ',':
                        datos = datos + ch # concatenacion de datos
                rst.append(datos) #se agregan a una lista parcial
            
            elif i == 1:
                datos = ''
                ch = ''
                #print (cont)
                while ch != ',':
                    ch = d[cont]
                    cont = cont + 1
                    if ch != ',':
                        datos = datos + ch
                rst.append(datos)
        except IndexError:
            pass
    #print(Nod)
    return rst
