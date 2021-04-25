# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 18:54:46 2021
@author: ANDRES
"""
import numpy as np
import pandas as pd 

url="Casos_positivos_de_COVID-19_en_Colombia.csv"
data=pd.read_csv(url)

# 1 Número de casos de Contagiados en el País.

print('El numero total de contagiados en el pais es :', data.shape[0])

# 2 Número de Municipios Afectados

municipios = data.groupby('Código DIVIPOLA municipio').sum().reset_index()
print('El Número de Municipios Afectados es: ' , municipios.shape)

#3 Liste los municipios afectados (sin repetirlos)

print(data.groupby('Código DIVIPOLA municipio').sum().reset_index())

# 4 Número de personas que se encuentran en atención en casa

data.loc[data['Ubicación del caso'] == 
               'CASA', 'Ubicación del caso'] = 'Casa'
data.loc[data['Ubicación del caso'] == 
               'casa', 'Ubicación del caso'] = 'Casa'
casa = data[data['Ubicación del caso'] == 'Casa']
print('El numero de personas que se encuentran en atencion en casa son :' , casa.shape)

#5 Número de personas que se encuentran recuperados

recuperado = data[data['Recuperado'] == 'Recuperado']
print('El numero de personas recuperadas son :' , recuperado.shape)

#6 Número de personas que ha fallecido

data.loc[data['Recuperado'] == 
               'fallecido', 'Recuperado'] = 'Fallecido'
data.loc[data['Recuperado'] == 
               'FALLECIDO', 'Recuperado'] = 'Fallecido'
fallecido = data[data['Recuperado'] == 'Fallecido']
print('El numero de personas fallecidas son :' , fallecido.shape)

# 7 Ordenar de Mayor a menor por tipo de caso (Importado, en estudio,
# Relacionado)

sorted_df = data.sort_values(by='Tipo de contagio', ascending =False)
print(sorted_df['Tipo de contagio'].value_counts())

# 8 Número de departamentos afectados

departamentos = data.groupby('Código DIVIPOLA departamento').sum().reset_index()
print('El Número de departamentos afectados es: ' , departamentos.shape)

# 9 Liste los departamentos afectados(sin repetirlos)
departamentos = data.groupby('Código DIVIPOLA departamento').sum().reset_index()
print(departamentos['Código DIVIPOLA departamento'])

#10 Ordene de mayor a menor por tipo de atención
tipoAtencion = data.sort_values(by='Tipo de recuperación', ascending =False)
print(tipoAtencion['Tipo de recuperación'].value_counts())

#11 Liste de mayor a menor los 10 departamentos con mas casos de
# contagiados

datos = data['Nombre departamento'].value_counts().sort_index(ascending=False).sort_values(ascending=False)  
print(datos[0:10])

# 12. Liste de mayor a menor los 10 departamentos con mas casos de
# fallecidos

data.loc[data['Recuperado'] == 
              'fallecido', 'Recuperado'] = 'Fallecido'
data.loc[data['Recuperado'] == 
              'FALLECIDO', 'Recuperado'] = 'Fallecido'
fallecido = data[data['Recuperado'] == 'Fallecido']
datos = fallecido['Nombre departamento'].value_counts().sort_index(ascending=False).sort_values(ascending=False)  
print(datos[0:10])

# 13. Liste de mayor a menor los 10 departamentos con mas casos de
# recuperados

recuperado = data[data['Recuperado'] == 'Recuperado']
datos = recuperado['Nombre departamento'].value_counts().sort_index(ascending=False).sort_values(ascending=False)  
print(datos[0:10])

# 14. Liste de mayor a menor los 10 municipios con mas casos de
# contagiados

datos = data['Nombre municipio'].value_counts().sort_index(ascending=False).sort_values(ascending=False)  
print(datos[0:10])

# 15. Liste de mayor a menor los 10 municipios con mas casos de
# fallecidos

data.loc[data['Recuperado'] == 
              'fallecido', 'Recuperado'] = 'Fallecido'
data.loc[data['Recuperado'] == 
              'FALLECIDO', 'Recuperado'] = 'Fallecido'

recuperado = data[data['Recuperado'] == 'Fallecido']
datos = recuperado['Nombre municipio'].value_counts().sort_index(ascending=False).sort_values(ascending=False)  
print(datos[0:10])




























