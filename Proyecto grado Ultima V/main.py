from Apoyos import crear_apoyo

from Cargas import crear_carga

from Calculos_reacciones import Operaciones

from Viga import Viga

from Calculo_momento_cortante import Calculos



longitud = []
mi_lista_cargas = []
mi_lista_apoyos = []
super_lista = []
L = 6
viga = Viga('v',6,longitud)
apoyo = crear_apoyo("f", 0, mi_lista_apoyos)
apoyo2 = crear_apoyo("f", 6,mi_lista_apoyos)

carga = crear_carga("d", 25, 0, L,mi_lista_cargas)
#carga = crear_carga("p", 10, 3, 0,mi_lista_cargas)
#carga = crear_carga("p", 10, 4, 0,mi_lista_cargas)
#carga2 = crear_carga("d", 15, 0, 5,mi_lista_cargas)
carga3 = crear_carga("m",-34.68,0,0,mi_lista_cargas)
carga = crear_carga("m",-34.68,L,0,mi_lista_cargas)

ejercicio = Operaciones(longitud[0],mi_lista_cargas,mi_lista_apoyos)

print("lista:",ejercicio.obtener_cargas_ordenadas())



#calculo = Calculos(longitud[0],ejercicio.obtener_cargas_ordenadas(),500)

calculo = Calculos(6, (('d', 25, 0, 6), ('m', -34.68, 0), ('Ray', 75, 0), ('m', -34.68, 6), ('Rby', 75, 6)),500)
