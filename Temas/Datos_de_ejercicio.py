# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 21:42:37 2022

@author: Estudiante
"""

#Datos de ejercicios
# ENTRADA DE DATOS 
"""EJERCICIO 10-6 LIBRO QUISPE """


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
        #El, Ni, Nf
#print(nodos[:])
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

"""EJERCICIO 10-9 LIBRO QUISPE """
E  = 217370.65

tbl_Elem = [
    
  # Elem, Ni, Nf, b, h, E,
    ["1", 1, 4, 25, 25, E],
    ["2", 2, 5, 25, 25, E],
    ["3", 3, 6, 25, 25, E],
    ["4", 4, 8, 25, 25, E],
    ["5", 5, 9, 25, 25, E],
    ["6", 6, 10, 25, 25, E],
    ["7", 4, 5, 25, 50, E],
     ["8", 5, 6, 25, 50, E],
     ["9", 6, 7, 25, 50, E],
    ["10", 8, 9, 25, 50, E],
     ["11", 9, 10, 25, 50, E],
     ["12", 10, 11, 25, 50, E],


    ]
    
tbl_Nod = [
    #Nodo, cx, cy
    [1, 0, 0],
    [2, 500, 0],
    [3, 900, 0],
    [4, 0, 400],
    [5, 500, 400],
    [6, 900, 400],
    [7, 1050, 400],
    [8, 0, 700],
    [9, 500, 700],
    [10, 900, 700],
    [11, 1050, 700],

    ]
        #El, Ni, Nf
#print(nodos[:])


tbl_Fuer = [
    #Nod, fx, fy, Mz
    # [3, 700, 0, 0],

  
    ]

tbl_Fuer_W = [
    #Elem, Li,Lf, Wi, Wf
    ["7", -7, -7],
    ["8", -7, -7,],
    ["9", -7 , -7],
    ["10", -7, -7,],
    ["11", -7, -7],
    ["12", -7, -7,],

    ]

tbl_Rest = [
        #Tipo de Apoyo, Nodo
        # Simple
        # Articulado
        # Empotrado
    ["Empotrado", 1],
    ["Empotrado", 2,],
    ["Empotrado", 3,],
    ]


"""EJERCICIO 10-8 LIBRO QUISPE """


E  = 219498.39

tbl_Elem = [
    
  # Elem, Ni, Nf, b, h, E,
    ["1", 1, 2, 40, 40, E],
    ["2", 2, 3, 40, 40, E],
    ["3", 3, 4, 40, 40, E],

    ]
    
tbl_Nod = [
    #Nodo, cx, cy
    [1, 0, 0],
    [2, 0, 500],
    [3, 1000, 767.95],
    [4, 1000, 0],

    ]
        #El, Ni, Nf
#print(nodos[:])
tbl_Fuer = [
    #Nod, fx, fy, Mz
  [2,500, 0, 0],
    ]

tbl_Fuer_W = [
    #Elem, Li,Lf, Wi, Wf
    ["2", -1, -1],

    ]

tbl_Rest = [
        #Tipo de Apoyo, Nodo
        # Simple
        # Articulado
        # Empotrado
    ["Empotrado", 1],
    ["Empotrado", 4,],

    ]




"""EJERCICIO Youtube https://www.youtube.com/watch?v=e9oqbQtloFY """

fc = 28
E  = 4700*sqrt(fc)
tbl_Elem = [
    
  # Elem, Ni, Nf, b, h, E,

    ["1", 1, 4, 0.4, 0.5, E],
    ["2", 2, 5, 0.5, 0.6, E],
    ["3", 3, 6, 0.5, 0.6, E],
    ["4", 4, 7, 0.4, 0.5, E],
    ["5", 5, 8, 0.4, 0.5, E],
    ["6", 4, 5, 0.4, 0.5, E],
    ["7", 5, 6, 0.4, 0.5, E],
    ["8", 7, 8, 0.4, 0.5, E],
    ]
    
tbl_Nod = [
    # Nodo, cx, cy

    [1, 0, 0],
    [2, 4, 0],
    [3, 11, 0],
    [4, 0, 4],
    [5, 4, 4],
    [6, 11, 4],
    [7, 0, 8],
    [8, 4, 8],

    ]


tbl_Fuer = [
    #Nod, fx, fy, Mz

    [4, 10, 0, 0],
    [7, 20, 0, 0 ],

  
    ]

"""Eliminar Li y Lf """
tbl_Fuer_W = [

    # Elem, Li,Lf, Wi, Wf
    ["6", -8.1, -8.1],
    ["7", -8.1, -8.1],
    ["8", -5, -5],

    ]

tbl_Rest = [
        #Tipo de Apoyo, Nodo
        # Simple
        # Articulado
        # Empotrado
    ["Empotrado", 1],
    ["Empotrado", 2,],
    ["Empotrado", 3,],

    ]

"""EJERCICIO 11-18 LIBRO Jairo U """


E  = 19*(1000**2)

tbl_Elem = [
    
  # Elem, Ni, Nf, b, h, E,
    ["1", 1, 2, 0.3, 0.5, E],
    ["2", 3, 1, 0.3, 0.3, E],
    ["3", 4, 2, 0.3, 0.3, E],


    ]
    
tbl_Nod = [
    #Nodo, cx, cy
    [1, 0, 3],
    [2, 6, 3],
    [3, 0, 0],
    [4, 6, 0],

    ]


tbl_Fuer = [
    #Nod, fx, fy, Mz
    # [3, 700, 0, 0],
  
    ]

tbl_Fuer_W = [
    #Elem, Li,Lf, Wi, Wf
    ["1", -25, -25],

    ]

tbl_Rest = [
        #Tipo de Apoyo, Nodo
        # Simple
        # Articulado
        # Empotrado
    # ["Empotrado", 1],
    ["Empotrado", 4,],
    ["Empotrado", 3,],
    ]

"""EJERCICIO 11-20 LIBRO Jairo U """

# ENTRADA DE DATOS 
E  = 19*(1000**2)

tbl_Elem = [
    
  # Elem, Ni, Nf, b, h, E,
    ["1", 1, 2, 0.3, 0.5, E],
    ["2", 2, 3, 0.3, 0.5, E],
    ["3", 3, 4, 0.3, 0.5, E],
    ["4", 4, 5, 0.3, 0.5, E],
    ["5", 6, 2, 0.3, 0.3, E],
    ["6", 7, 3, 0.3, 0.3, E],

    ]
    
tbl_Nod = [
    #Nodo, cx, cy
    [1, 0, 3.5],
    [2, 2, 3.5],
    [3, 7, 3.5],
    [4, 9, 3.5],
    [5, 13, 3.5],
    [6, 2, 0],
    [7, 7, 0],
    ]
        #El, Ni, Nf
#print(nodos[:])


tbl_Fuer = [
    #Nod, fx, fy, Mz
    [4, 0, -80, 0],
  
    ]

tbl_Fuer_W = [
    #Elem, Li,Lf, Wi, Wf
    ["1", -26, -26],
    ["2", -26, -26],

    ]

tbl_Rest = [
        #Tipo de Apoyo, Nodo
        # Simple
        # Articulado
        # Empotrado
    ["Empotrado", 5],
    ["Articulado", 6,],
    ["Empotrado", 7,],

    ]


"EJercicio marcelo pardo"

# ENTRADA DE DATOS 
E  = 21*(1000**2)

tbl_Elem = [
    
  # Elem, Ni, Nf, b, h, E,
    ["1", 1, 2, 0.4, 0.4, E],
    ["2", 2, 3, 0.3, 0.3, E],
    ["3", 2, 5, 0.2, 0.5, E],
    ["4", 3, 6, 0.2, 0.5, E],
    ["5", 4, 5, 0.4, 0.4, E],
    ["6", 5, 6, 0.3, 0.3, E],
    ["7", 5, 7, 0.2, 0.5, E],
    ["8", 7, 9, 0.2, 0.5, E],
    ["9", 8, 9, 0.4, 0.4, E],


    ]
    
tbl_Nod = [
    #Nodo, cx, cy
    [1, 0, 0],
    [2, 0, 4],
    [3, 0, 7],
    [4, 5.2, 0],
    [5, 5.2, 4],
    [6, 5.2, 7],
    [7, 7.8, 4],
    [8, 10.1, 1.5],
    [9, 10.1, 4],

    ]


tbl_Fuer = [
    #Nod, fx, fy, Mz
    [7, 0, -20, 0],

  
    ]

tbl_Fuer_W = [
    #Elem, Li,Lf, Wi, Wf
    ["1", 0, ((10*4)/7)],
    ["2", ((10*4)/7), 10],
    ["3", -8, -8], #"""CASO ANALIZAR######################"""############################
    ["4", -8, -8],
    ["7", -8, -8,],
    ["8", -8, -8,],

    ]

tbl_Rest = [
        #Tipo de Apoyo, Nodo
        # Simple
        # Articulado
        # Empotrado
    ["Empotrado", 1],
    ["Empotrado", 4,],
    ["Empotrado", 8,],

    ]


"EJercicio Rafael Rojas 4.10"

E  = 221.359

tbl_Elem = [
    
  # Elem, Ni, Nf, b, h, E,
   ['1', 1, 2, 30, 30, 221.359],
 ['2', 2, 3, 30, 60, 221.359],
 ['3', 4, 3, 30, 30, 221.359],
 
]
    
tbl_Nod = [
    #Nodo, cx, cy
 [1, 0, 0.0],
 [2, 0, 400],
 [3, 1000, 400],
 [4, 1000, 0.0],
 ]
        #El, Ni, Nf
#print(nodos[:])
tbl_Fuer = [
    
    #Nod, fx, fy, Mz
    [2,10, 0, 0],
    ]

tbl_Fuer_W = [
    #Elem, Li,Lf, Wi, Wf
 ]

tbl_Rest = [
        #Tipo de Apoyo, Nodo
        # Simple
        # Articulado
        # Empotrado
    ['Empotrado', 1],
    ['Articulado', 4]
    ]

"""EJERCICIO 10-8 LIBRO QUISPE """


E  = 217370.65

tbl_Elem = [
    
  # Elem, Ni, Nf, b, h, E,
   ['1', 1, 3, 25, 25,E ],
 ['2', 2, 4,  25, 25,E],
 ['3', 3, 4,  25, 50, E],
 ['4', 3, 5,  25, 25, E],
['5', 4, 6,  25, 25, E],
['6', 5, 6, 25, 50, E],
 
]
    
tbl_Nod = [
    #Nodo, cx, cy
 [1, 0, 0.0],
 [2, 500, 0],
 [3, 0, 400],
 [4, 500, 400],
 [5, 0, 700],
 [6, 500, 700],
 ]
        #El, Ni, Nf
#print(nodos[:])
tbl_Fuer = [
    
    #Nod, fx, fy, Mz
    [3,700, 0, 0],
    [5,1000, 0, 0],
    ]

tbl_Fuer_W = [
    #Elem, Li,Lf, Wi, Wf
    ["3", -12, -12,],
    ["6", -12, -12,],
    
 ]

tbl_Rest = [
        #Tipo de Apoyo, Nodo
        # Simple
        # Articulado
        # Empotrado
    ['Empotrado', 1],
    ['Empotrado', 2]
    ]


"""EJERCICIO 11.8 LIBRO Jairo Uribe """

E  = 19

tbl_Elem = [
    
  # Elem, Ni, Nf, b, h, E,
   ['1', 1, 2, 300, 500,E ],
 ['2', 3, 1,  300, 300,E],
 ['3', 4, 2,  300, 300, E],

]
    
tbl_Nod = [
    #Nodo, cx, cy
 [1, 0, 3000],
 [2, 6000, 3000],
 [3, 0, 0],
 [4, 6000, 0],
 ]
        #El, Ni, Nf
#print(nodos[:])
tbl_Fuer = [
    
    #Nod, fx, fy, Mz
    ]

tbl_Fuer_W = [
    #Elem, Li,Lf, Wi, Wf
    ["1",  -0.025, -0.025,],    
 ]

tbl_Rest = [
        #Tipo de Apoyo, Nodo
        # Simple
        # Articulado
        # Empotrado
    ['Empotrado', 3],
    ['Empotrado', 4]
    ]