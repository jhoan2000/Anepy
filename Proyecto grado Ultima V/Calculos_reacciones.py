class Operaciones():
	def __init__ (self,longitud_de_viga,lista_cargas,d_reacciones):
		

		#longitud_de_viga = 10.0
		distancia_apoyo_A = d_reacciones[0][1]
		distancia_apoyo_B = d_reacciones[1][1]
		#distancia_apoyo_A = d_reacciones[0]	#Prueba
		#distancia_apoyo_B = d_reacciones[1]	#prueba

		distancia_A_B = distancia_apoyo_B - distancia_apoyo_A
	

		lista_distancias = []
		
		ordenados = []
		lista_v = []
		lista_d = []

		self.reacciones(lista_cargas,distancia_apoyo_A,distancia_apoyo_B,longitud_de_viga)
		self.ordena_cargas(lista_cargas)

		
		'''
		self.indices_V_max(self.obtiene_Vmax(lista_v),lista_v)

		lista_V_max_x = [lista_d[self.indices_V_max(self.obtiene_Vmax(lista_v),lista_v)[0]],lista_d[self.indices_V_max(self.obtiene_Vmax(lista_v),lista_v)[1]]]
		lista_V_max_y = [lista_v[self.indices_V_max(self.obtiene_Vmax(lista_v),lista_v)[0]],lista_v[self.indices_V_max(self.obtiene_Vmax(lista_v),lista_v)[1]]]

		Grafica_V(longitud_de_viga,lista_d,lista_v,lista_V_max_x,lista_V_max_y)'''


	def dist_puntual(self,distancia_i_c,distancia_A,distancia_B):
		#-----Distancia a desde la carga a A
		if distancia_i_c < distancia_A:
			distancia_c_A = -(distancia_A - distancia_i_c)
		elif distancia_i_c > distancia_A:
			distancia_c_A =  distancia_i_c - distancia_A
		else:
			distancia_c_A = 0

		#-----Distancia a desde la carga a B
		if distancia_i_c < distancia_B:
			distancia_c_B =   distancia_B - distancia_i_c
		elif distancia_i_c > distancia_A:
			distancia_c_B = -(distancia_i_c - distancia_B)
		else:
			distancia_c_B = 0

		#print("distancia A: ", distancia_c_A, "distancia B: ", distancia_c_B)
		return distancia_c_A,distancia_c_B

	def dist_rectangular(self,distancia_i_c,distancia_f_carga,distancia_A,distancia_B,longitud_de_viga):
		d_c_p = (distancia_f_carga-distancia_i_c)/2
		d_c_p_i = d_c_p + distancia_i_c
		d_c_p_f = longitud_de_viga - d_c_p 
		base = d_c_p * 2
		distancia_c_A = 0
		distancia_c_B = 0


		if distancia_i_c < distancia_A and distancia_A < distancia_f_carga and d_c_p_i > distancia_A:

			distancia_c_A = d_c_p - distancia_A

		elif distancia_i_c <  distancia_A and distancia_A < distancia_f_carga and d_c_p_i < distancia_A :

			distancia_c_A =  distancia_A - d_c_p 
		
		elif distancia_i_c == distancia_A or distancia_i_c > distancia_A:

			distancia_c_A = distancia_i_c - distancia_A + d_c_p
	



		#-----Distancia a desde la carga a B
		if distancia_f_carga == distancia_B :

			distancia_c_B = distancia_f_carga - d_c_p_i
			print("1:",distancia_c_B)

		elif distancia_i_c < distancia_B and distancia_f_carga < distancia_B:

			distancia_c_B = distancia_B - distancia_f_carga + d_c_p
			print("2:",distancia_c_B)

		'''elif distancia_i_c > distancia_B :

			distancia_c_B = distancia_c_p - (distancia_f_carga - distancia_B)

		else:'''

		if distancia_f_carga > distancia_B and d_c_p < distancia_B:

			distancia_c_B = distancia_B - distancia_i_c - d_c_p
			print("3:",distancia_c_B)

		elif distancia_f_carga > distancia_B and d_c_p > distancia_B:

			distancia_c_B = distancia_f_carga - distancia_B - d_c_p
			print("4:",distancia_c_B)
	

		print("distancia A: ", distancia_c_A, "distancia B: ", distancia_c_B)


		return distancia_c_A,distancia_c_B,base

	def reaccion_A (self,distancia,carga):
		#calcula la reaccion generada por cada carga de forma individual
		#print("here",distancia)
		#print("here",carga)

		reaccion = (carga*distancia)
		#print("here",reaccion)
		#print("##################",)
		return reaccion

	def reaccion_B (self,distancia,carga):
		#calcula la reaccion generada por cada carga de forma individual
		reaccion = (carga*distancia)
		return reaccion

	def reacciones(self,lista_cargas,distancia_A,distancia_B,longitud_de_viga):   

		#print(lista_cargas)
		self.Ray = 0 
		self.Rby = 0 
		distancia_apoyo_A = distancia_A
		distancia_apoyo_B = distancia_B
		distancia_A_B = distancia_B - distancia_A
		
		
		datos = 0 #Si el indice que toma x es igual a el numero de cargas calcula la reaccion
		#ingresa las cargas y las distancias a las funciones reacciones A y B una a una
		for x in lista_cargas:

			datos = datos +1 #Contador de datos

			# si la carga es puntual llama a las funciones distncia puntual y reaccion a y raccion b que produce

			if str(x[0]).lower() == "p" or str(x[0]).lower() == "puntual": 
				distancias = self.dist_puntual(x[2],distancia_A,distancia_B)
				distanciaB = distancias[1]
				distanciaA = distancias[0]

				self.Ray= self.Ray + self.reaccion_A(distanciaB,x[1])

				self.Rby = self.Rby + self.reaccion_B(distanciaA,x[1])

			if str(x[0]).lower() == "d" or str(x[0]).lower() == "distribuida": 
				
				distancia_r = self.dist_rectangular(x[2],x[3],distancia_A,distancia_B,longitud_de_viga)
				distancia_r_A = distancia_r[0]
				distancia_r_B = distancia_r[1]
				
				
				base = distancia_r[2]
				print("Basee", base)
				carga = base * x[1] 
				
				self.Ray = self.Ray + self.reaccion_A(distancia_r_B,carga)
				self.Rby = self.Rby + self.reaccion_B(distancia_r_A,carga)
				print(self.Ray)

			if str(x[0]).lower() == "m" or str(x[0]).lower() == "momento": 
				
				self.Ray = self.Ray + x[1]
				self.Rby = self.Rby - x[1]	

			#Calculo de reacciones finales
			if datos ==  len(lista_cargas) :
				self.Ray = self.Ray / distancia_A_B
				lista_cargas.append(("Ray",self.Ray,distancia_apoyo_A))
				print("Reaccion Ray: ", self.Ray)

				self.Rby = self.Rby / distancia_A_B
				lista_cargas.append(("Rby",self.Rby,distancia_apoyo_B))
				print("Reaccion Rby: ", self.Rby)
				
				datos = 10


	def ordena_cargas(self,lista_cargas):
		#esta funcion ordena las carga dependiendo su distancia utilizando el metodo sorted
		global ordenados
		ordenados = sorted(lista_cargas, key= lambda lista_cargas: lista_cargas[2])
		#print("Ordenadas: ",ordenados)
		return ordenados

	def obtener_cargas_ordenadas(self):
		global ordenados
		self.lista_final = ordenados
		#print("Here",self.lista_final)
		return self.lista_final

#lista = [("d", 10, 6, 8,)]
#Operaciones(8,lista,(0,6))