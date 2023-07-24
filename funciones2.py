#forma no optima de sumar valores
def suma (a,b):
    return a+b

#sumo valores pasando una lista como parametros --> no optima
def sumavalores (lista):
    suma = 0
    for num in lista:
        suma = suma + num
    return suma

resultado = suma (5,3)
print (resultado)
resultado2 = sumavalores ([2,3,4,5,6,8,9,5])
print (resultado2)

def suma (*numeros): #el * permite varios parametros
    return sum(numeros) #suma los numeros de un iterable

resultado = suma (5,5,5,5,5)
print (resultado)

# el argumento con * solo al final
def suma2 (nombre,*numeros):
    return f" {nombre}, la suma de tus numeros es: {sum(numeros)}"
 
#si tengo su ([*numeros]) , el * solo toma los numeros de la lista por eso se pone el []

