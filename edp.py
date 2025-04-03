# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 12:15:46 2022

@author: Estudiante
"""

#Entrada_Datos_Prueba

import matplotlib.pyplot as plt
from propiedades_elementos import Propiedades_elemento

E  = 21*(1000**2)

tbl_Elem = [
    
  # Elem, Ni, Nf, b, h, E,
    ["1", 1, 2, 0.4, 0.4, E],
    ["2", 2, 4, 0.3, 0.3, E],
    ["3", 3, 4, 0.2, 0.5, E],


    ]
    
tbl_Nod = [
    #Nodo, cx, cy
    [1, 0, 0],
    [2, 0, 3],
    [3, 3, 0],
    [4, 3, 3],

    ]


tbl_Fuer = [
    #Nod, fx, fy, Mz
   # [2, 0, -20, 0],

    ]

tbl_Fuer_W = [
    #Elem, Li,Lf, Wi, Wf
    ["1", -20, -20],

    ]

tbl_Rest = [
        #Tipo de Apoyo, Nodo
        # Simple
        # Articulado
        # Empotrado
    ["Simple", 1],
    ["Simple", 3,],

    ]

"""====Diccionarios===="""
# ==============Diccionarios de elementos==================#

diccionarioE = {}

for i in range(len(tbl_Elem)):
    Elem = tbl_Elem[i][0]
    Ni = tbl_Elem[i][1]
    Nf = tbl_Elem[i][2]
    b = tbl_Elem[i][3]
    h = tbl_Elem[i][4]
    E = tbl_Elem[i][5]   
    diccionarioE[Elem] = [Ni, Nf, b, h, E]

# ==============Diccionarios de nodos==================#
    
diccionarioN = {}

for i in range(len(tbl_Nod)):
    Nod = tbl_Nod[i][0]
    cx = tbl_Nod[i][1]
    cy = tbl_Nod[i][2]
    diccionarioN[Nod] = [cx, cy]
    

elementos = [] # Almacena todos los elementos con sus propiedades

def ext_elem(): # Elementos fuera del analisis

    GDL = []
    #########---------->
    #Grados de libertad de los nodos
    #########---------->
    GDL_nodos = {}
    for i in range(len(tbl_Nod)):
        nodo = tbl_Nod[i][0]
        gdl = [nodo*3-3, nodo*3-2, nodo*3-1]
        GDL_nodos[nodo] = gdl   

    for i in range(len(tbl_Elem)):
        b = tbl_Elem[i][3]
        h = tbl_Elem[i][4]
            
        Elem = tbl_Elem[i][0]
        #print(Elem)
        Ni = tbl_Elem[i][1]
        Nf = tbl_Elem[i][2]
        conexion = [Elem, Ni, Nf]
        cxi = diccionarioN[Ni][0]
        cyi = diccionarioN[Ni][1]
        cxf = diccionarioN[Nf][0]
        cyf = diccionarioN[Nf][1]
            
        barra = Propiedades_elemento(Elem,b, h, E, cxi, cyi, cxf, cyf, conexion)
        elementos.append(barra) # Almacena elemento
    return elementos

ext_elem()
    



""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   
##############################
# DIBUJO DE BARRAS PORTICO
#############################
for i in range(len(tbl_Elem)):
    #i = 1
    Ele = tbl_Elem[i][0]
    Ni = tbl_Elem[i][1]
    Nf = tbl_Elem[i][2]
    #print(Ni)
    #print(Nf)
    xi = diccionarioN[Ni][0]
    yi = diccionarioN[Ni][1]
    xf = diccionarioN[Nf][0]
    yf = diccionarioN[Nf][1]
    #print(Ele,"({},{}),({},{})".format (xi, yi, xf, yf))
    #plt.plot([xi, xf], [yi, yf])
    
    plt.plot([xi, xf], [yi, yf],color = "black",linewidth=2)
    #plt.plot([xi, xf], [yi, yf],marker = "o",color = "#55aaff",  ms=10, )
   
#########################
# Dibujo de nodos
#########################
for i in range(len(tbl_Nod)):
    nodo = tbl_Nod[i][0]
    cxi = diccionarioN[nodo][0]
    cyi = diccionarioN[nodo][1]
    
    for j in range(len(tbl_Rest)):
        rst = tbl_Rest[j][0]
        n = tbl_Rest[j][1]
        
        
        if nodo == n:
           if rst == "Empotrado":
               plt.plot([cxi],[cyi], marker = '$\U000025AC$', ms = 20, color = "r")#'$\U000025A6$', ms = 20, color = "r")
           elif rst == "Articulado" :
               plt.plot([cxi],[cyi],"^b", ms = 10) 
           elif rst == "Simple" :
               plt.plot([cxi],[cyi],"og", ms = 10) 
               

#######################
#Delimitacion del dibujo
######################
xmax = 0
ymax = 0

for key in diccionarioN:
    
    valor_x = diccionarioN[key][0]
    valor_y = diccionarioN[key][1]
        
    if xmax < valor_x:
        xmax = valor_x
        
    if ymax < valor_y:
        ymax = valor_y
        
print("xmax: ", xmax, "ymax: ", ymax,)

###########################
# Dibujando fuerzas concentradas
###########################

for i in range(len(tbl_Fuer)):
    fuerzas = tbl_Fuer[i]
    #print("fuerza: ", fuerzas)
    nodo = fuerzas[0]
    #print("nodo: ", nodo)
    cx = diccionarioN[nodo][0]
    cy = diccionarioN[nodo][1]
    n_decim = 3
    fx = round(fuerzas[1], n_decim)
    fy = round(fuerzas[2], n_decim)
    Mz = round(fuerzas[3], n_decim)
    
    
    if fx > 0 or fx < 0:
        #print("fuer: ", fx)
        
        ####PENDIENTE POR INVESTICAR ANNOTATE
        plt.plot([cx- xmax*0.08],[cy], marker = '$\U00002192$', ms = 20, c ="#7D1E6A") #
        #plt.text(cx-xmax*0.35, cy+ymax*0.001, str(fx), color = "#7D1E6A", size = 8 ) 
        pass
    if fy > 0 or fy < 0 :
        #print("fuery: ",fy)
        plt.plot([cx- xmax*0.02],[cy+ymax*0.13], marker = '$\U00002193$', ms = 20, c ="#1A3C40") #U+2193
        #plt.text(cx+xmax*0.02, cy+ymax*0.12, str(fy), color = "#1A3C40", size = 8 ) 
        pass
        
    if Mz > 0  or Mz < 0:
         #plt.annotate("", xy = (cx, cy), xytext = (cx, cy+2), arrowprops = dict(arrowstyle = "simple", color = "y"), size = 20)
         #plt.annotate(str(fy), xy = (cx, cy), xytext = (cx+0.5, cy+1))
         plt.plot([cx+ xmax*0.05],[cy- ymax*0.12], marker = '$\U000021BA$', ms = 20, c ="#2F8F9D") #U+21BA
         #plt.text(cx+ xmax*0.12, cy - ymax*0.14, str(Mz), color = "#2F8F9D", size = 8 )
         pass
###########################
# Dibujo de fuerzas distribuidas
###########################
'''

for i in range(len(tbl_Fuer_W)):
    Elem = tbl_Fuer_W[i][0]
    wi = tbl_Fuer_W[i][1]
    wf = tbl_Fuer_W[i][2]
    
    #print("fuerza: ", fuerzas)
    nodo = fuerzas[0]
    #print("nodo: ", nodo)
    cx = diccionarioN[nodo][0]
    cy = diccionarioN[nodo][1]

    fx = fuerzas[1]
    fy = fuerzas[2]
    Mz = fuerzas[3]
    
    
    if fx > 0 or fx < 0:
        #print("fuer: ", fx)
        
        ####PENDIENTE POR INVESTICAR ANNOTATE
        plt.plot([cx- xmax*0.12],[cy], marker = '$\U00002192$', ms = 25, c ="#7D1E6A") #
        plt.text(cx-xmax*0.18, cy+ymax*0.12, str(fx), color = "#7D1E6A", size = 15 ) 
    if fy > 0 or fy < 0 :
        #print("fuery: ",fy)
        plt.plot([cx- xmax*0.02],[cy+ymax*0.13], marker = '$\U00002193$', ms = 25, c ="#1A3C40") #U+2193
        plt.text(cx+xmax*0.02, cy+ymax*0.12, str(fy), color = "#1A3C40", size = 15 ) 
        
        
    if Mz > 0  or Mz < 0:
         #plt.annotate("", xy = (cx, cy), xytext = (cx, cy+2), arrowprops = dict(arrowstyle = "simple", color = "y"), size = 20)
         #plt.annotate(str(fy), xy = (cx, cy), xytext = (cx+0.5, cy+1))
         plt.plot([cx+ xmax*0.05],[cy- ymax*0.12], marker = '$\U000021BA$', ms = 20, c ="#2F8F9D") #U+21BA
         plt.text(cx+ xmax*0.12, cy - ymax*0.14, str(Mz), color = "#2F8F9D", size = 15 )



'''

#######################################
# LIMITES DEL DIBUJO
#######################################
        
plt.xlim([-0.5 * xmax, 1.5 * xmax])# Limitando el eje x
plt.ylim([-0.5 * ymax, 1.5 * ymax])# Limitando el eje y

