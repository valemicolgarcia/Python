
#archivos txt

with open ("archivos\\texto1.txt") as archivo: #abre y cierra el archivo, renombro con as
    print ("Se abrio el archivo correctamente")
    print ("   ")
    #leemos el archivo
    print (archivo.read())
        
    

#with open ("archivos\\texto1", "r"): modo de lectura viene x defecto --> R (READ)
    #print ("Se abrio el archivo correctamente")


