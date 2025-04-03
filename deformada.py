# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 15:37:40 2022

@author: Estudiante
"""


class Deformada:
    def __init__(self, elementos,Desplazamientos_elementos,f_amp ):
        
        self.Desplazamientos = self.nodo_delta(elementos, Desplazamientos_elementos)
        self.dic_deformada =self.coordenadas_desplazadas(elementos, f_amp, self.Desplazamientos)
    
    def nodo_delta(self, elementos,Desplazamientos_elementos ):
        d_agregados = [] # Comprueba los desplazamientos ya agregados
        Desplazamientos = {}
        for i in range(len(elementos)):
            Ni = elementos[i].conex[1]
            Nf = elementos[i].conex[2]
            
            if Ni not in d_agregados:
                #print(Ni)
                # Desplazmiento en el nodo inicial, se obtiene de los desplazamiento por elemento
                dx_i = Desplazamientos_elementos[i][0]
                dy_i = Desplazamientos_elementos[i][1]
                dz_i = Desplazamientos_elementos[i][2]
                Desplazamientos[Ni] = [dx_i, dy_i, dz_i] # Se agregan a un diccionario en f(N)
                
            if Nf not in d_agregados:
            # Desplazmiento en el nodo inicial
                #print(Nf)
                dx_f = Desplazamientos_elementos[i][3]
                dy_f = Desplazamientos_elementos[i][4]
                dz_f = Desplazamientos_elementos[i][5]
                Desplazamientos[Nf] = [dx_f, dy_f, dz_f]

            d_agregados.append(Ni)  
            d_agregados.append(Nf)
            # print(d_agregados)
            # print(Desplazamientos)
        return Desplazamientos
    
    def coordenadas_desplazadas(self,elementos, f_amp, Desplazamientos):
        d_agregados = [] # Comprueba los desplazamientos ya agregados
        tbl_Nod_desplazados = []

        for i in range(len(elementos)):
            Ni = elementos[i].conex[1]
            Nf = elementos[i].conex[2]
            
            cx_i = elementos[i].cxi # Cordenadas del xi de Ni
            cy_i = elementos[i].cyi # Cordenadas del yi de Ni
            cx_f = elementos[i].cxf # Cordenadas del xf de Nf
            cy_f = elementos[i].cyf # Cordenadas del yf de Nf
            
            if Ni not in d_agregados:
                cd_xi = cx_i + Desplazamientos[Ni][0][0] * f_amp
                cd_yi = cy_i + Desplazamientos[Ni][1][0] * f_amp
                tbl_Nod_desplazados.append([Ni, cd_xi, cd_yi])
            #cd_zi = cx_i + Desplazamientos[Ni][0] * amp # Pendiente grafico del giro
            if Nf not in d_agregados:
                cd_xf = cx_f + Desplazamientos[Nf][0][0] * f_amp
                cd_yf = cy_f + Desplazamientos[Nf][1][0] * f_amp
                #cd_zi = cz_i + Desplazamientos[Nf][0] * amp
                tbl_Nod_desplazados.append([Nf, cd_xf, cd_yf])
            
            
            d_agregados.append(Ni)
            d_agregados.append(Nf)
            
        diccionarioN_desplazados = {}

        for i in range(len(tbl_Nod_desplazados)):
            Nod = tbl_Nod_desplazados[i][0]
            cx = tbl_Nod_desplazados[i][1]
            cy = tbl_Nod_desplazados[i][2]
            diccionarioN_desplazados[Nod] = [cx, cy]
        
        return diccionarioN_desplazados
        
    
    