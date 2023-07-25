#ejercicios practicos 2



def obtener_companeros (cant):
    companeros = []
    #ejecutamos un for para pedir informacion a cada companero
    for i in range (cant):
        nombre = input ("Ingrese el nombre del companero: ")
        edad = int (input ("Ingrese la edad del companero: "))
        companero = (nombre,edad) #tupla 
        
        #agregamos informacion a la lista de tuplas (companeros)
        companeros.append(companero)
        
    #ordenamos de menor a mayor segun la edad    
    companeros.sort(key = lambda x:x[1]) #aca le indico que quiero que los ordene por el segundo parametro
    
    #companeros [x] devuelve una tupla con (nombre, edad), entonces accedemos a los nombres:
    asistente = companeros [0][0] # primer elemento de la lista
    profesor = companeros[-1][0] #ultimo elemento de la lista
    
    #retornamos una tupla
    return asistente,profesor

#desempaquetamos lo que nos retorna la funcion
asistente,profesor = obtener_companeros(5)

print (f"El profesor es {profesor} y su asistente es {asistente}")

    
    