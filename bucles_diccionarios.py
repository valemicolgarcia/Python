#iterar diccionarios

diccionario = {
    "nombre" : "vale",
    "apelllido" : "garcia",
    "dni" : 45356003,
}

#recorriendo diccionario para obtener las claves
for key in diccionario.items():
    print (f"La clave es: {key}")  

#recorriendo un diccionaraio con items() para obtener clave y valor
for datos in diccionario.items():
    key = datos [0]
    value = datos [1]
    print (f"La clave es: {key} y el valor es: {value}")


