
#archivos csv --> PANDAS
#tuve que instalar pandas, pip ya lo tenia instalado, min 6:23 del video
#es una libreria de python, se la renombra como pd por convencion

import pandas as pd 
print (type(pd))
print ("  ")

#LECTURA DE ARCHIVO
df = pd.read_csv("archivos\\datos1.csv")
df2 = pd.read_csv("archivos\\datos1.csv")
#print (df) #df --> data frame --> filas y columnas
#print ("   ")
#print (df["nombre"]) #obtengo los datos de la columna nombre

#RENOMBRAR LAS COLUMNAS
#puedo renombrar los nombres de las columnas asi:
#el nombre que ya tenia pasa a ser la primer columna de datos
print ("  ")
#df = pd.read_csv ("archivos\\datos1.csv", names= ["name","lastname","age"])
#print (df)
#print ("  ")

#obtengo los datos de la columna nombre
nombres = df ["nombre"]

#ordenando el dataframe por la edad
df_orden_ascendente = df.sort_values("edad")
print (df_orden_ascendente)
print ("  ")

#ordenando de forma descendente
df_orden_descendente = df.sort_values("edad",ascending=False)
print (df_orden_descendente)
print ("  ")

#concatenando los 2 dataframes
df_concatenado = pd.concat([df,df2])
print (df_concatenado)
print ("  ")

#accedo a la primer fila con head
primer_fila = df.head(0) #me muestra el encabezado
print (primer_fila)
print ("   ")
primer_fila = df.head(3) #me muestra las primeras tres filas
print (primer_fila)
print("  ")

#accedo a las ultimas filas
ultimas_filas = df.tail(3)
print (ultimas_filas)
print("   ")

#accediendo a la cantidad de filas y columnas con shape
filas_y_columnas_totales = df.shape
filas_totales = filas_y_columnas_totales[0]
columnas_totales = filas_y_columnas_totales[1]
print (filas_y_columnas_totales)
print(f"Las filas totales son {filas_totales}")
print(f"Las columnas totales son {columnas_totales}")
print("  ")

#desempaquetamos
filas,columnas = df.shape
print(filas)
print(columnas)
print ("  ")

#obteniendo data estadistica del dataframe: --> analisis de datos
df_info = df.describe()
print(df_info)
print("  ")

#accediendo a un elemento especifico del df con loc
elemento_especifico_loc = df.loc[2,"edad"]
print (elemento_especifico_loc)
print ("  ")

#accediendo a un elemento especifico del df con iloc --> indices
elemento_especifico_iloc = df.iloc[2,2]
print (elemento_especifico_iloc)
print ("  ")

#accediendo a todas las filas de una columna
apellidos = df.iloc[:,1]
print (apellidos)
print ("  ")

#accediendo a la fila 3 con loc o con iloc funciona igual
fila_3 = df.loc[2,:]
print (fila_3)
print("   ")

#accediendo a filas con edad mayor a 20
mayor_que_30 = df.loc[df["edad"] > 20,:]
print (mayor_que_30)
print ("  ")

#


