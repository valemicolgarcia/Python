#creando una funcion que nos devuelve los numeros primos
#entre 0 y argumento que pasamos

#creamos funcion que verifique si un numero es primo
def es_primo (num):
    #verificamos que el numero pasado no pueda dividirse 
    #por ningun numero entre el 2 y ese mismo numero - 1
    for i in range(2,num-1): #arranco desde dos porque todos los nros se pueden dividir por 1
        if (num%i == 0): return False
    return True

#creamos funcion que retorna lista con todos los numeros primos
def primos_hasta (num):
    primos = []
    for i in range (3,num+1): #pongo desde el 3 para que no tome el 2
        res = es_primo(i)
        if res == True:
            primos.append(i)
    return primos


resultado = es_primo (13)
print (resultado)   

resultado2 = primos_hasta(13)
print (resultado2)

#SEGUNDA OPCION PARA RESOLVER --> en una sola linea de codigo
print ("segunda opcionnnnnn")
primos_hasta2 = lambda num: list (filter (lambda x:all(x % i != 0 for i in range (2, int (x ** 0.5) + 1)), range(2, num) ))
print (primos_hasta(15))