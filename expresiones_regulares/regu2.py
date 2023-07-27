import re
#la cadena en la que se buscan los patrones
text = "La fecha es 23/06/2021 y el telefono e +1-555-555-5555"

#el patron a buscar
pattern = r"\d{2}/\d{2}/\d{4}"  #22/34/4568 

#el texto con el que se reemplazara el patron
replacement = "Fecha oculta"

#reemplazar todas las apariciones del patron en la cadena de texto
new_text = re.sub(pattern,replacement,text)

#imprimir el resultado
print ("Texto modificado: ", new_text)

