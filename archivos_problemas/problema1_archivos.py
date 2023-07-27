
#2 listas, 1 con nombres y otra con apellidos
nombres = ["Vale","Amarinda","Milena","Martina","Micaela","Rosario"]
apellidos = ["Garcia","Loiseau","Confeggi","Gargano","Bogastti","Rissi"]

#Registro esta informacion en un txt de forma optima
with open ("archivos_problemas\\nombres_y_apellidos.txt","w") as archivo:
    print ("El archivo se abrio correctamente")
    archivo.writelines("Los datos son:\n")
    [archivo.writelines(f"Nombre: {n}\nApellido: {a}\n ------\n") for n,a in zip(nombres,apellidos)]
    #la linea de arriba es lo mismo que esto:, pero lo meto adentro de un array e invierto orden
    #for n,a in zip (nombres,apellidos):
        #archivo.writelines(f"Nombre{n}\nApellido: {a}\n ------\n")
    