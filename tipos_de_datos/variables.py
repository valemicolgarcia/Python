#DECLARACION Y DEFINICION DE VARIABLES

#variables modificables
a = 2
a += 1
a -= 2
print (a)

#concatenacion con +
nombre = " vale "
bienvenida = "hola" + nombre + "como estas"
print (bienvenida)

# concatenar distintos tipos de datos - le pongo f adelante - sStrings
#toma un dato y lo convierte a texto (integramos)
nombre = 'VAL'
nombre = 5
bienvenida = f"Hola {nombre} como estas? " 
print(bienvenida)

#OPERADORES DE PERTENENCIA (in y not in)
print ("ola" in bienvenida) #me sale true
print ("pedro" in bienvenida) #me sale false
print ("pedro" not in bienvenida) #me sale true


#BORRAR VARIABLES
del bienvenida


#camelCase ---> valeGarcia
#snake ---> vale_garcia --> + recomendado