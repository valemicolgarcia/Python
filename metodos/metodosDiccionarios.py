#METODOS DE DICCIONARIOS

diccionario = {
    "nombre" : 'valeria',
    "apellido": 'garcia',
    "edad" : 19
}

#KEYS --> devuelve las claves (tambien sirve para iterar)
claves = diccionario.keys()
print (claves)

#GET --> devuelve el valor de una clave
#si no encuentra devuelve none, pero no tira error
clave = diccionario.get("nombre")
print (clave)

#POP --> elimina un elemento en particular
diccionario.pop ("nombre")
print (diccionario)

#ITEMS --> para iterar el diccionario y recorrerlo
diccionario_iterable = diccionario.items()
print (diccionario_iterable)

#CLEAR --> elimina todos los elementos
diccionario.clear()
print (diccionario)
