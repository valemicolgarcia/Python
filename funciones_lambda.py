
#funciones lambda --> funciones anonimas --> no tienen nombres
#no apta cuando hay que usar mas de una linea
#ocupa menos lineas 
#ejemplo: 

multiplicar_por_dos = lambda x : x*2
print (multiplicar_por_dos (5))

#es lo mismo que:

def multiplicar_dos (x):
    return x*2
res = multiplicar_dos (5)
print (res)

#ejemplo2
def es_par (num):
    if (num%2 == 0):
        return True

#usando filter con una funcion comun
numeros = [1,2,3,4,5,6,7,8,9]
numeros_pares = filter (es_par,numeros)
#nos ejecuta la funcion es par, y el parametro son cada uno de los elementos de la lista
#los que devuelvan true, los va a agregar a una lista

#print (numeros_pares) #devuelve un objeto filter
print (list(numeros_pares)) #lo hago lista


#creo lo mismo pero con lambda
numeros_pares2 = filter (lambda x: x%2==0,numeros)
print (list(numeros_pares2))

