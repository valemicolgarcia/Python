import re
texto = '''Hola como estas, me llamo abbbvaabableria micol. garcia
Tengo 19 a;os, fui al cole1. gio esq123 uiu.
'''
#busco una palabra en la cadena de texto, la primera
resultado = re.search("Hola",texto)
print (resultado)

#busco todas las coincideencia con hola
resultado = re.findall("Hola",texto,flags=re.IGNORECASE) #esto te ignora las mayusculas y minusuclas
print (resultado)

#\d --> busca digitos numericos del 0 al 9
resultado = re.findall(r"\d",texto)
print (resultado)
print ("  ")

#\D --> busca TODO MENOS los digitos numericos del 0 al 9
resultado = re.findall(r"\D",texto)
print (resultado)
print ("  ")

#\w --> busca caracteres alfanumericos (a-z / A-Z / 0-9 / _)
resultado = re.findall(r"\w",texto)
print (resultado)
print ("  ")

#\W --> busca TODO MENOS caracteres alfanumericos (a-z / A-Z / 0-9 / _)
resultado = re.findall(r"\W",texto)
print (resultado)
print ("  ")

#\s --> busca espacios en blanco --> espacios, tabs, saltos de linea
resultado = re.findall(r"\s",texto)
print (resultado)
print ("  ")

#\S --> busca TODO MENOS espacios en blanco 
resultado = re.findall(r"\S",texto)
print (resultado)
print ("  ")

#\n --> busca saltos de linea
resultado = re.findall(r'\n',texto)
print (resultado)
print ("  ")

#. --> busca TODO MENOS saltos de linea
resultado = re.findall(r'.',texto)
print (resultado)
print ("  ")

#\ --> cancela caracteres especiales --> todos los que no son alfanumericos (a-z,A-Z,0-9,_)
#cancela la funcion del punto y busca los puntos
resultado = re.findall(r'\.',texto)
print (resultado)
print ("  ")

#armando una cadena que busque un numero, seguido de un punto, seguido de un espacio
resultado = re.findall(f'\d\.\s', texto)
print(resultado)
print("  ")

# ^ --> busca el comienzo de una linea (te dice si hola esta al comienzo de una linea o no)
#con el parametro ( flags= re.M ) activo MULTILINEA
# lo que hago es que me tome cada linea con un comienzo
#sino solo el comienzo de linea esta al inicio de la cadena
resultado = re.findall(r'^Hola',texto,flags= re.M)
print (resultado)
print ("  ")

#$ --> busca el final de una linea
resultado = re.findall(r'garcia$',texto,flags= re.M)
print (resultado)
print ("  ")

#{n} --> busca n cantidad de veces el valor de la izquierda
#aca deberia buscar 3 digitos que aparezcan todos juntos y un espacio
resultado = re.findall(r'\d{3}\s',texto)
print (resultado)
print ("  ")

#{n,m} --> al menos n, cmo maximo m
#en este caso busca minimo 1 maximo 4 "b" seguidas de una "a"
resultado = re.findall(r'(ab){1,4}',texto)
print (resultado)
print ("  ")

#devuelve 1 ab por cada 2 ab que encontro juntos
resultado = re.findall(r'(ab){2}',texto)
print (resultado)
print ("  ")

# | --> devuelve una cosa o la otra
resultado = re.findall(r'\d{2,4}|Hola',texto)
print (resultado)
print ("  ")
