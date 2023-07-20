
#CONJUNTOS

#FUNCION SET
conjunto = set (["dato1", "dato2"])
print (conjunto)
#conjuntos 

#creando un conjunto
conjunto = set (["dato1", "dato2"])
print (conjunto)
#para poner conjuntos dentro de otros conjuntos

#ESTO ESTA MAL
#conjunto1 = {conjunto,"dato3"}
#print (conjunto1)

#FUNCION FROZENSET --> crea conjunto inmutable
conjunto = frozenset (["dato1","dato2"])
conjunto2 = {conjunto, "dato3"}
print (conjunto2)

#TEORIA DE CONJUNTOS
conjunto1 = {1,3,4,5}
conjunto2 = {1,3,5}

#FUNCION ISSUBSET --> verifica si es un subconjunto
resultado = conjunto2.issubset(conjunto1)
print (resultado)

#  <=  --> verifica si es un subconjunto
resultado2 = conjunto2 <= conjunto1
print (resultado2)

#FUNCION ISSUPERSET --> verifica si es un superconjunto
resultado = conjunto2.issuperset(conjunto1)
print (resultado)

#  >  --> verifica si es un superconjunto
resultado2 = conjunto2 > conjunto1
print (resultado2)

#FUNCION ISDISJOINT --> verifico si hay algun numero en comun
#devuelve true, solo cuando todos los elementos son diferentes entre si
resultado = conjunto2.isdisjoint(conjunto2)
print (resultado)

#
