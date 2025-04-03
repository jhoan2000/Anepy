import matplotlib.pyplot as plt

class Grafica_V_M():

	def __init__ (self, x, y_M, y_V, luz):
		#print("jjjjjjjjjjjjjjj")
		#Grafica el eje 0
		self.luz = luz
		self.eje_0_x = [0, self.luz]
		self.eje_0_y = [0, 0]

		self.x = x
		self.y_M = y_M
		self.y_V = y_V


		fig = plt.figure(figsize=(5,8),dpi = 80) # maximizar dpi = 80
		fig.tight_layout()
		fig.subplots_adjust(wspace = 0.6, hspace = 0.32,
		top = 0.95, left = 0.15) #Configurar tamaños de grafico interno
		#fig.subplots_adjust(hspace = 0.32)


		self.graficar_momento()
		self.graficar_cortante()

		
		
		plt.show()

	def graficar_cortante(self):
		#plt.plot(self.x, self.y_V, color = "black")# grafica los cortantes
		self.V_cero = self.cortante_cero(self.x, self.y_V)
		print("punto:", self.V_cero)
		#plt.plot(self.V_cero[0], self.V_cero[1], marker="o", color = "red")

		ax = plt.subplot(2,1,1)
		ax.plot(self.eje_0_x, self.eje_0_y, color = "black")
		ax.plot(self.x, self.y_V, color = "red")
		ax.plot(self.V_cero[0],self.V_cero[1],marker="o", color = "green")
		ax.set_title('Grafico de Cortante V')
		ax.set_xlabel("x[m]")
		ax.set_ylabel("V[KN]")
		ax.set_xlim(0, self.luz)


	def cortante_cero(self,x,y):
		self.x = x
		self.y = y
		
		self.max_y_positivo=max(self.y) #Busca el cortante maximo positivo
		self.max_y_negativo=min(self.y) #Busca el cortante maximo negativo
		print("Positivo maximo= ",self.max_y_positivo, "x=",self.x[self.y.index(self.max_y_positivo)])
		print("Negativo maximo= ",self.max_y_negativo)

		
		contador = 0
		indices = []
		#Buca y agrega el indice cuabdo v = 0
		for i in y:
			contador = contador+1
			if round(i,4) == -0 or round(i,4) == 0.0000:
				indices.append(contador-1)
		print("Indices: ",indices)
		self.index_cero_v = 0
		if len(indices) == 3:
			self.index_cero_v = indices[1] #
		
		

			
		self.v_cero = 0

		#print("indice:",self.index_cero_v)
		self.punto_v_cero = [self.x[self.index_max_y], 0]
		
		
		
		return (self.punto_v_cero)

	

	def graficar_momento(self):
		ax = plt.subplot(2,1,2)
		ax.plot(self.eje_0_x, self.eje_0_y, color = "black")
		ax.plot(self.x, self.y_M, color = "blue")# grafica los momentos
		self.M_max = self.momento_max(self.x, self.y_M)
		ax.plot(self.M_max[0], self.M_max[1], 'r-.o')
		ax.set_title('Grafico de Momento M')
		ax.set_xlabel("x[m]")
		ax.set_ylabel("M[KNxm]")
		ax.set_xlim(0, self.luz)
		#plt.plot(self.M_max[2], self.M_max[3], 'b--o')
		

	def momento_max(self,x,y):
		self.x = x
		self.y = y
		self.max_y_positivo=max(self.y) #Busca el momento maximo positivo
		self.max_y_negativo=min(self.y) #Busca el momento maximo negativo
		print("Positivo maximo= ", self.max_y_positivo, "x=",self.x[self.y.index(self.max_y_positivo)])
		print("Negativo maximo= ", self.max_y_negativo)
		if abs(self.max_y_negativo) > self.max_y_positivo:
			self.maximo = self.max_y_negativo
		else:
			self.maximo = self.max_y_positivo


		self.index_max_y = self.y.index(self.maximo) # Busca el indice del momento maximo

		self.linea_y_max_x = [self.x[self.index_max_y], self.x[self.index_max_y]]
		self.linea_y_max_y = [0,self.y[self.index_max_y]]
		# x maximo con y max
		self.linea_x_max_y = [self.y[self.index_max_y], self.y[self.index_max_y]]
		self.linea_x_max_x = [0,self.x[self.index_max_y]]
		return (self.linea_y_max_x, self.linea_y_max_y, self.linea_x_max_x, self.linea_x_max_y)

		



class Calculos(object):
	"""docstring for Calculos"""
	def __init__(self, longitud,cargas,presicion):
		self.cargas = cargas
		self.longitud = longitud
		self.lista = [0]
		self.momentos = []
		self.cortantes = []

		#presicion del grafico
		self.nun_cortes = presicion #numero de subcortes o subdivisiones realizads a la longitud de la viga

		self.subcortes(self.nun_cortes, self.lista)

		self.cortante(self.cargas,self.lista,self.cortantes) #Se llama la funcion para el calculo de V
	

		self.momento(self.cargas, self.lista, self.momentos) #Se llama la funcion para el calculo del moemnto
		
		self.graficar = Grafica_V_M(self.lista, self.momentos, self.cortantes, 
			self.longitud)

	def subcortes(self,numero,lista):
		for x in range(self.nun_cortes): #realiza los cortes a lo largo de toda la luz 
			cortes = self.lista[x]+(self.longitud-0)/self.nun_cortes
			self.lista.append(cortes)


	#-----------CORTANTE------------	
	def  cortante(self,cargas,cortes,cortantes):
		self.cortantex = 0
		contador = 0

		for x in cortes: #Para una distancia x se va aprobar con todas las cargas 
			#print("x",x)'''
			for n in cargas: #pasa las cargas una a una y introduce en la funcion correspondiente
				contador = contador+1
						
				if n[0] == "p":
					self.cortantex = self.cortantex - self.puntual_v(x,n)
				elif n[0] == "Ray" or n[0]=="Rby" :
					self.cortantex = self.cortantex + self.puntual_v(x,n)

				elif n[0] == "m":
					self.cortantex = self.cortantex + self.carga_momento_v(x,n)
				#('d', 10, 0, 6)
				elif n[0] == "d":
					self.cortantex = self.cortantex - self.distribuida_v(x,n,self.longitud)
							
				if contador == len(cargas):
						#print("M=",self.momentox)
					contador=0
					#print("x:",round(x,2)," v= ",round(self.cortantex,3))
					self.cortantes.append(self.cortantex)
					self.cortantex = 0

	def puntual_v(self,x,carga):
		
		self.suma= x - carga[2]
	
		if self.suma<=0:
			if carga[0] == "p":
				self.v_c_p = 0
			else:
				self.v_c_p = 0		
		else:
			self.v_c_p = carga[1]

		if carga[0] == "Rby" and round((carga[2] - x),6) == 0:
			self.v_c_p = carga[1]


		#print("carga=",carga, "x= ",x, "suma= ", self.suma,"v=",self.v_c_p)
		return self.v_c_p
		

		#llamar funcion y pasar por argumrnto x el la distanciaes es negativo es igual a cero y sino si se suma
		
	def carga_momento_v(self,x,carga):
		self.v_c_m = 0
		#print("carga=",carga, "x= ",x, "suma= ", self.suma,"m=",self.m_c_p)		
		return self.v_c_m

	def distribuida_v(self,x,carga,luz):
		self.v_c_d = 0 #cortante carga distribuida
		self.suma = 0

		d_c_c_p = (carga[3]-carga[2])/2
		base = carga[3]-carga[2]
		w = carga[1]


		if carga[2] == 0 and luz == carga[3] or carga[2] == 0 and carga[3] <=luz:
			#print("0############")
			self.v_c_d =  w*x

		elif carga[2] > 0 and luz == carga[3]:
			#print("1############:")
			self.suma= x - carga[2]
		
			if self.suma<=0:
				self.v_c_d = 0 #momento carga distribuida
			else:
				self.v_c_d = + w*(x-carga[2])

		elif carga[2] > 0 and x <= carga[3] and carga[3] < luz:
			#print("2#################:")
			self.suma = x - carga[2]

			if self.suma <=0:

				self.v_c_d = 0
			else:
				self.v_c_d = w*(x-carga[2])
				



		if carga[2] >= 0 and x >= carga[3] and carga[3] < luz:
			#print("	3#############:")
			self.suma= x - carga[3]
		
			if self.suma<=0:
				self.v_c_d = 0 #momento carga distribuida
			else:
				self.v_c_d = w*base

						
		return -self.v_c_d


	#-----------MOMENTO------------	

	def  momento(self,cargas,cortes,momentos):
		self.momentox = 0
		contador = 0

		for x in cortes: #Para una distancia x se va aprobar con todas las cargas 
			#print("x",x)'''
			for n in cargas: #pasa las cargas una a una y introduce en la funcion correspondiente
				contador = contador+1
						
				if n[0] == "p":
					self.momentox = self.momentox - self.puntual_m(x,n)
				elif n[0] == "Ray" or n[0]=="Rby" :
					self.momentox = self.momentox + self.puntual_m(x,n)

				elif n[0] == "m":
					self.momentox = self.momentox + self.carga_momento_m(x,n)
				#('d', 10, 0, 6)
				elif n[0] == "d":
					self.momentox = self.momentox - self.distribuida_m(x,n,self.longitud)
							
				if contador == len(cargas):
						#print("M=",self.momentox)
					contador=0
					#print("x:",round(x,2)," m= ",round(self.momentox,3))
					self.momentos.append(self.momentox)
					self.momentox = 0

	def puntual_m(self,x,carga):
		
		self.suma= x - carga[2]
	
		if self.suma<=0:
			self.m_c_p = 0
		else:
			self.m_c_p = carga[1] * self.suma

		#print("carga=",carga, "x= ",x, "suma= ", self.suma,"m=",self.m_c_p)


		
		return self.m_c_p
		

		#llamar funcion y pasar por argumrnto x el la distanciaes es negativo es igual a cero y sino si se suma
		
	def carga_momento_m(self,x,carga):

		self.suma= x - carga[2]
	
		if self.suma<=0:
			self.m_c_m = 0 #momento carga momento
		else:
			self.m_c_m = -carga[1]

		#print("carga=",carga, "x= ",x, "suma= ", self.suma,"m=",self.m_c_p)		
		return self.m_c_m

	def distribuida_m(self,x,carga,luz):
		self.m_c_d = 0
		self.suma = 0

		d_c_c_p = (carga[3]-carga[2])/2
		base = carga[3]-carga[2]
		w = carga[1]


		if carga[2] == 0 and luz == carga[3] or carga[2] == 0 and carga[3] <=luz:
			#print("0############")
			self.m_c_d = + (w*x**2)/2

		elif carga[2] > 0 and luz == carga[3]:
			#print("1############:")
			self.suma= x - carga[2]
		
			if self.suma<=0:
				self.m_c_d = 0 #momento carga distribuida
			else:
				self.m_c_d = + (w*(self.suma)**2)/2

		elif carga[2] > 0 and x <= carga[3] and carga[3] < luz:
			#print("2#################:")
			self.suma = x - carga[2]

			if self.suma <=0:

				self.m_c_d = 0
			else:
				self.m_c_d = w*(((x-carga[2])**2)/2)
				#               10    *(((A27-2)^2)/2)



		if carga[2] >= 0 and x >= carga[3] and carga[3] < luz:
			#print("	3#############:")
			self.suma= x - carga[3]
		
			if self.suma<=0:
				self.m_c_d = 0 #momento carga distribuida
			else:
				self.m_c_d = (w*base)*(((d_c_c_p))+(x-carga[3]))

				#				10   *          2        *(           1           + (A31-4))

		#print("carga=",carga, "x= ",x, "suma= ", self.suma,"m=",self.m_c_d)		
		return self.m_c_d

#lista=[('d', 20, 0, 8), ('Ray', 80.0, 0), ('Rby', 80.0, 8)]

#prueba =  Calculos(8,lista,500)


	


