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
# print(estudiantesQueNoAsistieron)

# Encontrar los estudiantes que llegaron tarde (justificaron)
estudiantesQueLLeganTarde=asistenciaDataFrame.query('estado=="justificado"')
# print(estudiantesQueLLeganTarde)

# Encontrar los estudiantes de estrato 1
estudiantesEstratoUno=asistenciaDataFrame.query('estrato==1')
# print(estudiantesEstratoUno)

# Encontrar los estudiantes de estratos altos (5,6)
estudiantesEstratosAltos=asistenciaDataFrame.query('estrato==[5,6]')
# print(estudiantesEstratosAltos)

# Encontrar estudiantes que llegan en metro
estudiantesQueLleganEnMetro=asistenciaDataFrame.query('medio_transporte=="metro"')
# print(estudiantesQueLleganEnMetro)

# Encontrar estudiantes que llegaron en bicicleta
estudiantesQueLleganEnBicicleta=asistenciaDataFrame.query('medio_transporte=="bicicleta"')
# print(estudiantesQueLleganEnBicicleta)


# Encontrar todos los estudiantes MENOS los que llegaron a pie
estudiantesQueNoCaminan=asistenciaDataFrame.query('medio_transporte!="a pie"')

# Encontrar todos los registros de asistencia de Junio
# print(asistenciaDataFrame["fecha"].dtype) #Esta en formato object
asistenciaDataFrame["fecha"] = pd.to_datetime(asistenciaDataFrame["fecha"])
# print(asistenciaDataFrame["fecha"].dtype) #Verifico que haya cambiado a formato datetime
# print(asistenciaDataFrame["fecha"].dt.month.value_counts())  # Verifico qué meses están presentes
# registroAsistenciaJunio = asistenciaDataFrame.query('fecha.dt.month == 6')
# print(registroAsistenciaJunio)

# Encontrar los estudiantes que usan transportes ecologicos
estudiantesQueUsanTransportesEcologicos=asistenciaDataFrame.query('medio_transporte==["a pie", "metro", "bicicleta"]')
# print(estudiantesQueUsanTransportesEcologicos)

# Encontrar los estudiantes que usan bus y son de estrato alto
estudiantesQueUsanBusYSonEstratoAlto=asistenciaDataFrame.query('medio_transporte=="bus" and estrato==[5,6]')
# print(estudiantesQueUsanBusYSonEstratoAlto)

# Encontrar los estudiantes que usan bus y son de estrato bajo
estudiamtesQueUsanBusYSonEstratoBajo=asistenciaDataFrame.query('medio_transporte=="bus" and estrato==[1,2]')
# print(estudiamtesQueUsanBusYSonEstratoBajo)

# Encontrar los estudiantes que caminan para llegar a clases
estudiantesQueCaminan=asistenciaDataFrame.query('medio_transporte=="a pie"')
# print(estudiantesQueCaminan)

# -------------------------------------------------------------------
# CONTEOS POR AGRUPACIONES

# Conteo de registros por estado de asistencia
conteo=asistenciaDataFrame.groupby('estado').size()
# print(conteo)

# Obtener el número de registros por estrato
registrosPorEstrato=asistenciaDataFrame["estrato"].value_counts() #Conteo de registros ordenado de mayor a menor
# print(registrosPorEstrato)

# Cantidad de estudiantes por medio de transporte
conteoMedioTransporte=asistenciaDataFrame.groupby('medio_transporte').size()
# print(conteoMedioTransporte)

# Promedio de estrato por estado de asistencia
promedioAsistenciaEstrato=asistenciaDataFrame.groupby('estado')['estrato'].mean()
# print(promedioAsistenciaEstrato)

# Máximo estrato por estado
maximoEstratoPorEstado=asistenciaDataFrame.groupby('estado')['estrato'].max()
# print(maximoEstratoPorEstado)

# Minimo estrato por estado
minimoEstratoPorEstado=asistenciaDataFrame.groupby('estado')['estrato'].min()
# print(minimoEstratoPorEstado)

# Conteo de asistencias por grupo y estado
conteoAsistenciaGrupoYEstado=asistenciaDataFrame.groupby(['estado', 'id_grupo']).size()
# print(conteoAsistenciaGrupoYEstado)