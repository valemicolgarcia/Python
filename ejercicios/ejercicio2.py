
#EJERCICIO 2

frase = input ("Ingrese una frase: ")
palabrasSeparadas = frase.split(" ") #el split crea una lista y sus elementis estan determinados por los espacios
cantPalabras = len(palabrasSeparadas)
print (f'La cantidad de palabras es de {cantPalabras} ')
print (f'Tardarias en decirlas {cantPalabras/2} segundos')

if cantPalabras > 120:
    print ("Son muchas palabras")
else:
    print ("Esta bien la cantidad")