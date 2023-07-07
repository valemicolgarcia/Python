
#DATOS COMPUESTOS

#LISTA---------------------------------------------------------
lista = ["hola", True, 1.85] #pos del 0 al ultimo
print(lista)
print (lista [0]) 
lista[0] = "holaaaaa"
print (lista [0]) 

#TUPLAS--------------------------------------------------------
tupla = ("vale", False, 19) #igual que la lista pero no se puede modificar
print (tupla[0])

#SET-----------------------------------------------------------
#puedo redefinirlos pero no modificarlo
#no podemos acceder por el indice a un elemento del conjunto
#no muestra valores repetidos
#para acceder a cada uno de los datos hay que usar un bucle
#datos desordenados

conjunto = {"hola", 1.2, True}
conjunto = {"chau", 1.2, True}
print(conjunto)

#DICCIONARIO-----------------------------------------------------
diccionario = {
    'nombre' : "valeria",
    'apellido' : "garcia",
    'altura' : 1.65
}
# 'nombre' --> clave - key
# "valeria" --> valor
#separo con comas

#accedo por el nombre asociado
print (diccionario ['altura'])
