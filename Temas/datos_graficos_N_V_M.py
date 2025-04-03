# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 10:01:25 2022

@author: Estudiante
"""

# def main():
#     Desplazamientos = {}
#     Fuerzas_Internas = Portico_A.F_Internas_E
#     Elementos = np.asarray(tbl_Elem)
#     Nodos =  np.asarray(tbl_Nod)

#     Desplazamientos_elementos = Portico_A.g_delta_elemento

#     # Desplazamiento de por cada nodo

#     d_agregados = [] # Comprueba los desplazamientos ya agregados
#     for i in range(len(elementos)):
#         Ni = elementos[i].conex[1]
#         Nf = elementos[i].conex[2]
        
#         if Ni not in d_agregados:
#             #print(Ni)
#             # Desplazmiento en el nodo inicial, se obtiene de los desplazamiento por elemento
#             dx_i = Desplazamientos_elementos[i][0]
#             dy_i = Desplazamientos_elementos[i][1]
#             dz_i = Desplazamientos_elementos[i][2]
#             Desplazamientos[Ni] = [dx_i, dy_i, dz_i] # Se agregan a un diccionario en f(N)
            
#         if Nf not in d_agregados:
#         # Desplazmiento en el nodo inicial
#             #print(Nf)
#             dx_f = Desplazamientos_elementos[i][3]
#             dy_f = Desplazamientos_elementos[i][4]
#             dz_f = Desplazamientos_elementos[i][5]
#             Desplazamientos[Nf] = [dx_f, dy_f, dz_f]

#         d_agregados.append(Ni)  
#         d_agregados.append(Nf)
#         # print(d_agregados)
#         # print(Desplazamientos)

#     # Coordenadas con nodos desplazados
#     """En este apartado se le va a sumar a las coordenadas 
#     iniciales los desplazamientos.

#     Los deplazmientos se van amplificar en 100 veces, para 
#     objeto de visualizacion"""


#     amp = 1000 # controlar con un desplizador
#     d_agregados = [] # Comprueba los desplazamientos ya agregados
#     tbl_Nod_desplazados = []

#     for i in range(len(elementos)):
#         Ni = elementos[i].conex[1]
#         Nf = elementos[i].conex[2]
        
#         cx_i = elementos[i].cxi # Cordenadas del xi de Ni
#         cy_i = elementos[i].cyi # Cordenadas del yi de Ni
#         cx_f = elementos[i].cxf # Cordenadas del xf de Nf
#         cy_f = elementos[i].cyf # Cordenadas del yf de Nf
        
#         if Ni not in d_agregados:
#             cd_xi = cx_i + Desplazamientos[Ni][0][0] * amp
#             cd_yi = cy_i + Desplazamientos[Ni][1][0] * amp
#             tbl_Nod_desplazados.append([Ni, cd_xi, cd_yi])
#         #cd_zi = cx_i + Desplazamientos[Ni][0] * amp # Pendiente grafico del giro
#         if Nf not in d_agregados:
#             cd_xf = cx_f + Desplazamientos[Nf][0][0] * amp
#             cd_yf = cy_f + Desplazamientos[Nf][1][0] * amp
#             #cd_zi = cz_i + Desplazamientos[Nf][0] * amp
#             tbl_Nod_desplazados.append([Nf, cd_xf, cd_yf])
        
        
#         d_agregados.append(Ni)
#         d_agregados.append(Nf)
     
#     ##############################
#     # DICCIONARIO DE DESPLAZAMIENTOS
#     #############################
#     diccionarioN_desplazados = {}

#     for i in range(len(tbl_Nod_desplazados)):
#         Nod = tbl_Nod_desplazados[i][0]
#         cx = tbl_Nod_desplazados[i][1]
#         cy = tbl_Nod_desplazados[i][2]
#         diccionarioN_desplazados[Nod] = [cx, cy]


#     ##############################
#     # DIBUJO DE LA ELASTICA DE LAS BARRAS
#     #############################
#     for i in range(len(tbl_Elem)):
#         #i = 1
#         Ele = tbl_Elem[i][0]
#         Ni = tbl_Elem[i][1]
#         Nf = tbl_Elem[i][2]
#         #print(Ni)
#         #print(Nf)
#         xi = diccionarioN_desplazados[Ni][0]
#         yi = diccionarioN_desplazados[Ni][1]
#         xf = diccionarioN_desplazados[Nf][0]
#         yf = diccionarioN_desplazados[Nf][1]
#         #print(Ele,"({},{}),({},{})".format (xi, yi, xf, yf))
#         #plt.plot([xi, xf], [yi, yf]) # Lineas con colores diferentes
        
#         #plt.plot([xi, xf], [yi, yf],"b--",linewidth=1)
#         # plt.plot([xi, xf], [yi, yf],marker = "o",color = "#55aaff",  ms=1, ) # Para mostrar subdivisiones
        

#     ##############################
#     # GRAFICO DE FUERZAS AXIALES
#     #############################

#     Fuerzas_Internas_Elementos = Portico_A.F_Internas_E


#     # Desplazamiento de por cada nodo
#     Fuerzas_Internas = []
#     F_agregadas = [] # Comprueba los desplazamientos ya agregados
#     contador = 0
#     for i in range(len(elementos)):
#         contador += 1

#         id_Elem = str(i+1)
        
#         F_agregadas.append(Fuerzas_Internas_Elementos[i])
#         if contador == sub:
#             Fuerzas_Internas.append(F_agregadas)
#             F_agregadas = [] # Comprueba los desplazamientos ya agregados
#             contador = 0
#     can_Elemento = int(len(elementos)/sub)
#     lista_F_axial_colum = []
#     lista_F_axial_vig = []


#     """----MAXIMOS Y MINIMOS EN VIGAS Y COLUMNAS---"""

#     for i in range(len(elementos)):
#         Fx = Fuerzas_Internas_Elementos[i][0]
#         ang = elementos[i].ang
#         if ang == 90:
#             lista_F_axial_colum.append(abs(Fx))
#         if ang > 0 or ang <0 : # Se combina los elementos inclinados con las vigas
#             lista_F_axial_vig.append(abs(Fx))
#     max_min_Fx_col = (max(lista_F_axial_colum)[0],min(lista_F_axial_colum)[0])

#     max_min_Fx_vig =(max(lista_F_axial_vig)[0],min(lista_F_axial_vig)[0])
#     y_max =ymax # Y max en el dibujo
#     x_max =  xmax # X max en el dibujo
#     print("maximos: ",max_min_Fx_col,max_min_Fx_vig, x_max, y_max)

#     #-----------------------------------#
#     """FUERZAS AXIAL EN COLUMNAS"""
#     #------------------------------------#
#     amp_col = 0 # Factor Amplificacion en columnas
#     F_amp = 0 # Fuerza max amplificada
#     lista_fac_i = [0.001, 0.01, 0.1,1,10] # Posibles factores de amplificacion

#     """ En este bucle se aplican los posicles factores de 
#         amplificacion base y se escoge el maximo que cumple con la condicion:
#         la maxima fuerza amplificada entre el maximo valor de las cx en el 
#         dibujo debe ser menor al 16%, lo que permite que la linea 
#         en el grafico se separe al rededor de ese valorde la linea original
#         conservando la proporcionañlidad entre las lineas del mismo tipo
#         de elementos"""

#     for i in lista_fac_i:
#         if max_min_Fx_col[0]*i/x_max <0.16:
#             factor_i = i
#     #print("fac",factor_i)
#     i = 0

#     """
#         Se acumula el facor de amplificacion hasta que se cumple la condicion 
#         de forma mas precisa"""
#     while F_amp/x_max < 0.16:
#         F_amp=  max_min_Fx_col[0]*i
#         amp_col = i
#         i +=factor_i

#     Y = []
#     F_Axial = []

#     amp_fx = amp_col #amp_col
#     contador = 0
#     can_Elemento = len(elementos)/sub

#     for j in range(int(can_Elemento)):
#         sub_fuerzas = Fuerzas_Internas[j]
#         Fx = []
#         y = []
#         for i in range(sub):
#             contador += 1
#             #print(contador)
            
#             Elemento =  elementos[contador-1]
#             ang = elementos[contador-1].ang
#             Ni = Elemento.conex[1]
#             Nf = Elemento.conex[2]
#             # print(Ni)
#             # print(Nf)
            
#             xi = diccionarioN[Ni][0]
#             yi = diccionarioN[Ni][1]
#             xf = diccionarioN[Nf][0]
#             yf = diccionarioN[Nf][1]  
#             #print(Ni,xi, yi)
#             #print(Nf, xf, yf)
#             F_i = sub_fuerzas[i][0][0]
#             F_f = sub_fuerzas[i][3][0]
#             f = F_i
#             if ang == 90:
                
                
#                 i = i+1
#                 if i == 1 :
#                     y.append(yi)
#                     F = 0 + xi
#                     Fx.append(F)
#                     #print("X", yi, "Fx", F)
#                     y.append(yi)
#                     F = xi + F_i*amp_fx
#                     Fx.append(F)
#                     #print("X", yi, "Fx", F)
#                 # elif i > 1 and i < sub:
#                 #     y.append(yi)
#                 #     F = xi + F_i*amp_fx
#                 #     Fx.append(F)
#                 #     #print("X", yi, "Fx", F)
#                 elif i == sub:
#                     y.append(yf)
#                     Fx.append(F)
#                     #print("X", yf, "Fx", F)
#                     #Tramo
#                     y.append(yf)
#                     F = xf + F_i+F_f
#                     Fx.append(F)
#                     #print("X", yf, "Fx", F)
#         if  (y and Fx) != [] :  
#             #print(x)
#             Y.append(y)
#             F_Axial.append(Fx)


#     #print("y:", Y)            
#     # print("F:", F_Axial)

#     for i in range(len(F_Axial)):
#         #plt.plot(F_Axial[i],Y[i] ,"g",linewidth=1)
#         pass
        

#     #-----------------------------------#
#     """FUERZAS AXIAL EN VIGAS"""
#     #------------------------------------#


#     amp_vig = 0
#     #for i in range(16):
#     amp_p = 0

#     lista_fac_i = [0.001, 0.01, 0.1,1,10] # Posibles factores de amplificacion

#     for i in lista_fac_i:
#         if max_min_Fx_vig[0]*i/y_max <0.16:
#             factor_i = i

#     i = 0
#     while amp_p/y_max < 0.16 and (y_max+amp_vig*max_min_Fx_vig[0]) < 1.15 * y_max :
#         amp_p =  max_min_Fx_vig[0]*i
#         #amp_p = max_min_Fx_col[0]+amp_p*x_max i/10 #amplificador parcial hasta un 115%
#         amp_vig = i
#         #print(i, "-", amp_p)
#         i +=factor_i

#     X = []
#     F_Axial_v = [] # Para vigas
#     #print("xmax: ", xmax, "ymax: ", ymax,)


#     amp_fx = amp_vig
#     amp_coord = 0
#     contador = 0
#     for j in range(int(can_Elemento)):
#         sub_fuerzas = Fuerzas_Internas[j]
#         Fx = []
#         x = []
#         f = 0
#         for i in range(sub):
#             contador += 1
#             #print(contador)
            
#             Elemento =  elementos[contador-1]
#             ang = elementos[contador-1].ang
#             Ni = Elemento.conex[1]
#             Nf = Elemento.conex[2]
#             # print(Ni)
#             # print(Nf)
            
#             xi = diccionarioN[Ni][0]
#             yi = diccionarioN[Ni][1]
#             xf = diccionarioN[Nf][0]
#             yf = diccionarioN[Nf][1] 
            
#             F_i = sub_fuerzas[i][0][0]
#             F_f = sub_fuerzas[i][3][0]
#             #print(F_i,F_f)
            
#             if ang == 90:
#                 #print(F_i,F_f)
#                 # print(Ni,xi, yi)
#                 # print(Nf, xf, yf)
                
#                 i = i+1
#                 if i == 1 :
#                     x.append(xi)
#                     F = yi 
#                     Fx.append(F)
#                     #print("X", xi, "Fx", F)
#                     x.append(xi)
#                     F = yi + F_i*amp_fx
#                     Fx.append(F)
#                     f = F
#                     #print("X", xi,"yi",yi,"F_i", F_i, "Fx", F)
#                 # elif i > 1 and i < sub:
#                 #     x.append(xi)
#                 #     F = yi + F_i*amp_fx
#                 #     Fx.append(F)
#                 #     #print("X", xi, "Fx", F)
#                 #     #Tramo
#                 #     x.append(xi)
#                 #     F = yi + F_i*amp_fx
#                 #     Fx.append(F)
#                 #     #print("X", xf, "Fx", F)
#                 elif i == sub:
#                     #Tramo
#                     x.append(xf)
#                     # if F_i>0:
#                     #     F = yf + F_f*amp_fx*-1
#                     # else:
#                     #     F = yf + F_f*amp_fx*-1
#                     # #print("X", xf, "Fx", F)
#                     # if F_f<0:
#                     #     Fx.append(yf+F_f*amp_fx*-1)
#                     # else: 
#                     #     Fx.append(yf+F_i*amp_fx)
#                     F = f
#                     Fx.append(F)
#                     #print("X1", xf, "Fx", F)
#                     #Tramo
#                     x.append(xf)
#                     F = yf + F_i+F_f
#                     Fx.append(F)
#                     #print("X1", xf, "Fx", F)
            
#         if  (x and Fx) != [] :  
#             #print(x)
#             pass
#             #X.append(x)
#             #F_Axial_v.append(Fx)

#     # print(X)
#     # print(F_Axial_v)

#     for i in range(len(F_Axial_v)):
#         plt.plot(X[i],F_Axial_v[i] ,"b",linewidth=1)


#     ########################################3
#     #----ELEMENTOS INCLINADOS----
#     ###################################
#     X = []
#     F_Axial_inc = [] # Para elementos inclinados
#     #print("xmax: ", xmax, "ymax: ", ymax,)


#     amp_fx = amp_vig
#     print("amp_e_incli", amp_vig)
#     amp_coord = 0
#     contador = 0
#     for j in range(int(can_Elemento)):
#         sub_fuerzas = Fuerzas_Internas[j]
#         Fx = []
#         x = []
#         f = 0
#         for i in range(sub):
#             contador += 1
#             #print(contador)
            
#             Elemento =  elementos[contador-1]
#             ang = elementos[contador-1].ang
#             Ni = Elemento.conex[1]
#             Nf = Elemento.conex[2]
#             # print(Ni)
#             # print(Nf)
            
#             xi = diccionarioN[Ni][0]
#             yi = diccionarioN[Ni][1]
#             xf = diccionarioN[Nf][0]
#             yf = diccionarioN[Nf][1] 
            
#             F_i = sub_fuerzas[i][0][0]
#             F_f = sub_fuerzas[i][3][0]
            
            
#             if ang >0 and ang < 90:
#                 print(F_i,F_f)
                
#                 #print(F_i,F_f)
#                 # print(Ni,xi, yi)
#                 # print(Nf, xf, yf)
                
#                 i = i+1
#                 if i == 1 :
#                     x.append(xi)
#                     F = yi 
#                     Fx.append(F)
#                     #print("X", xi, "Fx", F)
#                     x.append(xi)
#                     F = yi + F_i*amp_fx
#                     Fx.append(F)
#                     f = F
                    
#                 elif i == sub:
#                     x.append(xf)
#                     if F_f <0:
#                         F_f = F_f*-1
#                     F = yf + F_f*amp_fx
#                     Fx.append(F)
#                     #print("X1", xf, "Fx", F)
#                     #Tramo
#                     x.append(xf)
#                     F = yf 
#                     Fx.append(F)
#                     #print("X1", xf, "Fx", F)
            
#         if  (x and Fx) != [] :  
#             #print(x)
#             X.append(x)
#             F_Axial_inc.append(Fx)

#     print(X)
#     print(F_Axial_inc)

#     for i in range(len(F_Axial_inc)):
#         plt.plot(X[i],F_Axial_inc[i] ,"b",linewidth=1)
#         pass


#     """CORTANTE EN ELEMENTOS"""


#     lista_F_v_colum = []
#     lista_F_v_vig = []


#     """----MAXIMOS Y MINIMOS EN VIGAS Y COLUMNAS---"""

#     for i in range(len(elementos)):
#         Fv = Fuerzas_Internas_Elementos[i][1]
#         ang = elementos[i].ang
#         if ang == 90:
#             lista_F_v_colum.append(abs(Fv))
#         if ang > 0 or ang <0 : # Se combina los elementos inclinados con las vigas
#             lista_F_v_vig.append(abs(Fv))
#     max_min_Fv_col = (max(lista_F_v_colum)[0],min(lista_F_v_colum)[0])

#     max_min_Fv_vig =(max(lista_F_v_vig)[0],min(lista_F_v_vig)[0])
#     y_max =ymax # Y max en el dibujo
#     x_max =  xmax # X max en el dibujo
#     print("maximos: ",max_min_Fv_col,max_min_Fv_vig, x_max, y_max)

