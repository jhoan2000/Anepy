# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 23:09:10 2022

@author: Estudiante
"""

from math import cos, sin, radians, sqrt, pi, atan
import numpy as np
from cortante_MEP import v_mep


class Vector_fuerzas_externas:
    
    def __init__(self, *Datos, **kwargs):
        
        elementos, [tbl_Elem, tbl_Nod, tbl_Fuer,tbl_Rest, tbl_Fuer_W, nElem], diccionarioN, diccionarioE = Datos # Obtiene nados de Fn_ExtraerDatosTablas
        
        self.dic_tf_auxi = self.diccionario_Fuer(tbl_Fuer) # Diccionario de fuerzas parciales,esto quiere decir: sin las distribuidas
        
        self.dic_vecF_ext_Elem = self.vec_f_ext_Elem(elementos, tbl_Fuer_W) # Discionario de vector de fuerzas distribuidas por elementos ( Cortantes y Momentos de empotramiento perfecto en los apoyos)
        self.dic_fuerzas_T_G, self.vec2 = self.transformacion_vec_f_ext(elementos, tbl_Fuer_W, self.dic_vecF_ext_Elem)
        self.dic_tf_auxi_comple = self.suma_fuerzas_en_nodos(tbl_Fuer, tbl_Fuer_W, self.dic_tf_auxi, diccionarioE, self.dic_fuerzas_T_G) # Diccionario de fuerzas. Incluye fuerzas en los nodos y las fuerzas provocada por las cargas distribuida en los nodos
        self.tbl_Fuer, self.dic_tf = self.reconstruccion_tbl_Fuer(self.dic_tf_auxi_comple)
        
        
    def __str__(self):
        
        print("Dic vec ext")
        print(self.dic_vecF_ext_Elem)
        print("Dic transformacion Sis Global")
        print(self.dic_fuerzas_T_G)
        print("Tabla de fuerzas")
        print(self.tbl_Fuer)
        print("Dic Fuerzas")
        print(self.dic_tf)
        
        return ""
    
    def diccionario_Fuer(self,tbl_Fuer):
        dic_tf_auxi = {}

        for i in range(len(tbl_Fuer)):
            Nod = tbl_Fuer[i] #Escoge el nodo en funcion de la cantidad de tbl_Fuer
            #print(Nod[0])
            fx = Nod[1] # Escoge Fx 
            fy = Nod[2] # Escoge Fy 
            Mz = Nod[3] # Escoge Mz 
            dic_tf_auxi[Nod[0]] = [Nod[0],fx, fy, Mz]
        return dic_tf_auxi
   
    def vec_f_ext_Elem(self, elementos, tbl_Fuer_W ):
        

        dic_vecF_ext_Elem = {}
        for i in range(len(tbl_Fuer_W)):
            f_ext_Elem = []
            Elem = tbl_Fuer_W[i][0]
            ang = elementos[int(Elem)-1].ang
            L = elementos[int(Elem)-1].L
            
            # Fuerzas V y M para elementos incilnados
            if ang > 0 and ang != 90:
                wi = tbl_Fuer_W[i][1] * cos(radians(ang))
                wf = tbl_Fuer_W[i][2] * cos(radians(ang))
            else:
                wi = tbl_Fuer_W[i][1] 
                wf = tbl_Fuer_W[i][2]
    
                    
            # Cargas laterales Distribuidas
            """Se pasa la carga al sistema local del elemento
            aunque la direccion de la fuerza vaya -->+
            en el elemento es -->negativa"""
            
            if abs(ang) == 90 and wi>0 or wf>0:
                # print("here")
                wi = wi *-1
                wf = wf *-1
            
            V_MEP = v_mep(L, wi, wf)
            V1 = V_MEP.v1
            V2 = V_MEP.v2
            M1 = V_MEP.M1
            M2 = V_MEP.M2 
            # print(Elem, wi, wf)
            # print("v",V1, V2, M1,M2)
                
            """ Fuerza horizondal debido a carga distribuida"""
            f_H1 = 0 # Fuerza Horizontal
            f_H2 = 0 # Fuerza Horizontal
            
            if ang > 0 and ang != 90:
                
                w_Hi = tbl_Fuer_W[i][1] * sin(radians(ang)) # W horizon Inicial
                
                w_Hf = w_Hi

                f_H1 = (w_Hi * L)/2 # Fuerza H nodo inicial
                f_H2 = (w_Hf * L)/2 # Fuerza H nodo final
                
            f_ext_Elem.append([f_H1])
            f_ext_Elem.append([V1])
            f_ext_Elem.append([M1])
            f_ext_Elem.append([f_H2])
            f_ext_Elem.append([V2])
            f_ext_Elem.append([M2])
            # print("E", Elem)
            # print(f_ext_Elem)
            
            dic_vecF_ext_Elem[Elem] = f_ext_Elem
        return dic_vecF_ext_Elem   
    
    def transformacion_vec_f_ext(self, elementos, tbl_Fuer_W, dic_vecF_ext_Elem ):
        vec2_E = [] # Almacena los vectores transformados
        vec_E = 0 # vector de fuerzas externas sin transformar
        dic_fuerzas_T_G = {}
        for n in range(len(tbl_Fuer_W)):
            fuerzas_T_G = []# Trasformada global
            Elem = tbl_Fuer_W[n][0]
            vec_E = np.array(dic_vecF_ext_Elem[Elem]) # Vector externo
            
            T = elementos[int(Elem)-1].T
            vec_F_elem = np.dot(T, vec_E )
            vec2_E.append(vec_E)
            
            f_H1, V1, M1,f_H2, V2, M2 = vec_F_elem
            fuerzas_T_G.append(f_H1[0])
            fuerzas_T_G.append(V1[0])
            fuerzas_T_G.append(M1[0])
            fuerzas_T_G.append(f_H2[0])
            fuerzas_T_G.append(V2[0])
            fuerzas_T_G.append(M2[0])
            dic_fuerzas_T_G[Elem] = fuerzas_T_G
        return dic_fuerzas_T_G, vec2_E
   
    def suma_fuerzas_en_nodos(self,tbl_Fuer, tbl_Fuer_W, dic_tf_auxi, diccionarioE, dic_fuerzas_T_G ):  
        
        nodos = [] # Guarda nodos existente en tabla Fuerzas para verificacion en diccionario auxi
        
        for n in range(len(tbl_Fuer)):
            nodos.append(tbl_Fuer[n][0])
            
        #=======Adiccionar reacciones produccidas por carags en elementos en los 
        
        for i in range(len(tbl_Fuer_W)):
        
        
            Elem = tbl_Fuer_W[i][0]
            Ni = diccionarioE[Elem][0]
            Nf = diccionarioE[Elem][1]
            
            # print("Elemento: ", Elem)
            # print("Ni: ", Ni)
            # print("Nf: ", Nf)
            # print("Fuerzas en el SG: ",dic_fuerzas_T_G[Elem])
            
            
            #Se busca el nodo y se le adicciona las fuerzas causadas por las cargas
        
            #print("hi")
            # Como el nodo no existe se agrega al diccionario auxiliar y posteriormente
            # Se agrega a la tbl_Fuer
            # Nudos---> V cortante y los MPE Momentos de Empotremiento Perfecto
            
            if Ni not in nodos:
                dic_tf_auxi[Ni] = [Ni, dic_fuerzas_T_G[Elem][0], dic_fuerzas_T_G[Elem][1], dic_fuerzas_T_G[Elem][2]]
                nodos.append(Ni)
            else:
                # Fuerzas en Nodo inicial del elemento
                dic_tf_auxi[Ni][1] = dic_tf_auxi[Ni][1] + dic_fuerzas_T_G[Elem][0] # Fx
                dic_tf_auxi[Ni][2] = dic_tf_auxi[Ni][2] + dic_fuerzas_T_G[Elem][1] # Cortante
                dic_tf_auxi[Ni][3] = dic_tf_auxi[Ni][3] + dic_fuerzas_T_G[Elem][2] # Momento
                
            if Nf not in nodos:
                #print("Nodo: ",Nf)
                dic_tf_auxi[Nf] = [Nf, dic_fuerzas_T_G[Elem][3], dic_fuerzas_T_G[Elem][4], dic_fuerzas_T_G[Elem][5]]
                nodos.append(Nf)
            else:
                # Fuerzas en Nodo final del elemento
                dic_tf_auxi[Nf][1] = dic_tf_auxi[Nf][1] + dic_fuerzas_T_G[Elem][3] # Fx
                dic_tf_auxi[Nf][2] = dic_tf_auxi[Nf][2] + dic_fuerzas_T_G[Elem][4] # Cortante
                dic_tf_auxi[Nf][3] = dic_tf_auxi[Nf][3] + dic_fuerzas_T_G[Elem][5] # Momento
                
        return dic_tf_auxi
    
    def reconstruccion_tbl_Fuer(self,dic_tf_auxi_comple ):
        # Reconstruccion de tbl_F
        tbl_Fuer = []

        for i in dic_tf_auxi_comple:
            
            tbl_Fuer.append(dic_tf_auxi_comple[i])
            
        dic_tf = {}
        for i in range(len(tbl_Fuer)):
            Nod = tbl_Fuer[i] #Escoge el nodo en funcion de la cantidad de tbl_Fuer
            #print(Nod[0])
            fx = Nod[1] # Escoge Fx 
            fy = Nod[2] # Escoge Fy 
            Mz = Nod[3] # Escoge Mz 
            dic_tf[Nod[0]] = [fx, fy, Mz]
        return tbl_Fuer, dic_tf