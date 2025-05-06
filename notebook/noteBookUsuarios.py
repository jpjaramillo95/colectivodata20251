import pandas as pd

usuariosDataFrame=pd.read_excel("./data/usuarios_sistema_completo.xlsx")
# print(usuariosDataFrame)
# print(usuariosDataFrame.isnull().sum())

# Necesito solo un listado de aprendices o estudiantes
# print(usuariosDataFrame["tipo_usuario"].unique()) #Muestra los valores que hay dentro de esa columna
listaAprendicesOEstudiantes=usuariosDataFrame.query('tipo_usuario=="estudiante"')
# print(listaAprendicesOEstudiantes)

# Necesito un listado de solo instructores o profesores
# print(usuariosDataFrame["tipo_usuario"].unique()) #Muestra los valores que hay dentro de esa columna
listaInstructoresOProfesores=usuariosDataFrame.query('tipo_usuario=="docente"')
# print(listaInstructoresOProfesores)

# Necesito un listado de especialistas en desarrollo web o sistemas
# print(usuariosDataFrame["especialidad"].unique()) #Muestra los valores que hay dentro de esa columna
listaEspecialistasEnDlloWebODlloSistemas=usuariosDataFrame.query('especialidad=="Ingenieria de Sistemas"')
# print(listaEspecialistasEnDlloWebODlloSistemas)

# Necesito un listado de solo usuarios con direcciones en Medellín
usuariosDireccionMedellin = usuariosDataFrame.loc[
    usuariosDataFrame["direccion"].str.contains("Medellín|Medellin|medellin", case=False, na=False)
]
# print(usuariosDireccionMedellin)

# Necesito un listado de usuarios de cuyas direcciones terminan en sur
usuariosDireccionSur = usuariosDataFrame.loc[
    usuariosDataFrame["direccion"].str.contains("Sur|sur", case=False, na=False)
]
# print(usuariosDireccionSur)

# Necesito un listado de especialistas que contengan la palabra datos
# print(usuariosDataFrame["especialidad"].unique()) #Muestra los valores que hay dentro de esa columna
listadoEspecialistasPalabraDatos = usuariosDataFrame.loc[
    usuariosDataFrame["especialidad"].str.contains("datos", case=False, na=False)
]
# print(listadoEspecialistasPalabraDatos)

# Necesito docentes de Itagui
listaDocentesDeItagui = usuariosDataFrame.loc[
    usuariosDataFrame["direccion"].str.contains("Itagui|Itagüí", case=False, na=False), ["direccion", "tipo_usuario"]
]
# print(listaDocentesDeItagui)

# Necesito una lista de nacidos del 90 o anteriores
# print(usuariosDataFrame["fecha_nacimiento"].dtype) #Esta en formato datetime64
listaNacidosAntesDel90 = usuariosDataFrame.query('fecha_nacimiento <= "1990-12-31"')
# print(listaNacidosAntesDel90)

# Necesito un listado de instructores mayores o viejitos
listaDocentesMayoresDeEdad=usuariosDataFrame.query('fecha_nacimiento <= "2007-05-06" and tipo_usuario == "docente"')
# print(listaDocentesMayoresDeEdad)

# Necesito un listado de estudiantes o profesores nacidos en el nuevo milenio
listaEstudiantesYProfesoresNuevoMilenio=usuariosDataFrame.query('fecha_nacimiento >= "2000-01-01" and tipo_usuario == ["docente" , "estudiante"]')
# print(listaEstudiantesYProfesoresNuevoMilenio)