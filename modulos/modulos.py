#cualquier archivo.py es un modulo
#desde un modulo puedo llamar a otro

#3 tipos de modulos--------------
#modulos creados por python, escritos en c
#modulos de terceros
#modulos propios
#--------------------------------

#se pueden importar modulos, acceder desde diferentes archivos
#solo se pone el nombre del archivo, no la extension
#el modulo que importamos se comporta como un objeto, con sus propias funciones

#IMPORTAR modulos
import modulo_saludar
saludo = modulo_saludar.saludar("Vale")
print (saludo)

#saludar se comporta como modulo, no como metodo
#la carpeta pycache se crea automaticamente por python

#IMPORTAR modulo y renombrar el modulo con AS
import modulo_saludar as m_saludar 
salu = m_saludar.saludar("Vicky")
print (salu)

#IMPORTAR determinadas funciones con FROM
#puedo renombrar las funciones que importo
from modulo_saludar import saludar, despedir as despedd
salud = saludar ("ValeGarcia")
print (salud)
despe = despedd("amarinda")
print (despe)

#importo TODO con *
#mala practica!!!!
from modulo_saludar import *
print (saludar ("valllll"))

#importar variable y funcion con el mismo nombre, tira errores
# las funciones las creo con mayusculas al inicio
# las variables arranacan con minusculas

#DIR --> propiedades y metodps del namespace 
print (dir(m_saludar))

#.NAME --> te muestra el nombre del modulo que se importo
print (m_saludar.__name__)
print (__name__) #modulo que se esta ejecutando es el main

#importamos desde una carpeta . archivo import nombre_de_funcion
from modulos.modulo_saludar import saludar

