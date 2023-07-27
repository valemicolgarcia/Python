#PROBLEMAS ARCHIVOS CSV

import pandas as pd
df = pd.read_csv("archivos_problemas\\datos1.csv")
print (df) #muestro todo el archivo
print ("   ")

#CAMBIAR TIPO DE DATO DE UNA COLUMNA

print ("Tipo de dato de la edad sin modificarlo: ")
print (type(df['edad'][0])) #muestro tipo de daro
df['edad'] = df['edad'].astype(str) #convierto el tipo de dato de edad a string
print ("  ")

print ("Tipo de dato de la edad despues de modificarlo: ")
print (type(df['edad'][0])) #muestro tipo de daro
print("   ")

#REEMPLAZAR VALOR (reemplaza todas las veces que aparece garcia por genia)
df['apellido'].replace("garcia","genia",inplace=True)
print (df['apellido'])

#ELIMINAR FILAS CON DATOS FALTANTES
print(df)
df = df.dropna() #axis = 0 , por defecto
print(df)

#ELIMINAR COLUMNAS CON DATOS FALTANTES
df = df.dropna(axis = 1)

#ELIMINAR FILAS REPETIDAS
df = df.drop_duplicates()
print (df)

#CREAMOS UN CSV CON EL DATAFRAME RESULTANTE
df.to_csv("archivos_problemas\\datos1_limpios.csv")
