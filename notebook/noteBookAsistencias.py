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

# print(asistenciaDataFrame['estrato'].value_counts().head()) #Mostrar datos de determinada columna || value_counts() -> cuenta cada uno de los elementos o valores

# print(asistenciaDataFrame["medio_transporte"].unique()) #Muestra los valores que hay dentro de esa columna

# ----------------------------------------------------------------------------------------------

#FILTROS O CONSULTAS DETALLADAS

# Encontrar los estudiantes que si asistieron
estudiantesQueAsistieron=asistenciaDataFrame.query('estado=="asistio"')#query es una función para hacer una condición
# print(estudiantesQueAsistieron)

# Necesito Encontrar los estudiantes que faltaron
estudiantesQueNoAsistieron=asistenciaDataFrame.query('estado=="inasistencia"')

# Encontrar los estudiantes que llegaron tarde (justificaron)


# Encontrar los estudiantes de estrato 1
estudiantesEstratoUno=asistenciaDataFrame.query('estrato==1')
# print(estudiantesEstratoUno)

# Encontrar los estudiantes de estratos altos (5,6)

# Encontrar estudiantes que llegan en metro
estudiantesQueLleganEnMetro=asistenciaDataFrame.query('medio_transporte=="metro"')
# print(estudiantesQueLleganEnMetro)

# Encontrar estudiantes que llegaron en bicicleta

# Encontrar todos los estudiantes MENOS los que llegaron a pie
estudiantesQueNoCaminan=asistenciaDataFrame.query('medio_transporte!="a pie"')

# Encontrar todos los registros de asistencia de Junio

# Encontrar los estudiantes que usan transportes ecologicos

# Encontrar los estudiantes que usan bus y son de estrato alto

# Encontrar los estudiantes que usan bus y son de estrato bajo

# Encontrar los estudiantes que caminan para llegar a clases

# -------------------------------------------------------------------
# CONTEOS POR AGRUPACIONES

# Conteo de registros por estado de asistencia
conteo=asistenciaDataFrame.groupby('estado').size()
# print(conteo)

# Obtener el número de registros por estrato

# Cantidad de estudiantes por medio de transporte
conteoMedioTransporte=asistenciaDataFrame.groupby('medio_transporte').size()
# print(conteoMedioTransporte)

# Promedio de estrato por estado de asistencia
promedioAsistenciaEstrato=asistenciaDataFrame.groupby('estado')['estrato'].mean()
print(promedioAsistenciaEstrato)

# Máximo estrato por estado

# Minimo estrato por estado

# Conteo de asistencias por grupo y estado