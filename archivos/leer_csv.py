#ARCHIVOS CSV --> valores separados por comas y por \n
import csv

with open ("archivos\\datos1.csv") as archivo:
    print ("El archivo se abrio correctamente")
    
    #LECTURA DE UN ARCHIVO
    reader = csv.reader(archivo)
    for row in reader:
        print (row) #nos devuelve listas con las filas
    
    
        
    