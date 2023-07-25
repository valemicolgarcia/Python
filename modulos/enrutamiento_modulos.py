
#enrutamiento de modulos

#importar modulos en la misma ruta
import funciones_e.saludar as m_saludarr

#print (funciones_e.saludar.saludar ("vale"))
print (m_saludarr.saludar ("Valeeeee"))


#SYS
import sys
print (sys)
print ("---------------------")

print (sys.builtin_module_names) #devuelve una tupla con todos los nombres de los modulos
#no crear modulos con esos nombres porque python le da prioridad a esos no los propios
print ("---------------------")

print (sys.path) #rutas
#la primer ruta que nos devuelve es la ruta actual

#agrego a la ruta actual, la carpeta de la que quiero importar modulos
#copio y pego la ruta actual y le pongo el nombre de la carpeta
#la ruta actual era esta: c:\\Users\\valem\\Documents\\yo\\PYTHON\\modulos y la cambio asi: 
sys.path.append("c:\\Users\\valem\\Documents\\yo\\PYTHON\\funciones_prueba")

print ("  ")
print (sys.path)

#con la ruta modificada ahora si puedo importar
print ("   ")

import saludar #esto va a aparecer subrayado como si fuese un error pero funciona
print (saludar.saludar ("valeee"))

import saludar as modulos_saludos
print (modulos_saludos.saludar ("valemicolgarcia"))

