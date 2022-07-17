import pandas as pd
import matplotlib.pyplot as plt
import csv

datosestudiante = pd.read_csv('datos\estudiante.csv')

print('ESTUDIANTES')
print(datosestudiante)

datosestu1 = pd.read_csv('datos\datos_asistencia.csv')

print('ASISTENCIAS')
print(datosestu1)

estudent = pd.merge(datosestudiante,datosestu1, how='right')
print(estudent)

print('ESTUDIANTES POR CEDULA = 1111111111')
print(estudent[estudent.cedula == 1111111111])

estudent[estudent.cedula == 1111111111].to_csv('datos\asistencia.csv', index=True)

estudent[estudent.cedula == 1111111111]['fecha_dia'].value_counts().plot(kind='bar')

plt.show()