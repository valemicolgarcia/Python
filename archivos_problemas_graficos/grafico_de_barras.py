import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos_problemas_graficos\\ingresos.csv")
print(df)

#GRAFICO DE BARRAS
sns.barplot(x="fuente",y="ingresos",data = df)

#obteniendo el total de ingresos
total = df['ingresos'].sum()
print(total)

#mostramos el grafico
plt.show()
