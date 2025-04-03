# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 11:36:32 2022

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


class v_mep:
    def __init__(self, L, wi, wf ):
    
    # print("wi ",wi)
    # print("wf ",wf)
        self.v1 = 0 
        self.v2 = 0
        self.M1 = 0
        self.M2 = 0
        #self.W = 0
        
        self.n_d = 2 # numero de decimales    
        
        # Carga distibuida rectangular
        if wi == wf:
            [self.v1, self.v2, self.M1, self.M2] = self.W_rectangular(L, wi, wf)
            # print("caso 1")
            
        # Carga distibuida triangular decreciente
        elif abs(wf) == 0:
            [self.v1, self.v2, self.M1, self.M2] = self.W_tringular_decreciente(L, wi, wf)
            # print("caso 2")
            
        # Carga distibuida triangular creciente
        elif abs(wi) == 0:
            [self.v1, self.v2, self.M1, self.M2] = self.W_tringular_creciente(L, wi, wf)
            # print("caso 3")
            
        # Carga distibuida trapezoidal decreciente
        elif abs(wi) > abs(wf) and abs(wf)> 0:
            [self.v1, self.v2, self.M1, self.M2] = self.W_trapezoidal_decreciente(L, wi, wf)
            # print("caso 4")
            
        # Carga distibuida trapezoidal creciente
        elif abs(wi) < abs(wf) and abs(wi)> 0:
            [self.v1, self.v2, self.M1, self.M2] = self.W_trapezoidal_creciente(L, wi, wf)
            #print("caso 5")
    
    # Carga distibuida rectangular
    def W_rectangular(self, L, wi, wf):
        W = wi
        v1 = W*L/2
        v2 = v1
        M1 = W*L**2/12
        M2 = -M1
        
        # if wi < 0: 
        #     M1 = M1*-1
            
        return round(v1, self.n_d), round(v2, self.n_d), round(M1, self.n_d), round(M2, self.n_d)
   
    # Carga distibuida triangular decreciente
    def W_tringular_decreciente(self, L, wi, wf):
        W = wi
        v1 = (7/20)*W*L
        v2 = (3/20)*W*L
        M1 = W*L**2/20
        M2 = -W*L**2/30
        
        # if wi < 0:
        #     M1 = M1*-1
            
        return round(v1, self.n_d), round(v2, self.n_d), round(M1, self.n_d), round(M2, self.n_d)
    
    # Carga distibuida triangular creciente
    def W_tringular_creciente(self, L, wi, wf):
        #print("###########3",wi, wf)
        W = wf
        v1 = (3/20)*W*L
        v2 = (7/20)*W*L
        # print("W:", W)
        M1 = W*L**2/30
        M2 = -W*L**2/20
        
        # if wf < 0:
        #     M2 = M2*-1
        #print("M1:{},M2:{}".format(M1,M2))
  
        return round(v1, self.n_d), round(v2, self.n_d), round(M1, self.n_d), round(M2, self.n_d)
        
    # Carga distibuida trapezoidal decreciente        
    def W_trapezoidal_decreciente(self, L, wi, wf):

        w = wi - wf
        v1 = (7/20)*w*L + wf*L/2
        v2 = (3/20)*w*L + wf*L/2
        M1 = -w*L**2/20 - wf*L**2/12
        M2 = w*L**2/30 + wf*L**2/12
        
        if wi < 0:
            M1 = M1*-1
            
        return round(v1, self.n_d), round(v2, self.n_d), round(M1, self.n_d), round(M2, self.n_d)
        
    
    # Carga distibuida trapezoidal creciente
    def W_trapezoidal_creciente(self, L, wi, wf):
    
        w = wf - wi
        v1 = (3/20)*w*L + wi*L/2
        v2 = (7/20)*w*L + wi*L/2
        M1 = -(w*L**2)/30 - (wi*L**2)/12
        M2 = w*L**2/20 + wi*L**2/12

        # if M1<0:
        #     M1 = M1
        if wi < 0:
            M1 = M1*-1
            M2 = M2*-1
        
            
        return round(v1, self.n_d), round(v2, self.n_d), round(M1, self.n_d), round(M2, self.n_d)

