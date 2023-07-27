
def sumar_dos ():
    while True:
        a = input("numero 1: ")
        b = input("numero 2: ")
        try:
            resultado = int(a) + int(b)
        except Exception as e: #en vez de excepcion podemos poner ValueError
            print("Ingresaste un string, no un numero.")
            print (f"ERROR!!!!:  {e}")
            print (f"Tipo de error: {type(e).__name__}")
            print("Ingrese nuevamente los valores solicitados")
        #podemos usar varios except: 
        except ZeroDivisionError:
            print("No dividas por ceroooo")
        else:
            break
        finally:
            print ("Manejo de excepcion finalizado --> se ejecuta siempre")
            
    return resultado

print(sumar_dos())

