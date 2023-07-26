#un paquete es una carpeta con muchos archivos python
#para que sea un paquete tiene que tener el archivo llamado __init__.py
print ("   ")

import paquete #nombre de la carpeta
print (type(paquete)) #es un modulo
print (paquete.__path__) #ruta, si no es paquete no me lo tira
print ("   ")
import paquete.saludar1
print (paquete.saludar1.saludar("mari"))

#puede haber subpaquetes, carpetas dentro del paquete que tengan el archivo __init__.py
#se importan asi: import paquete.subpaquete

