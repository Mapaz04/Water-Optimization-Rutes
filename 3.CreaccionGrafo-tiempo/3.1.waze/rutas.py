#------------------------------NO OLVIDAR LEER EL ARCHIVO README------------------------
import pandas as pd
from datetime import datetime,timedelta
import sys
# -*- coding: utf-8 -*-
data3=open(sys.argv[1]) #Archivo csv que contiene las calles con puntos de origen y de llegada para realizar el calculo de los tiempos de ruta
df3 = pd.read_csv(data3, sep=",", decimal=".", engine='python')

print(len(df3))
puntos=[]


for i in range(len(df3)):#Se forma una lista con las coordenadas de cada trayecto, es decir coordenadas del punto a y coordenadas del punto b. 
                         #Ejemplo:[[-77.0680621, -11.9068279], [-77.0684934, -11.9069826]]

    puntos.append([[round(df3["x"][i],8),round(df3["y"][i],8)],[round(df3["x2"][i],8),round(df3["y2"][i],8)]])

    
import WazeRouteCalculator
region="EU"
vehicle_type="TAXI"
tiempo=[]#calculando para las 12pm
tiemInici = 12
dist=[]
hora=[]
ide=[]


for i in range(len(df3)):
    from_address = str(puntos[i][0][1])+","+str(puntos[i][0][0])
    to_address = str(puntos[i][1][1])+","+str(puntos[i][1][0]) #Se da valor a estas variables recorriendo la lista de coordenadas generada anteriormente
    route = WazeRouteCalculator.WazeRouteCalculator(from_address, to_address, region,vehicle_type)
    now = datetime.now() #+timedelta(hours=1) #Se determina la hora de calculo por si el programa se excede del periodo de tiempo a evaluar y poder eliminar los valores que pasen del intervalo de tiempo
    current_time = now.strftime("%H:%M:%S")
    #If para determinar los minutos de salida dependiendo de la hora actual    
    if((tiemInici-int(datetime.now().strftime("%H")))<0): #Si la hora actual es mayor que la hora a la que se desea salir
        td=(24+(tiemInici-int(datetime.now().strftime("%H"))))*60
        nuevahora=(datetime.now()+timedelta(hours=tiemInici-int(datetime.now().strftime("%H")))).strftime("%H:%M:%S")
        print(td)
        print(nuevahora)
    elif((tiemInici-int(datetime.now().strftime("%H")))>0): #Si la hora actual es menor que la hora a la que se desea salir
        td=(tiemInici-int(datetime.now().strftime("%H")))*60
        nuevahora=(datetime.now()+timedelta(hours=tiemInici-int(datetime.now().strftime("%H")))).strftime("%H:%M:%S")
        print(td)
        print(nuevahora)
    elif((tiemInici-int(datetime.now().strftime("%H")))==0):#Si la hora de salida es la misma a la actual
        nuevahora=datetime.now().strftime("%H:%M:%S")
        
    try:#Probara calcular la ruta
        if(td!=0): #Si la hora de salida no es la misma se usara el parametro time_delta
            route_time, route_distance=route.calc_route_info(time_delta=td)
        else: #Si la hora de salida  es la misma no sera necesario el parametro time_delta
            route_time, route_distance=route.calc_route_info()
        
        tiempo.append(round(route_time,2))
        dist.append(round(route_distance,2))
        hora.append(nuevahora)
        ide.append(i)
        print(i)
    except: #Si el calculo fuese errado, se mostrara las coordenadas de determinado punto para proxima correcion
        tiempo.append(puntos[i])
        dist.append(puntos[i])
        hora.append(nuevahora)
        ide.append(i)
        print(puntos[i])
    #print(i)
dfinal=pd.DataFrame(zip(tiempo,dist,hora,ide),columns=["tiempo","distancia","hora","id"]) #Se crea un dataframe con los calculos realizados
dfinal.to_csv("Calctiempos.csv") #Se exporta el dataframe a un archivo csv


