# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 11:32:39 2022

@author: Estudiante
"""
from math import cos, sin, radians, sqrt, pi, atan
import numpy as np

class Propiedades_elemento():
    def __init__(self,elemento, base, altura, moduloElastico, coordenada_xi, coordenada_yi, coordenada_xf, coordenada_yf, conexion):
        
        self.Elem = elemento
        self.b = base
        self.h = altura
        self.E = moduloElastico
        self.cxi = coordenada_xi
        self.cyi = coordenada_yi
        self.cxf = coordenada_xf
        self.cyf = coordenada_yf
        self.conex = conexion
        # Propiedades del elemento
        self.A = self.Area()
        self.I = self.Inercia()
        self.L = self.Longitud()
        self.KL = self.K_local()
        self.ang = self.Angulo()
        self.l = self.coseno()
        self.m = self.seno()
        self.T = self.Transformacion()
        self.TT = self.Traspuesta_T() # Traspuesta de la matriz de Trans
        self.KG = self.K_global()
        self.gdl = self.GDL()

    def __str__(self):

        print("Base: ", self.b)
        print("Altura: ", self.h)
        print("Modulo de Elasticidad: ", self.E)
        print("Coordenadas iniciales: ({},{})".format(self.cxi, self.cyi))
        print("Coordenadas finales: ({},{})".format(self.cxf, self.cyf))
        print("Conectado en: ", self.conex)
        print("Area: ", self.A)
        print("Inercia: ", self.I)
        print("Longitud: ", self.L)
        print("Matriz de rigides Local: ", self.KL)
        print("")
        print("Angulo: ", self.ang)
        print("Coseno: ", self.l)
        print("Seno: ", self.m)
        print("Matriz de transformacion: ", self.T)
        print("")
        print("Matriz de rigidez global: ", self.KG)
        print("")
        print("Grados de libertad: ", self.gdl)

        return ""
    # Propiedades del elemento

    def Area(self):
        return self.b * self.h

    def Inercia(self):
        return (self.b * self.h**3) / 12

    def Longitud(self):
        return sqrt((self.cxf - self.cxi)**2 + (self.cyf - self.cyi)**2)

    def K_local(self):
        k_local = None
        
        EAL = self.E * self.A / self.L
        EI12 = 12 * self.E * self.I / self.L**3
        EI6 = 6 * self.E * self.I / self.L**2
        EI4 = 4 * self.E * self.I / self.L
        EI2 = 2 * self.E * self.I / self.L
        k_local = np.array([
            [EAL, 0, 0, -EAL, 0, 0],
            [0, EI12, EI6, 0, -EI12, EI6],
            [0, EI6, EI4, 0, -EI6, EI2],
            [-EAL, 0, 0, EAL, 0, 0],
            [0, -EI12, -EI6, 0, EI12, -EI6],
            [0, EI6, EI2, 0, -EI6, EI4]
        ])
      
        return k_local

    def Angulo(self):

        b = (self.cxf - self.cxi)
        h = (self.cyf - self.cyi)
        try:
            angulo = atan(h/b)*180/pi
        except ZeroDivisionError:
            # angulo = 90
            
            if self.cyi > self.cyf:
                angulo = -90 # Indica que si se traza el sistema de coordenadas en el Ni el elemento se desarrolla hacia abajo del eje x por ende genera un angulo de -90
            else: 
                angulo = 90

        return angulo

    def seno(self):
        return sin(radians(self.ang))

    def coseno(self):
        return cos(radians(self.ang))

    def Transformacion(self):
        t = np.array([
            [self.l, -self.m, 0, 0, 0, 0],
            [self.m, self.l, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, self.l, -self.m, 0],
            [0, 0, 0, self.m, self.l, 0],
            [0, 0, 0, 0, 0, 1],
        ])
        return t
    def Traspuesta_T(self):
        TT = np.transpose(self.T)
        return TT

    def K_global(self):
        
        Tk = (np.matmul(self.T, self.KL))
        return np.matmul(Tk, self.TT)
        

    def GDL(self):
        gdl = []
        # print(conexion[2])

        de_nudo = self.conex[1]  # (x = nudo, y = el nudo donde sale)
        a_nudo = self.conex[2]  # (x = nudo, y = el nudo donde llega)
        # print(a_nudo)
        gdl.append([de_nudo * 3 - 3, de_nudo * 3 - 2, de_nudo * 3 - 1,
                    a_nudo * 3 - 3, a_nudo * 3 - 2, a_nudo * 3 - 1])  # Grados de libertad
        gdl = np.asarray(gdl)
        # print(gdl)
        return gdl

