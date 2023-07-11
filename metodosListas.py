
#METODOS DE LISTAS.PY
 
#LIST --> crea una lista
lista = list(["hola","soy","vale",19])
listaSinCadenas = list([10,5,2,15,10,65,100,1, True, False])

print (lista)

#LEN --> cuenta los elementos de una lista
resultado = len(lista)
print (resultado)

#APPEND --> agrega elementos a la lista
lista.append("JAJA")
print (lista)

#INSERT --> agrega elemento a la lista en una posicion determinada
lista.insert (2, "HOLIS")
print (lista)

#EXTEND --> agrego una lista a la lista, y se agregan como elementos individuales
lista.extend (["chau",10])
print (lista)

#POP --> elimina elemento de la lista con su indice
lista.pop (0)
print (lista)

#si pongo como parametro -1 se elimina el ultimo elemento de la lista
lista.pop (-1)
print (lista)
# si pongo -2 se elimina el anteultimo

#REMOVE --> elementa un elemento de la lista por su valor
lista.remove (19)
print (lista)

#SORT --> ordena todos los elementos de forma ascendente 
#solo funciona sin cadenas de texto
listaSinCadenas.sort ()
print (listaSinCadenas)

#SORT CON REVERSE=TRUE--> ordena todos los elementos de forma descendente
#solo funciona sin cadenas de texto
listaSinCadenas.sort (reverse=True)
print (listaSinCadenas)

#REVERSE --> invierte los elementos de una lista
listaRandom = list ([1,2,44,12,3,10])
listaRandom.reverse()
print (listaRandom)

#INDEX --> verifico si un elemento se encuentra o no en la lista
#busca elementos completos, no partes como pasa en las cadenas
pos_elemento_encontrado = listaRandom.index(44)
print (pos_elemento_encontrado)

#EN TUPLAS --> solo puedo usar el index y el count
#EN CONJUNTO --> solo puedo eliminar elementos o remover, no se puede agregar
#de esta forma veo cuales son los metodos que puedo usar para cada cosa
#FUNCION DIR
print (dir(set(["hola","val"])))

#CLEAR --> elimina todos los elementos de la lista
lista.clear ()
print (lista)
