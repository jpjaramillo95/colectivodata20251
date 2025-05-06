import pandas as pd

usuariosDataFrame=pd.read_excel("./data/usuarios_sistema_completo.xlsx")
# print(usuariosDataFrame)
# print(usuariosDataFrame.isnull().sum())

# Necesito solo un listado de aprendices o estudiantes
# print(usuariosDataFrame["tipo_usuario"].unique()) #Muestra los valores que hay dentro de esa columna
listaAprendicesOEstudiantes=usuariosDataFrame.query('tipo_usuario=="estudiante"')
print(listaAprendicesOEstudiantes)

# Necesito un listado de solo instructores o profesores

# Necesito un listado de especialistas en desarrollo web o sistemas

# Necesito un listado de solo usuarios con direcciones en Medellín

# Necesito un listado de usuarios de cuyas direcciones terminan en sur

# Necesito un listado de especialistas que contengan la palabra datos

# Necesito docentes de Itagui

# Necesito una lista de nacidos del 90 o anteriores

# Necesito un listado de instructores mayores o viejitos

# Necesito un listado de estudiantes o profesores nacidos en el nuevo milenio