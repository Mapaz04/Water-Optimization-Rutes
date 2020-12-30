import pandas as pd
import sys
import csv
import numpy as np


#Abre archivo que contiene los tiempos a corregir
data=open(sys.argv[1])

#lee como un DataFrame el csv
df = pd.read_csv(data, delimiter=',',decimal=".")

#setea la velocidad
velConst=500

#loop para recorrer el DataFrame
for i in range(len(df)):
    #condicion para encontrar los errores
    if (df["distancia"][i][0] == "["):
        #Acción de cambiar el tiempo a partir de dividir el legnht/velocidad=30. Luego redondear
        df["tiempo"][i]=round((df["lengh"][i]/velConst),2)


#imprimir el dataframe antes de exportarlo
#print(df)

print('Hecho!')

#exportarlo en csv con el nombre TiemposCompletos
df.to_csv('TiempoCompletos.csv',index=False)

