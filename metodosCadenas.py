
#METODOS DE CADENAS

cadena1 = "Hola,soy,Vale"
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

#ISNUMERIC --> si es alfanumerico devuelve true, sino false
#solo son validos los caracteres de la a a la z, no cuentan los carc especiales
es_alfanumerico = cadena1.isalpha()
print(es_alfanumerico)

#COUNT --> busca cadena en otra cadena y cuenta las coincidencias
contar_coincidencias = cadena1.count("a")
print (contar_coincidencias)

#LEN --> cuenta la cantidad de caracteres que tiene una cadena --> FUNCION, NO METODO
cant_caracteres = len (cadena)
print (cant_caracteres)

#ENDSWITH --> verificar si una cadena empieza con otra cadena dada
empieza_con = cadena1.startswith("H")
print (empieza_con)

#ENDWITH --> verificar si una cadena termina con otra cadena dada
termina_con = cadena1.endswith ("e")
print (termina_con)

#REPLACE --> reemplaza un pedazo de la cadena dada, por otra cadena
cadena_nueva = cadena1.replace ("la", "lu")
print (cadena_nueva)
cad_nue = cadena_nueva.capitalize () 
print (cad_nue)

#SPLIT --> separa las cadenas con las cadenas que le pasemos
cadena_separada = cadena1.split (",") #cada vez que hay una coma te separa la cadena
print (cadena_separada)
#crea una lista en la que ve todo lo que le pasamos y lo agrega
print (type (cadena_separada))
print (cadena_separada [0])

#