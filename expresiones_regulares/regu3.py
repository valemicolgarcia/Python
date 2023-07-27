import re

text = "reemplazando todas las vocales por el asterisco"

#como le puse [] tiene que encontrar cualquiera de las vocales
#si no estuviese [], entonces deeberia encontrar una cadena exactamente asi aeiou
new_text = re.sub("[aeiou]", "*", text)

print (new_text)

