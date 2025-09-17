# IMPORTAR LIBRERIAS
import pandas as pd
# lee el archivo CSV
df = pd.read_csv("C:/Users/Oscar/codigo/tarea/titanic.csv")
# muestra las primeras filas del DataFrame
df.head()
# Con la manera de texto
print(df.head())
# Descripción estadística del DF
df.describe()
# Con manera de texto
print(df.describe)


