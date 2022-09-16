import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("avocado.csv")

# Imprime # de filas
print("La cantidad de filas es:", data.shape[0])

# Imprime # de columnas
print("La cantidad de columnas es:", data.shape[1], "\n")

# Imprime los primeros 100 registros
print("Los primeros 100 registros son:\n\n", data.head(100), "\n\n")

# Imprime los últimos 20 registros
print("Los últimos 20 registros son:\n\n", data.tail(20))

# Imprime el precio mínimo, máximo y promedio del aguacate

frame = pd.DataFrame(data)

a = frame['AveragePrice'].min()
b = frame['AveragePrice'].max()
c = frame['AveragePrice'].sum() / data.shape[0]

print("\n\nPrecio mínimo: $" + str(a))
print("Precio máximo: $" + str(b))
print("Precio promedio: $" + str(round(c, 3)))

# De esta forma se obtiene el menor y el mayor sin las funciones de pandas
"""for i in range(data.shape[0]):
    if frame['AveragePrice'][i] > a:
        a = frame['AveragePrice'][i]
    if frame['AveragePrice'][i] < b:
        b = frame['AveragePrice'][i]"""

# Gráfico Scatter o de dispersión para las variables Year y AveragePrice en 3 regiones
# (Albany, Chicago y Jacksonville)

Albany = frame[frame['region'] == 'Albany']
Chicago = frame[frame['region'] == 'Chicago']
Jacksonville = frame[frame['region'] == 'Jacksonville']

regions = pd.concat([Albany, Chicago, Jacksonville], axis=0)

ax = plt.subplot()
ax.scatter(regions['year'], regions['AveragePrice'])
plt.show()