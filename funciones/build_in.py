#funciones build_in
#funciones integradas por python

#MAX () --> encuentro el numero maximo de una lista
numeros = [1,2,3,4,5]
num_max = max (numeros)
print(num_max)

#MIN() --> encuentro el numero minimo de una lista
num_min = min (numeros)
print (num_min)

#ROUND --> redondeamos a tantos decimales

#antes
num = round(12.345678 * 100)
print (num / 100) #me muestra un 12.35 porque redondea hacia abajo

#ahora
num = round (12.345678,3) #lo que pongo atras de la coma son los decimales que redondea
print (num)

#BOOL ()--> retorna false si le pasamos como parametro 0, vacio, False, ninguno
res = bool(0)
print (res) #devuelve false
res2 = bool (9)
print (res2) #devuelve true

#ALL () --> retorns true si todos los valores que le pasamos son verdaderos
resultado_all = all ([234,"true",[344,23]])
print (resultado_all)

#SUM() --> suma todos los valores de un iterable
suma_total = sum(numeros)
print (suma_total)








