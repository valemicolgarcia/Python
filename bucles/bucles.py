#bucles
#iterar listas y tuplas
#los bucles funcionan igual en listas, tuplas y conjuntos

animales = ["gato","perro","loro","vaca"]
numeros = [1,2,3,4]

#FOR
#se ejecuta tantas veces como variables haya
for animal in animales:
    print (f'Ahora la variable es: {animal}')

for num in numeros:
    print (num)
    resultado = num*10
    print (resultado)

#FUNCION ZIP    
#varias iteraciones al mismo tiempo
#las listas tienen que tener la misma cantidad de elementos
for numero,animal in zip (animales,numeros):
    print (f'recorriendo lista 1: {numero}')
    print (f'recorriendo lista 2: {animal}')

#FUNCION RANGE --> va del 10 al 20
for num in range (10,20):
    print (num)

#si ponemos un solo parametro arranca de 0 al numero que le digamos
for num in range (5):
    print (num)

#recorremos lista por el indice --> NO OPTIMA --> no funciona en conjuntos
for num in range (len(numeros)):
    print (numeros[num])
    
#FUNCION ENUMERATE

for num in enumerate(numeros): #num es una tupla, primer elem: indice , segun elem: valor
    indice = num[0]
    valor = num[1]
    print (f'El indice es: {indice} y el valor es: {valor}')

#usando el else
for numero in numeros:
    print (f"ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print ("el bucle termino") #se muestra siempre al final del bucle
