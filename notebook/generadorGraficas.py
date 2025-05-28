import seaborn as sns
import matplotlib.pyplot as plt # pyplot grafica en 2d
import pandas as pd

#Gráfica de barras
colores=["#46d3bc","#2bb6b3","#2399a3","#297d8e","#2f4858","green"]

asistenciaDataFrame=pd.read_csv("./data/asistencia_estudiantes_completo.csv")

plt.figure(figsize=(8,5)) # Tamaño de la imagen
sns.countplot(x='estado', data=asistenciaDataFrame, palette=colores) #Que se va a imprimir
plt.title("Cantidad de registros por estado")
plt.xlabel("Estado")#Como quiero nombrar mi eje x
plt.ylabel("Cantidad")#Como quiero nombrar mi eje y
plt.tight_layout() #Ajustar a la figura
# plt.savefig("C:/xampp/htdocs/clientedatos/src/assets/img/barras.png")
plt.show() #imprimir

#Gráfica de torta
conteoTransporte=asistenciaDataFrame['medio_transporte'].value_counts()

plt.figure(figsize=(5,5))
plt.pie(
    conteoTransporte, #me trae los valores de la variable para la gráfica de torta
    labels=conteoTransporte.index, #Me agrupa por tipo de transporte 
    autopct='%1.1f%%', #Formato para usar los porcentajes
    startangle=140, #Cuantos grados tiene la torta
    colors=sns.color_palette("Blues") #Se genera una paleta de colores automatica a partir de la palabra reservada Blues
)
plt.title("Distribución por medio de transporte")
plt.tight_layout()
plt.show()


# Barras agrupadas
plt.figure(figsize=(10,6))
conteoEstadoMedioTransporte=asistenciaDataFrame.groupby(['estado','medio_transporte']).size().unstack(fill_value=0)#Trae datos en forma de matriz en 1 o 2 direcciones

conteoEstadoMedioTransporte.plot(
    kind='bar', #tipo de gráfica
    figsize=(10,6),
    color=colores
    )
plt.title("Registros por estado y medio de transporte")
plt.xlabel("Estados de asistencia")
plt.ylabel("Medio de transporte")
plt.xticks(rotation=45) # Como son tantos datos se suele presentar de esta manera en diagonal
plt.grid(True)
plt.tight_layout()
plt.show()

# Gráfica de linea
promedioTransporte=asistenciaDataFrame.groupby('medio_transporte')['estrato'].mean().sort_values()#Ordenar medio de transporte x estrato
plt.figure(figsize=(10,5))
plt.plot(promedioTransporte.index,promedioTransporte.values, marker='o', linestyle='-', color="#2f4858")#index -> estiquetas values-> valores marker -> donde se cruzan los datos
plt.title("Promedio de estrato por medio de transporte")
plt.xlabel("Medio de transporte")
plt.ylabel("Estrato promedio")
plt.grid(True)
plt.tight_layout()
plt.show()