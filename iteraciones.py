
frutas = ["banana", "manzana", "durazno", "naranja"]

#funcion CONTINUE
for fruta in frutas:
    if fruta == 'manzana':
        continue #se saltea a la siguiente vuelta y se ignora todo lo de abajo
    print (f'La fruta es: {fruta}')

#funcion BREAK
for fruta in frutas:
    if fruta == 'manzana':
        break #se saltea a la siguiente vuelta y se ignora todo lo de abajo
    print (f'La fruta es: {fruta}')
else:
    print ("Bucle terminado") #cuando hay un break el else tampoco se ejecuta
print ("No se ejecutan mas las frutas")

#recorrer una cadena de texto
cadena = "holasoyvale"
for letra in cadena:
    print (letra)

#multiplicamos por dos cada elemento de una lista en varias lineas
numeros = [1,2,3,4,5,6,7,8,9]
numeros_duplicados = list()
for num in numeros:
    numeros_duplicados.append(num*2)
print (numeros_duplicados)

#for en una sola linea
numeros_duplicados_version2 = [x*2 for x in numeros]
print (numeros_duplicados_version2)


