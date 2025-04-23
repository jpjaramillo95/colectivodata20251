import pandas as pd

usuariosDataFrame=pd.read_excel("./data/usuarios_sistema_completo.xlsx")
# print(usuariosDataFrame)
print(usuariosDataFrame.isnull().sum())