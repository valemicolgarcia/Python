def frase (nombre,apellido,adjetivo):
    return f"Hola {nombre} {apellido}, sos {adjetivo}"

frase1 = frase ("Valeria", "Garcia","divina")
print (frase1)

#puedo forzar los argumentos poniendolos en lugares diferentes a como se mandan como parametros
#KEYWORD ARGUMENTS
frase2 = frase (adjetivo="genia",nombre="valeeee",apellido="garcia")
print (frase2)

