import pandas as pd
import matplotlib.pyplot as plt
# Jesus Arriaga NC = 0019 | Fecha 23/11/2026
# 1. Leer el archivo CSV
df_food_india = pd.read_csv("indian_food.csv")
print("\n--- DATOS LEÍDOS DESDE CSV, COMIDA INDIA - 0019---")
print(df_food_india)
print("--- MOSTRAR NOMBRE COMIDA + INGREDIENTES - 0019---")
recetas = df_food_india[["name", "ingredients"]]
print(recetas)

print("--- MOTRAR 10 PRIMEROS REGISTROS DE TIEMPO DE COCINADO CON HEAD - 0019---")
nombre_y_hora = df_food_india[["name", "cook_time"]].head(10)
print(nombre_y_hora)
print("--- GRÁFICA COMIDA (X) TIEMPO DE COCINADO (Y) - 0019---")
print("--- GRÁFICA COMIDA (X) TEXTO A 30° GRADOS - 0019---")
nombre_y_hora.plot.bar(x="name", y="cook_time", rot=30)
plt.title("Comida tipica de la India - 0019")
plt.xlabel("Nombre de la comida ")
plt.ylabel("Tiempo de cocinado")
plt.show()

print("--- GRÁFICA DE VARIAS COLUMNAS - JESUS 0019---")
nombre_y_hora_prep = df_food_india[["name", "prep_time", "cook_time"]].head(10)
nombre_y_hora_prep.plot.bar(x="name", rot=30)
plt.title("Comida de dos culmnas de la India - 0019")
plt.xlabel("Nombre de la comida ")
plt.ylabel("Tiempo de cocinado y preparación")
plt.show()

print("--- GRÁFICAS APILADAS UNA TRAS OTRA VERTICALMENTE - JESUS 0019---")
nombre_y_hora_prep.plot.bar(x='name', stacked=True, rot=30)
plt.title("Grafica con columnnas apiladas de la India - 0019")
plt.xlabel("Nombre de la comida ")
plt.ylabel("Tiempo de cocinado y preparación")
plt.show()