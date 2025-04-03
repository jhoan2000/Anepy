class Cargas(object):
	"""docstring for Cargas"""
	def __init__(self, nombre,fuerza,distancia_i_c,distancia_f_c,lista_cargas):
		self.lista_cargas = lista_cargas #Almacena las cargas
		self.nombre = nombre #Nombre de la carga
		self.fuerza = fuerza #Magnitud
		self.distancia_i_c = distancia_i_c #Distancia Inicial
		self.distancia_f_c = distancia_f_c #Distancia Final
		self.V = 0 #Cortante
		self.M = 0 #Momento

	#Crea carga puntal
	def puntual(self):
		self.p_c = self.fuerza #Magnitud
		self.p_d = self.distancia_i_c 
		self.V = -self.p_c
		self.M = self.p_c * self.p_d
		print("Nombre:", self.nombre,'\n'
			"Carga:",self.p_c,'Kn\n',
			"Distancia:", self.p_d,'m\n'
			"Contante:", self.V,'Kn\n'
			 "Momento:", self.M,'Kn*m\n'
			 )
		self.lista_cargas.append(("p",self.p_c,self.p_d)) #Agrega la carga con su(s) distancia a las lista

	#Crea carga distribuida
	def distribuida(self):
		self.d_c = self.fuerza #Magnitud
		self.d_d_i = self.distancia_i_c #distanci inicial
		self.d_d_f = self.distancia_f_c #distancia final
		self.d_d = self.d_d_f - self.d_d_i
		self.V = -self.d_c * self.d_d
		self.M = (self.d_c * self.d_d**2)/2
		print("Nombre:", self.nombre,'\n'
			"Carga:",self.d_c,'Kn\n',
			"Distancia:", self.d_d,'m\n'
			"Contante:", self.V,'Kn\n'
			 "Momento:", self.M,'Kn*m\n'
			 )
		self.lista_cargas.append(("d",self.d_c,self.d_d_i,self.d_d_f))#Agrega la carga con su(s) distancia a las lista

	#Crea carga par
	def momento(self):
		self.m_c = self.fuerza #Magnitud
		self.m_d = self.distancia_i_c #distancia
		self.V = 0
		self.M = self.m_c
		print("Nombre:", self.nombre,'\n'
			"Carga:",self.m_c,'Kn\n',
			"Distancia:", self.m_d,'m\n'
			"Contante:", self.V,'Kn\n'
			 "Momento:", self.M,'Kn*m\n'
			 )
		self.lista_cargas.append(("m",self.m_c,self.m_d))#Agrega la carga con su(s) distancia a las lista


contador = 0
def crear_carga(tipo, fuerza,d_i,d_f,lista):
	global contador
	contador +=1
	if len(lista) < 5:
	    tipo = str(tipo).lower()
	   
	    carga1 = Cargas(tipo,fuerza,d_i,d_f,lista)
	    
	 
	    
	    if tipo == "p" or tipo == "puntual" :       
	        carga1.puntual()
	        
	    elif tipo == "d" or  tipo ==  "distribuida" :   
	       
	        carga1.distribuida()
	    
	    elif tipo == "m" or tipo ==  "momento" :       
	        carga1.momento()
	    

