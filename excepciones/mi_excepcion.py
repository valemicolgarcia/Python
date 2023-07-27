class MiExcepcion (Exception): #hereda las propiedades, valores y atributos de la clase EXCEPTION
    def __init__ (self,err):
        print(f"Cometiste el siguiente error: {err}")


#manejando excepcion
try:
    raise MiExcepcion ("HOLA")
except: 
    print("Cometiste un error")

#lanzamos excepcion
raise MiExcepcion("excepcionnn creadaaaa :(   !  )")