class Apoyos(object):

	"""docstring for Apoyos"""
	def __init__(self, nombre,distancia,lista_apoyos):
		
		self.lista_apoyos = lista_apoyos
		self.nombre = nombre 
		self.tipo = 0
		self.distancia = distancia
		self.V = 0
		self.M = 0
        
    	
		

	def rodillo(self): 
		self.tipo = 1
		self.a_r_d = self.distancia
		
		'''print("Nombre:", self.nombre,'\n'
			"tipo:",self.tipo,'\n'
			"Distancia:", self.a_r_d,'m\n'
			"Reacciones en:",'\n'
		 	"	Y = 1",'\n'
			"	X = 0",'\n'
			"	M = 0",'\n' 
			)'''

		self.lista_apoyos.append((self.tipo,self.a_r_d))
        

	def fijo(self): 
		self.tipo = 2
		self.a_f_d = self.distancia
		
		'''print("Nombre:", self.nombre,'\n'
			"tipo:",self.tipo,'\n'
			"Distancia:", self.a_f_d,'m\n'
			"Reacciones en:",'\n'
		 	"	Y = 1",'\n'
			"	X = 1",'\n'
			"	M = 0",'\n'
			)'''
		self.lista_apoyos.append((self.tipo,self.a_f_d))

	def empotrado(self): 
		self.tipo = 3
		self.a_e_d = self.distancia
		
		'''print("Nombre:", self.nombre,'\n'
			"tipo:",self.tipo,'\n'
			"Distancia:", self.a_e_d,'m\n'
			"Reacciones en:",'\n'
		 	"	Y = 1",'\n'
			"	X = 1",'\n'
			"	M = 1"
			)'''
		self.lista_apoyos.append((self.tipo,self.a_e_d))

def crear_apoyo(tipo, distancia,lista):
	if len(lista) <=1:
	    tipo = str(tipo).lower()
	   
	    apoyo1 = Apoyos(tipo,distancia,lista)
	    
	 	
	    
	    if tipo == "r" or tipo == "rodillo" or tipo == "1":       
	        apoyo1.rodillo()
	        
	    elif tipo == "f" or  tipo ==  "fijo" or tipo == "2":   
	       
	        apoyo1.fijo()
	    
	    elif tipo == "e" or tipo ==  "empotrado" or tipo == "3":       
	        apoyo1.empotrado()




 	