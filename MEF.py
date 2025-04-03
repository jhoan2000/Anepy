#!/usr/bin/env python
# coding: utf-8


#from math import cos, sin, radians, sqrt, pi, atan, tan
# import matplotlib.pyplot as plt

# import Vector_fuerzas as VF
# import edp
# from edp import tbl_Elem, tbl_Nod, tbl_Fuer, tbl_Fuer_W, tbl_Rest, diccionarioE, diccionarioN

# from edp import ext_elem
from propiedades_elementos import Propiedades_elemento
# import Analisis_porticos
# from deformada import Deformada

import numpy as np
from math import sqrt, tan, radians

# # SUB-DIVISIONES

def Sub_E_N_F_FW_R(elementos,sub, tbl_Elem, tbl_Nod, tbl_Fuer, tbl_Fuer_W, tbl_Rest, diccionarioE, diccionarioN ):

    #sub = 2
    coordenadas = []
    coor_sub_elementos = []
    
    for i in range(len(tbl_Elem)):
        coord_p = [] # Guardado parcial
        Elemento = elementos[i]
        L = Elemento.L
        L_unitaria = L/sub
        
        cxi = Elemento.cxi
        cyi = Elemento.cyi
        cxf = Elemento.cxf
        cyf = Elemento.cyf
        
        ang = Elemento.ang
        for j in range(sub+1):
            
            # Elementos horizontales
            if ang == 0: 
                cy = cyi
                
                if cyf-cyi <0:
                    #print(i+1,"Yes",cyi,cyf )
                    
                    cx = round(cxi - L_unitaria*j,5)
                else:
                    cx = round(cxi + L_unitaria*j,5)
                    
                #cx = cxi + L_unitaria*j
                coord_p.append([cx,cy])
                
            # Elementos verticales
            elif abs(ang) == 90:
                
                cx = Elemento.cxi
                
                if cyf-cyi <0:
                    #print(i+1,"Yes",cyi,cyf )
                    cy = Elemento.cyi - round(L_unitaria*j,5)
                else:
                    cy = Elemento.cyi + round(L_unitaria*j,5)
                coord_p.append([cx,cy])
                    
            # Elementos inclinados crecientes
            elif ang > 0 and ang < 90:
                """estos fracmento forman l_uni en un triangulo rectangulo"""
                Ly_uni =  L_unitaria* sqrt(1/(1+(1/(tan(radians(ang))**2)))) # Longitud del fracmento en y
                Lx_uni = Ly_uni/tan(radians(ang)) # Longitud del fracmento en x
                #cx = Elemento.cxi + round(Lx_uni*j,5)
                #cy = Elemento.cyi + round(Ly_uni*j,5)
                
                #si la diferencia  entre las coordenadas de los nodos es negativa 
                # entonces corrige o invierte la o peracio + o -
                # Por ejem: Nf = (0,10), Ni = (20,10) x = (0-20), y = (10-10) como en x es negativa se debe restar L_uni..
                if cyf-cyi <0:
                    #print(i+1,"Yes",cyi,cyf )
                    cy =round( Elemento.cyi - Ly_uni*j,5)
                else:
                    cy = round(Elemento.cyi + Ly_uni*j,5)
                    
                if cxf-cxi <0:
                    #print(i+1,"Yes",cyi,cyf )
                    cx = round(Elemento.cxi - Lx_uni*j,5)
                else:
                    cx = round(Elemento.cxi + Lx_uni*j,5)
                    
                coord_p.append([cx,cy])
                
                #print("j=",j, "Ly= ",Ly_uni,"Lx= ",Lx_uni, "cx= ",cx, "cy= ", cy)
                    
            # Elementos inclinados decrecientes
            elif ang < 0:
                """estos fracmento forman l_uni en un triangulo rectangulo"""
                Ly_uni =  L_unitaria* sqrt(1/(1+(1/(tan(radians(ang))**2)))) # Longitud del fracmento en y
                Lx_uni = Ly_uni/tan(radians(ang)) # Longitud del fracmento en x
                
                cx = Elemento.cxi - round(Lx_uni*j,5)
                cy = Elemento.cyi - round(Ly_uni*j,5)
                   
                if cxf-cxi <0:
                   #print(i+1,"Yes",cyi,cyf )
                    cx = round(Elemento.cxi + Lx_uni*j,5)
                else:
                    cx = round(Elemento.cxi - Lx_uni*j,5)
                
                if cyf-cyi <0:
                    #print(i+1,"Yes",cyi,cyf )
                    cy =round( Elemento.cyi + Ly_uni*j,5)
                else:
                    cy = round(Elemento.cyi - Ly_uni*j,5)
                coord_p.append([cx,cy])
                
            #print(cx,cy)
            if [cx, cy] not in coordenadas: # Se chequea si la coord ya esta incluida
                coordenadas.append([cx,cy])
        coor_sub_elementos.append(coord_p)
    #coor_sub_elementos
    #coordenadas
    # Creacion de tbl de subnodos y diccionario de subnodos
    tbl_sub_nodos = []
    dic_sub_nodos = {}
    id_nodo = 0
    
    for n in range(len(coordenadas)):
        cx, cy = coordenadas[n]
        id_nodo += 1
        tbl_sub_nodos.append([id_nodo, cx, cy])
        dic_sub_nodos[id_nodo] = [cx, cy]
    
    # Creacion de tbl de subelementos y diccionario de subelementos x cada elemento
    tbl_sub_elementos = []
    dic_sub_elems_x_Elem = {}
    id_elementos = 0
    for i in range(len(tbl_Elem)):
        Elemento = elementos[i]
        Elem = Elemento.Elem
        b = Elemento.b
        h = Elemento.h
        E = Elemento.E
        angulo = Elemento.ang
        sub_elementos_p = []
        for j in range(sub):
            id_elementos += 1
            
            ci = coor_sub_elementos[i][j]
            cf = coor_sub_elementos[i][j+1]
    
            for m in range(len(tbl_sub_nodos)):
    
                N = m+1   
                
                if dic_sub_nodos[N] == ci:
                    Ni = N
                if dic_sub_nodos[N] == cf:
                    Nf = N  
            tbl_sub_elementos.append([str(id_elementos), Ni, Nf, b, h, E])
            sub_elementos_p.append([str(id_elementos), Ni, Nf, b, h, E])
        dic_sub_elems_x_Elem[Elem] = sub_elementos_p  
    
    # Creacion de diccionarios de  subelementos
    dic_sub_elementos = {}

    for i in range(len(tbl_sub_elementos)):
        Elem = tbl_sub_elementos[i][0]
        Ni = tbl_sub_elementos[i][1]
        Nf = tbl_sub_elementos[i][2]
        b = tbl_sub_elementos[i][3]
        h = tbl_sub_elementos[i][4]
        E = tbl_sub_elementos[i][5]   
        dic_sub_elementos[Elem] = [Ni, Nf, b, h, E]
    
    #Diccionario de nodos reales y correspondiente irreal
    # Creacion de diccionarios de nodos con su equivalencia en subnodos
    dic_nod_real_irreal =  {}
    for n in range(len(tbl_Nod)):
        coordenadas_reales = diccionarioN[n+1]
        for i in range(len(dic_sub_nodos)):
            sub_N = i+1
            if coordenadas_reales == dic_sub_nodos[sub_N]:
                Nod = sub_N
                dic_nod_real_irreal[n+1] = Nod
         

    
    
            
    #SUBFUERZAS
    tbl_sub_Fuer = []

    for j in range(len(tbl_Fuer)):
        Nod = tbl_Fuer[j][0]
        fx = tbl_Fuer[j][1]
        fy = tbl_Fuer[j][2]
        mz = tbl_Fuer[j][3]
        
        sub_N = dic_nod_real_irreal[Nod]
        tbl_sub_Fuer.append([sub_N, fx, fy, mz])


    #SUBRESTRICCIONES
    tbl_sub_restricciones = []

    for j in range(len(tbl_Rest)):
        N_rest = tbl_Rest[j][1]
        tipo = tbl_Rest[j][0]
        sub_N = dic_nod_real_irreal[N_rest]
        tbl_sub_restricciones.append([tipo, sub_N])    
    
    
    #SUBELEMENTOS
    sub_elementos = [] # Almacena todos los elementos con sus propiedades
    for i in range(len(tbl_sub_elementos)):
        Ni = tbl_sub_elementos[i][1]
        Nf = tbl_sub_elementos[i][2]
        b = tbl_sub_elementos[i][3]
        h = tbl_sub_elementos[i][4]
        Ele = tbl_sub_elementos[i][0]    
        conexion = [Ele, Ni, Nf]
        xi = dic_sub_nodos[Ni][0]
        yi = dic_sub_nodos[Ni][1]
        xf = dic_sub_nodos[Nf][0]
        yf = dic_sub_nodos[Nf][1]     
        barra = Propiedades_elemento(Ele,b, h, E, xi, yi, xf, yf, conexion)
        sub_elementos.append(barra) # Almacena elemento

    #SUBFUERZAS W
    
    tbl_sub_F_W = []

    for i in range(len(tbl_Fuer_W)):
        Elemento = tbl_Fuer_W[i][0]
        wi = tbl_Fuer_W[i][1]
        wf = tbl_Fuer_W[i][2]
        L = 0
        
        for n in range(len(elementos)): # Extrae la longitud del elemento sin sub...
            if Elemento == elementos[n].Elem:
                L = elementos[n].L

        for j in range(sub):
            
            Elem = dic_sub_elems_x_Elem[Elemento][j][0]
       
            ################################################
            ################################################
            # Carga distibuida rectangular
            #print(wi, wf)
            if wi == wf:
                
                L_unitaria = L/sub*(j+1)
                #print(L_unitaria)
                sub_W = wi
                tbl_sub_F_W.append([Elem, sub_W , sub_W])
                
                
            #################################################
            #################################################
                
            # Carga distibuida triangular decreciente
            
            if  abs(wf) == 0:
                
                W = wi
                L_unitaria = L/sub
                sub_wi = (W * L_unitaria * j) /L 
                sub_wf = (W * L_unitaria * (j+1))/L
                tbl_sub_F_W.append([Elem, sub_wf, sub_wi])
            
            
            # Carga distibuida triangular creciente
            if  abs(wi) == 0:
                
                W = wf
                L_unitaria = L/sub
                sub_wi = (W * L_unitaria * j) /L 
                sub_wf = (W * L_unitaria * (j+1))/L
                tbl_sub_F_W.append([Elem, sub_wi , sub_wf])
            
            # Carga distibuida trapezoidal decreciente
            if  abs(wi) > abs(wf) and abs(wf) > 0:
                
                W = (wi - wf)
                L_unitaria = L/sub
                sub_wi = (W * L_unitaria * j) /L + wf
                sub_wf = (W * L_unitaria * (j+1))/L + wf
                tbl_sub_F_W.append([Elem, sub_wf, sub_wi])
            
            # Carga distibuida trapezoidal creciente
            if  abs(wi) < abs(wf) and abs(wi) > 0:
                
                W = (wf - wi)
                L_unitaria = L/sub
                sub_wi = wi + (W * L_unitaria * j) /L
                sub_wf = wi + (W * L_unitaria * (j+1))/L
                tbl_sub_F_W.append([Elem, sub_wi , sub_wf])

    return tbl_sub_elementos, dic_sub_elementos, tbl_sub_nodos, dic_sub_nodos,tbl_sub_Fuer, tbl_sub_F_W, tbl_sub_restricciones, sub_elementos, dic_nod_real_irreal



def nodo_ireal(diccionarioN,dic_sub_nodos, nodo):
    coordenadas_reales = diccionarioN[nodo]
    for i in range(len(dic_sub_nodos)):
        sub_N = i+1
        if coordenadas_reales == dic_sub_nodos[sub_N]:
            Nod = sub_N
            return Nod

"""METODO DE LOS ELEMENTOS FINITOS """


# sub = 100

# tbl_sub_elementos, dic_sub_elementos, tbl_sub_nodos, dic_sub_nodos,tbl_sub_Fuer, tbl_sub_F_W, tbl_sub_restricciones, sub_elementos, dic_nod_real_irreal = Sub_E_N_F_FW_R(edp.elementos,sub, tbl_Elem, tbl_Nod, tbl_Fuer, tbl_Fuer_W, tbl_Rest, diccionarioE, diccionarioN )
# #print(tbl_Fuer)
# tbl_Elem = tbl_sub_elementos
# tbl_Nod = tbl_sub_nodos
# tbl_Fuer = tbl_sub_Fuer
# tbl_Fuer_W = tbl_sub_F_W 
# tbl_Rest = tbl_sub_restricciones
# diccionarioE = dic_sub_elementos
# diccionarioN = dic_sub_nodos
# elementos =  sub_elementos


# vector_fuerzas = VF.Vector_fuerzas_externas(sub_elementos,[tbl_Elem, tbl_Nod, tbl_Fuer, tbl_Rest,tbl_Fuer_W,len(elementos)], 
#                                             diccionarioN, diccionarioE)


# tbl_Fuer = vector_fuerzas.tbl_Fuer # Tabla de la suma de fuerzas que llegan al los nodos vector para corformacion del vector fuerzas
# dic_tf = vector_fuerzas.dic_tf
# dic_vecF_ext_Elem = vector_fuerzas.dic_vecF_ext_Elem


# Portico = Analisis_porticos.Analisis_matricial(tbl_Elem, tbl_Rest, tbl_Nod, dic_tf, diccionarioN, dic_vecF_ext_Elem)


# Desplazamientos = {}
# Elementos = np.asarray(tbl_Elem)
# Nodos =  np.asarray(tbl_Nod)

# Desplazamientos_elementos = Portico.d_elem

# # Coordenadas con nodos desplazados
# """En este apartado se va a sumar a las coordenadas 
# iniciales los desplazamientos.

# Los deplazmientos se van amplificar en 100 veces, para 
# objeto de visualizacion"""


# f_amp = 200 # costante de amplificacion

# datos_deformada = Deformada(elementos, Desplazamientos_elementos, f_amp)

# ##############################
# # DIBUJO DE BARRAS PORTICO
# #############################
# for i in range(len(tbl_Elem)):
#     #i = 1
#     Ele = tbl_Elem[i][0]
#     Ni = tbl_Elem[i][1]
#     Nf = tbl_Elem[i][2]
#     #print(Ni)
#     #print(Nf)
#     xi = diccionarioN[Ni][0]
#     yi = diccionarioN[Ni][1]
#     xf = diccionarioN[Nf][0]
#     yf = diccionarioN[Nf][1]
#     #print(Ele,"({},{}),({},{})".format (xi, yi, xf, yf))
#     #plt.plot([xi, xf], [yi, yf])
    
#     plt.plot([xi, xf], [yi, yf],color = "black",linewidth=3)
#     #plt.plot([xi, xf], [yi, yf],marker = "o",color = "#55aaff",  ms=10, )
   





# ##############################
# # DIBUJO DE LA ELASTICA DE LAS BARRAS
# #############################


# for i in range(len(elementos),):
#     Ni = elementos[i].conex[1]
#     Nf = elementos[i].conex[2]
    
#     xi = datos_deformada.dic_deformada[Ni][0]
#     yi = datos_deformada.dic_deformada[Ni][1]
#     xf = datos_deformada.dic_deformada[Nf][0]
#     yf = datos_deformada.dic_deformada[Nf][1]
#     #print(Ele,"({},{}),({},{})".format (xi, yi, xf, yf))
#     #plt.plot([xi, xf], [yi, yf]) # Lineas con colores diferentes
    
#     plt.plot([xi, xf], [yi, yf],"b--",linewidth=2)
#     # plt.plot([xi, xf], [yi, yf],marker = "o",color = "#55aaff",  ms=1, ) # Para mostrar subdivisiones
    
#     #plt.plot([xi], [yi],"b--",linewidth=2)
#     #plt.plot([xi],[yi],"og", ms = 4) 
    
    
    


"""d_agregados = [] # Comprueba los desplazamientos ya agregados
tbl_Nod_desplazados = []

for i in range(len(elementos)):
    Ni = elementos[i].conex[1]
    Nf = elementos[i].conex[2]
    
    cx_i = elementos[i].cxi # Cordenadas del xi de Ni
    cy_i = elementos[i].cyi # Cordenadas del yi de Ni
    cx_f = elementos[i].cxf # Cordenadas del xf de Nf
    cy_f = elementos[i].cyf # Cordenadas del yf de Nf
    
    if Ni not in d_agregados:
        cd_xi = cx_i + Desplazamientos[Ni][0][0] * amp
        cd_yi = cy_i + Desplazamientos[Ni][1][0] * amp
        tbl_Nod_desplazados.append([Ni, cd_xi, cd_yi])
    #cd_zi = cx_i + Desplazamientos[Ni][0] * amp # Pendiente grafico del giro
    if Nf not in d_agregados:
        cd_xf = cx_f + Desplazamientos[Nf][0][0] * amp
        cd_yf = cy_f + Desplazamientos[Nf][1][0] * amp
        #cd_zi = cz_i + Desplazamientos[Nf][0] * amp
        tbl_Nod_desplazados.append([Nf, cd_xf, cd_yf])
    
    
    d_agregados.append(Ni)
    d_agregados.append(Nf)
 
##############################
# DICCIONARIO DE DESPLAZAMIENTOS
#############################
diccionarioN_desplazados = {}

for i in range(len(tbl_Nod_desplazados)):
    Nod = tbl_Nod_desplazados[i][0]
    cx = tbl_Nod_desplazados[i][1]
    cy = tbl_Nod_desplazados[i][2]
    diccionarioN_desplazados[Nod] = [cx, cy]


##############################
# DIBUJO DE LA ELASTICA DE LAS BARRAS
#############################
for i in range(3):
    Ni = elementos[i].conex[1]
    Nf = elementos[i].conex[2]
    #print(Ni)
    #print(Nf)
    xi = diccionarioN_desplazados[Ni][0]
    yi = diccionarioN_desplazados[Ni][1]
    xf = diccionarioN_desplazados[Nf][0]
    yf = diccionarioN_desplazados[Nf][1]
    #print(Ele,"({},{}),({},{})".format (xi, yi, xf, yf))
    #plt.plot([xi, xf], [yi, yf]) # Lineas con colores diferentes
    
    plt.plot([xi, xf], [yi, yf],"b--",linewidth=2)
    # plt.plot([xi, xf], [yi, yf],marker = "o",color = "#55aaff",  ms=1, ) # Para mostrar subdivisiones
    
"""