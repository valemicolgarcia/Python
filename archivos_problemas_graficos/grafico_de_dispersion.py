import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos_problemas_graficos\\dinero.csv")
print(df)

#GRAFICO DE BARRAS
sns.scatterplot(x="tiempo",y="dinero",data = df)

#mostramos el grafico
plt.show()
