import re

text = "Pagina web https://www.example.com y tamb podemos visitar"

pattern = "https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

#el signo de pregunta --> encontrame ninguna coincidencia o una, si encontras mas no la muestres
result = re.findall(pattern, text)

print (result)
