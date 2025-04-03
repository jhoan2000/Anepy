# -*- coding: utf-8 -*-
"""
Created on Wed May 11 00:08:42 2022

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

# manejo de matrices
import numpy as np
np.set_printoptions(precision=5, suppress=True) # cantidad de decimales

# from MEF import Sub_E_N_F_FW_R, nodo_ireal
from propiedades_elementos import Propiedades_elemento
# import Vector_fuerzas as VF
# from edp import tbl_Elem, tbl_Nod, tbl_Fuer, tbl_Fuer_W, tbl_Rest, diccionarioE, diccionarioN, elementos
# from edp import ext_elem

#=====Calculo de Cortantes y de Momentos de Empotramientos Perfecto



# ENTRADA DE DATOS 


  
# ==============Diccionarios de fuerzas concentradas==================#

# vector_fuerzas = VF.Vector_fuerzas_externas(elementos,[tbl_Elem, tbl_Nod, tbl_Fuer, tbl_Rest,tbl_Fuer_W,len(elementos)], 
#                                             diccionarioN, diccionarioE)

# tbl_Fuer = vector_fuerzas.tbl_Fuer # Tabla de la suma de fuerzas que llegan al los nodos vector para corformacion del vector fuerzas
# dic_tf = vector_fuerzas.dic_tf
# dic_vecF_ext_Elem = vector_fuerzas.dic_vecF_ext_Elem



########################################
#-----------------ANALISIS MATRICIAL----
########################################

class Analisis_matricial():
    def __init__(self,tbl_Elem, tbl_Rest,tbl_Nod, dic_tf, dic_Nod, dic_vecF_ext_Elem):

        self.dicf = dic_tf # diccionario de fuerza
        self.dicNod = dic_Nod # diccionario de nodos
        self.tbl_Elem = tbl_Elem # Tabla de elementos
        self.nElem = len(self.tbl_Elem) # Cantidad de elementos
        self.nodos = tbl_Nod
        juli = tbl_Nod
        [self.gdlN,self.GDL, self.Elementos_creados  ] = self.Porticos() # Grado de libertad del nodo|matrices de rigidez global|grados de libres
        self.nN = len(self.gdlN)
        self.MGlobal = []
        for i in self.Elementos_creados:
            self.MGlobal.append(i.KG)
            
        self.dic_vecFW_exe_elem = dic_vecF_ext_Elem
        
        #print("f",self.dicf)
        
        self.tr = tbl_Rest # Tabla de restricciones
        self.ntrs = len(self.tr) # numero de restricciones
        self.nFuerzas = len(self.dicf)  # Tabla de fuerzas por nodo [x,y,z]
        
        self.dimen = len(self.gdlN) * 3 # Calcula las dimensiones de la matriz global
        self.K_global = np.zeros((self.dimen, self.dimen)) # MATRIZ GLOBALde ceros
        self.KG = self.ensamble() # Matriz global emsamblada
        self.rst = self.restricciones() # Nodos restringidos
        self.gl = self.grados_libres() # Grados libres 
        self.MGL = self.Matriz_grados_libre() # Matriz global de grados libres o sin restricciones
        self.F = self.vector_fuerza() # Vector fuerza en los grados libres
        self.F_ext_elem = self.fuerzas_ex_elem() # Fuerzas externas por elementos
        self.IMGL = self.inversa_MGL() # Inversa de la matriz Global de grados libres
        self.Desplazmiento_GL, self.delta_g = self.desplazamientos_GL() # desplazamiento en grados y grados-desplazamiento
        self.g_delta, self.dic_g_delta = self.grado_desplazamiento() # Grado-Desplazamiento 
        self.d_elem, self.g_delta_elemento = self.grados_delta_elemento() # Desplazamiento de grados por cada elemento
        self.delta_Local_Elementos = self.T_delta_L() # Transformacion de desplazamientos del sistema global al local
        self.F_Internas_E = self.fuerzas_internas_elementos() # Fuerzas internas de cada elemento

    def __str__(self):
        print("tbl_F")
        print(self.dicf)
        print("Matriz de rigides global ensamblada", "dimensiones: ",self.K_global.shape)
        print(self.KG)
        print("")
        print("Grados restringidos: ", self.rst)
        print("Matriz de grados libres")
        print(self.MGL)
        print("")
        print("Nodos Libres")
        print(self.Nl)
        print("Inversa de la matriz de grados libre")
        print(self.IMGL)
        print("Grados Libres")
        print(self.gl)
        print("Vector de fuerzas")
        print(self.F)
        print("")
        print("Desplazamiento en grados libres")
        print(self.Desplazmiento_GL)
        print("")
        print("Discionario desplazamientop por grados")
        print(self.dic_g_delta)
        print("Desplazamiento en todos los grados")
        print(self.g_delta)
        print("")
        print("Desplazamiento por elementos")
        print(self.g_delta_elemento)
        print("")
        print(self.F_Internas_E)
        
        
        
        return ""
    
        
        
    
    """===INFORMACION GENERAL CON TODOS LOS DATOS POR ELEMENTOS ===
    Matrices de rigidez globales, grados de libertad y grados libres por nodo"""
    
    def Porticos(self):
        #######################################
        #-----------------ANALISIS 1------------
        ########################################
        elementos = [] # Almacena todos los elementos con sus propiedades

        GDL = []

        #########---------->
        #Grados de libertad de los nodos
        #########---------->
        GDL_nodos = {}
        for i in range(len(self.nodos)):
        
            nodo = self.nodos[i][0]
            gdl = [nodo*3-3, nodo*3-2, nodo*3-1]
            GDL_nodos[nodo] = gdl
        #print(GDL_nodos)   

        #########---------->
        # Datos de entrada y Matrices de rigidez global de cada elemento 
        #########---------->
        for i in range(len(self.tbl_Elem)):
            b = self.tbl_Elem[i][3]
            h = self.tbl_Elem[i][4]
            E = self.tbl_Elem[i][5]
            
            Ele = self.tbl_Elem[i][0]
            Ni = self.tbl_Elem[i][1]
            Nf = self.tbl_Elem[i][2]
            conexion = [Ele, Ni, Nf]
            xi = self.dicNod[Ni][0]
            yi = self.dicNod[Ni][1]
            xf = self.dicNod[Nf][0]
            yf = self.dicNod[Nf][1]
            
            barra = Propiedades_elemento(Ele,b, h, E, xi, yi, xf, yf, conexion)
            elementos.append(barra) # Almacena elemento
            #print(elem)
            GDL.append(barra.gdl[0])
            
        GDL = np.asarray(GDL)
        
        return GDL_nodos, GDL, elementos
        
        
    """ EMSABLE DE ELEMENTOS EN LA MATRIZ GLOBAL EN FUNCION DE SUS GRADOS DE LIBERTAD"""
    def ensamble(self):
        #print(self.K_global.shape)
        cont = 0
        for n in range(len(self.GDL)): # Se recorren todo los elementos
            GDL_elemento = self.GDL[n] # Se asignan los 6 grado de libertad por elemento
            #print(GDL_elemento)
            
            for j in range(6): # Recorre los grados de libertan de forma horizontal
                for i in range(6): # Recorre los grados de libertan de forma vertical
                    self.K_global[GDL_elemento[j],GDL_elemento[i]] = self.Elementos_creados[n].KG[j,i] + self.K_global[GDL_elemento[j],GDL_elemento[i]]
                   
        return self.K_global
    

    """ CALCULA LOS GRADOS RESTRINGIDOS EN FUNCION DE LOS APOYOS """
    def restricciones(self):

        RST = []
        #print(self.tr)
        for i in range(len(self.tr)):
            nodo = self.tr [i][1]  #(x = nudo, y = el nudo donde sale)
            tipo_rst = self.tr [i][0]
            # Se chequea el tipo de apoyo y se asinas los grados restringidos
            # En funcion del numeo del nodo
            if tipo_rst == "Empotrado":
                RST.append(nodo*3-3)
                RST.append(nodo*3-2)
                RST.append(nodo*3-1)
                
            elif tipo_rst == "Articulado":
                RST.append(nodo*3-3)
                RST.append(nodo*3-2)

            elif tipo_rst == "Simple":
                RST.append(nodo*3-2)

        RST = np.asarray(RST)
        return RST
    
    """CALCULA LOS GRADOS NO RESTRINGIDOS O GRADOS LIBRES"""
    def grados_libres(self):
        con = 0
        g_Nodos = self.gdlN # Grados de libertad de nodos
        rst = self.rst # restricciones
        #print("N ",g_Nodos, "lon ", len(g_Nodos))
        nodos_libres = {}

        for i in range(len(g_Nodos)):
            nodo = i + 1
            #print("nodo ",nodo)
            for j in range(3):
                grado = g_Nodos[nodo][j]
                #print(grado)
                if grado not in rst: 
                    con += 1
                    if con == 1:
                        nodos_libres[nodo] = [grado]
                        # print("Nodos L ", nodos_libres)
                    else:
                        nodos_libres[nodo].append(g_Nodos[nodo][j])
        
            con = 0

        return nodos_libres
                    
    """CALCULA LA MATRIZ DE RIGIDEZ SIN RESTRINCIONES, CON GRADOS LIBRES """  
    def Matriz_grados_libre(self):
        Matriz_GL = self.KG
        #print(self.rst)
        Matriz_GL = np.delete(Matriz_GL, self.rst, axis = 0)
        Matriz_GL = np.delete(Matriz_GL, self.rst, axis = 1)
        #print(Matriz_GL.shape)
        
        return Matriz_GL
     
    """ CALCULA LA INVERSA DE MATRIZ DE GRADOS LIBRES """
    def inversa_MGL(self):
        inversa = np.linalg.inv(self.MGL)
        return inversa
    
    """CALCULA VECTOR DE FUERZA EN LOS NODOS Y EN CADA NODO """
    def vector_fuerza(self):
    
        F = []
        
        #print("N ",len(self.gl))
        #print("Grados libres ",(self.gl))
        for i in self.gl:
            nodo = i
            
            if nodo in self.dicf:
                fuerza = self.dicf[nodo]
                #print("fuerza: ", fuerza)
                if len(self.gl[i]) == 1: # Apoyo articula libre el giro
                    #print("nodo: ", nodo)
                    F.append([fuerza[2]])
                    #print("F: ", F)
                elif len(self.gl[i]) == 2: # Apoyo simple
                    for j in [0, 2]: # Pasa fuerza en x y el M que esta aplicado
                        #print("nodo: ", nodo)
                        F.append([fuerza[j]])
                        #print("F: ", F)
                
                else:
                    for j in range(len(self.gl[i])): #Apoyo libre
                        F.append([fuerza[j]])
            else:
                for i in range(len(self.gl[i])):
                    F.append([0])
        F = np.asarray(F)
        # print("F: ", F)
        
        return F
    
    
    """==Vector fuerza para cada elemento en fun de las fuerzas en los nodos==#
    """
    def fuerzas_ex_elem(self) :
        """
        [Fxi
         Fyi
         Mi
         FXf
         Fyf
         Mf] """
        
        F_E = []
        
        for i in range(len(self.tbl_Elem)):
            F = [] # Guardado parcial de fuerzas de nodos
            
            Ni = self.tbl_Elem[i][1]
            Nf = self.tbl_Elem[i][2]
            
            #-----------Fuerzas puntuales nodo inicial----------#
            if Ni in self.dicf: # Si el nodo tiene fuerzas las agrega a list F
                
                for i in range(3):
          
                    F.append([self.dicf[Ni][i]]) 
            else:
                for i in range(3):
                    F.append([0])
                
                    
            #-----------Fuerzas puntuales nodo final----------#
            if Nf in self.dicf:
                for i in range(3):
          
                    F.append([self.dicf[Nf][i]]) 
            else:
                for i in range(3):
                    F.append([0])
                    
                    
            F =  np.asarray(F)
            F_E.append(F) # Se agreega als fuerzas en el elemento
        
        F_E = np.asarray(F_E)
        
        return F_E
            
    """COLOCA LOS DESPLAZAMIENTO EN LOS GRADOS LIBRES POR NODO """  
    def desplazamientos_GL(self):
        delta_g = [] # Desplazamiento en cada grado
        #print(self.F)
        Desplazamientos = (np.matmul(self.IMGL,self.F) )#(, ))
        
        #print(Desplazamientos)
        #ASIGNANDO A CADA GRADO SU DESPLAZAMIENTO
        # Agrega los grados libres a una lista
        con = 0
        for i in self.gl:
            #print("i: ", self.gl[i])
            for j in range(len(self.gl[i])):
                con += 1
                #print("grado: ", self.gl[i])
                # print("grados: ", self.gl[i][j], "delta : ", Desplazamientos[con-1][0])
                delta_g.append([self.gl[i][j],Desplazamientos[con-1][0]])
        delta_g = np.asarray(delta_g) # desplazamiento de cada nodo
        #print(delta_g)
        #print("delta_g",delta_g )
            
            
        return np.array(Desplazamientos), delta_g
    
    """COLOCA LOS DESPLAZAMIENTO EN TODOS LOS GRADOS POR LOS NODOS """

    def grado_desplazamiento(self):
        
        g_delta = []
        dic_g_delta = {}
        #print("Numero de grados y restricciones ",(self.dimen))
        
        for i in range(self.dimen):
            #print(i)
            grado = i
            #print("grado: ", grado)
            if i in self.rst: # Si el grado esta restringifo-->delta = 0
                g_delta.append([i, 0])
                dic_g_delta[i] = 0
                
            else:
                for j in range(len(self.delta_g)):
                    if self.delta_g[j][0] == grado:
                        dic_g_delta[grado] = self.delta_g[j][1]
                        g_delta.append([grado, self.delta_g[j][1]])

        g_delta = np.asarray(g_delta)  
        #print("#", g_delta)
        
        return g_delta, dic_g_delta
    
    """ORGANIZA LOS DEPLAZAMIENTO EN CADA ELEMENDO POR GRADOS EN SUS NODO """
    def grados_delta_elemento(self):
        dlElemento = []
        g_d_elem = []
        gdElem = []
        d_elem = []
        for n in range(self.nElem):
            Ni = self.tbl_Elem[n][1]
            Nf = self.tbl_Elem[n][2]
            #print("Ni: ", Ni, "Nf: ", Nf )
            for i in range(len(self.g_delta)):  
                # i = 0
                for j in range(3):
                    grado = self.gdlN[Ni]
                    #print("grado ", grado)
                    if grado[j] == i:
                        #print("grado[j] ", grado[j])
                        #grado_actual = self.g_delta[i][0] # Imperimir grado
                        delta_actual= self.g_delta[i][1]
                        #print("grado ", grado_actual, "delta: ", delta_actual)
                        d_elem.append([delta_actual]) # se quito el grado al 
                                                        #que pertenece el desplazamiento
                        g_d_elem.append([grado[j], delta_actual]) # Agrega el grado y desplazamiento                      
                for m in range(3):
            
                    grado = self.gdlN[Nf]
                    #print("grado ", grado)
                    if grado[m] == i:
                        #grado_actual = self.g_delta[i][0]
                        delta_actual= self.g_delta[i][1]
                        d_elem.append([delta_actual])
                        g_d_elem.append([grado[m], delta_actual]) # Agrega el grado y desplazamiento
                        #print("grado ", self.g_delta[i][0], "delta: ", self.g_delta[i][0])
                        
            dlElemento.append(d_elem)
            gdElem.append(g_d_elem)
            d_elem = []
            g_d_elem = []
        dlElemento = np.asarray(dlElemento) 
        gdElem = np.asarray(gdElem) 
        
        return dlElemento, gdElem

    
    """==== Transformacion de desplazamientos del sistema global al local===="""
    """     Con ello se busca calcular las fuerzas internas """
    
    def T_delta_L(self):
        delta_Local = []
        
            
        for i in range(len(self.d_elem)):
            TT = (self.Elementos_creados[i].TT)
            TL = np.matmul(TT, self.d_elem[i])
            delta_Local.append(TL)
            
        delta_Local = np.asarray(delta_Local)
        # print("delta_L:")
        # print(delta_Local)
        
        return delta_Local
            
            
    """ FUERZAS INTERNAS EN CADA ELEMENTO """   
    def fuerzas_internas_elementos(self):
        fuerzas_i = []
        """ Hay que restarle el vector fuerza para que de la resultante real  
        a cada grado*"""
        """ 
        Intertar encontarr fuerzas internas en 
        los elementos multiplicando MGL con lo delta g*
        
        """
        
        for i in range(self.nElem):
            #print("KG: ", self.KG_elem[i].shape)
            #print(self.g_delta_elemento[i][1].shape)
            
            Elemento = self.Elementos_creados[i].Elem # Id elemento
            ang = self.Elementos_creados[i].ang # Angulo del elemento
            
            # Se cheque si el elemento tiene caraga distribuida
            if Elemento in self.dic_vecFW_exe_elem: 
                KL = self.Elementos_creados[i].KL 
                delta_L = self.delta_Local_Elementos[i] # Deplazamientos en los nodos del E en el SL
                
                # Se deben rotar las cargad el sistema L al global
                
                F_ex = np.asarray(self.dic_vecFW_exe_elem[Elemento])
                # print("Elemento: ", Elemento)
                # print(F_ex)
                
                fuerzas_elem = np.dot(KL, delta_L ) - F_ex # Fuerzas internas
                fuerzas_i.append(fuerzas_elem)
            else:
                KL = self.Elementos_creados[i].KL
                delta_L = self.delta_Local_Elementos[i]
                fuerzas_elem = np.dot(KL, delta_L ) #- F_ex # Fuerzas internas
                fuerzas_i.append(fuerzas_elem)
        
        fuerzas_i = np.asarray(fuerzas_i) # Fuerzas internas
        
        return fuerzas_i

    
# Portico_A = Analisis_matricial(tbl_Elem, tbl_Rest, tbl_Nod, dic_tf, diccionarioN ,dic_vecF_ext_Elem)
        
# F:  [[  0.  ]
#  [-30.  ]
#  [-26.67]
#  [  0.  ]
#  [-70.  ]
#  [ 40.  ]]

#[[0], [-30.0], [-26.67], [0], [-70.0], [40.0]]