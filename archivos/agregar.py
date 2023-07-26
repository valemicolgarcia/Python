#ABRIR EL ARCHIVO CON "A"   
#no sobreescribe, se posiciona al final del archivo

with open ("archivos\\texto1.txt", "a" ) as archivo:
    print ("Se abrio el archivo correctamente")
    #agrego datos al archivo
    for i in range(5):
        archivo.write (f"Linea {i+1} agregada \n")
    
    