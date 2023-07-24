
#DEF --> crear funcion simple
def saludar():
    print ("Hola como estas?")

#DEF (PARAMTROS )funcion con parametros
def saludar2 (nombre, sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        print (f"Hola {nombre} como estas???? ELLA")
    elif (sexo == "hombre"):
        print (f"Hola {nombre} como estas???? EL")
    else:
        print (f"Hola {nombre} como estas???? CRACK")

#crear funcion que retorne multiples valores
#en python las funciones pueden retornar mas de un valor

def contrasena_random (num):
    caracteres = "abcdefghij"
    num_entero = str (num) #convertimos a string el numero --> entero
    num = int (num_entero[0]) #obtiene el primer digito del numero entero (que ahora es string)
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contrasena = f"{caracteres[c1]}{caracteres[c2]}{caracteres[c3]}{num*2}"
    return (contrasena, num)
    
saludar()
saludar2 ("Vale","MujER")

password = contrasena_random (7)[0]
print (f"La contrasena es: {password} ")
numero = contrasena_random (7) [1]
print (f"El numero es {numero} ")
#o podemos desempaquetar para que sea mas eficiente
print ("EMPAQUETADO::::")
passw, primNum = contrasena_random(7)
print (f"El numero retornado en la funcion es {primNum}")
print (f"La contrasena retornada en la funcion es {passw}")



