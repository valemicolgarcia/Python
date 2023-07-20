#diccionarios

#FUNCION DICT
#es la unica forma de crear diccionarios vacios
diccionario = dict (nombre = "vale", apellido = "garcia")
print (diccionario)

#las listas no pueden ser claves
#diccionario = {["vale","garcia"]: "jajajaja"} #con lista da error
#print (diccionario)

diccionario = {("vale","garcia"): "jajajaja"} #con tupla se puede
print (diccionario)

diccionario = {frozenset(["hola","chau"]): "jaja"} #con conjunto uso frozenset
print (diccionario)

#FUNCION FROMKEYS --> crea el diccionario con valores sin asignar, none
diccionario2 = dict.fromkeys("nombre","chau")
print (diccionario2)
#el primer dato es un iterable

#o

diccionario = dict.fromkeys(["nombre","apellido"])
print (diccionario)

#le agrego valor
diccionario = dict.fromkeys(["nombre","apellido"], "no se")
print (diccionario)





