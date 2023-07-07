
#METODOS DE CADENAS

cadena1 = "Hola soy Vale"
cadena = "Tengo 19 años"

#DIR --> funcion
print(dir(cadena1)) #devuelve todos los atributos del objeto
print (dir (4)) #tiene otros atributos != al de los textos

print ()

#metodos --> funciones especificas de objetos

#UPPER y LOWER --> metodos , convierten a mayusculas o minusculas
resultado = cadena1.upper ()
print (resultado)
resultado2 = cadena1.lower ()
print (resultado2)

#CAPITALIZE --> convierte solo la primer letra a mayuscula y resto minuscula
primLetra = cadena1.capitalize()
print (primLetra)

#FIND --> busco cadena en otra cadena, devuelve -1 si no encuentra
busq = cadena1.find("soy")
print (busq) #devuelve la posicion 5

#INDEX --> busco cadena en otra cadena, devuelve error si no encuentra
busq2 = cadena1.index("V")
print (busq2)

#ISNUMERIC --> si es numerico devuelve true, sino false
es_numeric = cadena1.isnumeric()
print(es_numeric) #devuelve false
texto = "123456789"
es_numeric2 = texto.isnumeric()
print (es_numeric2) #devuelve true, identifica num no importa si es string


