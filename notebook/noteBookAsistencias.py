import pandas as pd

# Leyendo los datos de asistencias
asistenciaDataFrame=pd.read_csv("./data/asistencia_estudiantes_completo.csv")
# print(asistenciaDataFrame)

# Obteniendo información básica del dataframe
# print(asistenciaDataFrame.info()) #Tipos de datos en la bd y la cantidad

#print(asistenciaDataFrame.tail(20)) #Ultimos 5 registros de la bd -- si en los parentesis pongo un valor me muestra los ultimos x valores

#print(asistenciaDataFrame.head()) #Primeros registros de la bd si pongo un valor en los parentesis me muestra esa cantidad

#print(asistenciaDataFrame.describe()) #Analisis descriptivo de los datos númericos

#print(asistenciaDataFrame.isnull().sum()) #Cuantos datos en la bd estan vacios

print(asistenciaDataFrame['estrato'].value_counts().head()) #Mostrar datos de determinada columna || value_counts() -> cuenta cada uno de los elementos o valores