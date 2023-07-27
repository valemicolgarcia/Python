import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos_problemas_graficos\\info.csv")
print(df)

#GRAFICO LINEAL
sns.lineplot(x="fecha",y="pedidos",data = df)

#ponemos un puntito en un vertice
plt.plot ("01-02",5,"o")

#mostramos el grafico
plt.show()




