
with open ("archivos\\texto1.txt", "w" ) as archivo:
    print ("Se abrio el archivo correctamente")
    print ("  ")
    
    #WRITE() --> sobreescribimos el archivo
    #archivo.write ("mi dni es 45356003")
    
    #WRITELINES () --> escribimos varias lineas --> mandamos lista
    #no sobreescribe, se queda posicionado al final del archivo
    archivo.writelines (["Hola como estas \n","valeeeeeee\n"])
    archivo.writelines(["garcia\n", "111\n"])
    
