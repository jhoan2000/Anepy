# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 14:36:21 2023

@author: Estudiante
"""

def agregar_elementos(d):
    
    ch = '' # Caracter (numero, o texto) # obtiene cada caracter de forma individual
    datos = '' # almacena el numero completo
    Elem = [] 
    tbl_elem = []
    cont = 0
    x = 0
    for i in range(6):
        if i == 0:
            
            while ch != ',': # concatena datos hasta encontrar un separador
                ch = d[cont]
                cont = cont + 1
                if ch != ',':
                    datos = datos + ch # concatenacion de datos
            Elem.append((datos)) #se agregan a una lista parcial
        
        elif i == 1 or i == 2:
            datos = ''
            ch = ''
            print (cont)
            while ch != ',':
                ch = d[cont]
                cont = cont + 1
                if ch != ',':
                    datos = datos + ch
            Elem.append(int(datos))
            
        elif i == 3 or i == 4 or i == 5:
            datos = ''
            ch = ''
            print (cont)
            while ch != ',':
                ch = d[cont]
                cont = cont + 1
                if ch != ',':
                    datos = datos + ch
            Elem.append(float(datos))
    return Elem
d = '1, 1, 2, 20, 30, 219498.39,0'
print(agregar_elementos(d ))
        
    # lista.append(datos)
    # datos=''