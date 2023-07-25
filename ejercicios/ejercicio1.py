
#EJERCICIOS PRACTICOS 1

#promedio de duracion
min = 2.5
max = 7 
prom = 4
act = 1.5

print ("----------------------------------------------------------------")
print ("DIFERENCIAS DE DURACION")
#diferencias de duracion
diferencia_con_min = 100 - act / min * 100
print (f'La duracion es de {diferencia_con_min} porciento menos que el mas rapido')

diferencia_con_max = 100 - act / max * 100
print (f'La duracion es de {diferencia_con_max} porciento menos que el mas lento')

# BUENA PRACTICA 
#el // devuelve un entero redondeado hacia abajo, por eso es que conviene multiplicar * 10000 y despues sacarle el numero que le falta
diferencia_con_max = 100 - act * 1000 // max / 10
print (f'La duracion es de {diferencia_con_max} porciento menos que el mas lento')

diferencia_con_prom = 100 - act / prom * 100
print (f'La duracion es de {diferencia_con_prom} porciento menos que el promedio')

print ("----------------------------------------------------------------")
print ("PORCENTAJES DE TIEMPO VACIO")
#duracion de crudos
crudo_prom = 5
crudo_act = 3.5

#calculando el porcentaje de tiempo vacio
tiempo_vacio_promedio = 100 - prom * 1000 // crudo_prom / 10
print (f'El tiempo vacio promedio que se elimina es: {tiempo_vacio_promedio}%')

tiempo_vacio_act = 100 - act * 1000 // crudo_act / 10
print (f'El tiempo vacio actual que se elimina es: {tiempo_vacio_act}%')

print ("----------------------------------------------------------------")
print ("DIFERENCIAS EN CASO DE DURAR 10 HORAS")
#mostrando diferencias si los cursos duran 10 horas
print (f'10 horas de actual equivalen a {prom * 100 // act / 10} horas de otros') #asi le doy dos decimales
print (f'10 horas de otros equivalen a {act * 100 // prom / 10} horas de actual')

