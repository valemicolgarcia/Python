
#ARCHIVOS TXT
print ("  ")
#OPEN
archivo = open ("archivos\\texto1.txt")
#print (archivo)

#si llega a aparecer algun problema al leer lo abro asi:
# archivo = open ("archivos\\texto1.txt", encoding = "UTF-8")

#LEER TODO EL ARCHIVO --> .read()
#print (archivo.read())

#una vez que leo un archivo, para volver a leerlo tengo que antes cerrarlo

#LEER TODAS LAS LINEAS --> se guardan en un arreglo de lineas --> .readlines()
#lineas = archivo.readlines()
#print (lineas)

#LEER UNA SOLA LINEA --> lee solo la primer linea --> .readline()
#linea = archivo.readline()
#print (linea)

#LEER DETERMINADA CANTIDAD DE CARACTERES --> lee la primer linea --> .readline (100)
linea1 = archivo.readline(5)
print (linea1)

#CERRAR EL ARCHIVO --> sino pueden perderse datos o no pueden ser abiertos por otros programas
archivo.close()


