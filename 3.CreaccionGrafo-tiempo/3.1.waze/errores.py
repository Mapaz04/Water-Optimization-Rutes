import pandas as pd
from datetime import datetime,timedelta 
import WazeRouteCalculator
import sys
# -*- coding: utf-8 -*-             
data3=open(sys.argv[1]) #Archivo que contiene los tiempos que queremos corrregir             
df3 = pd.read_csv(data3, sep=",", decimal=".", engine='python')               
region="EU" 
vehicle_type="TAXI"
tiemIni = 12 #para toma 12

for i in range(len(df3)):
    if(df3["distancia"][i][0]=="["): #Busca en todo el archivo aquellos registros que empiecen con [ ya que nos indican que es la lista con coordenadas
        a,b,c,d=df3["distancia"][i][2:].replace("[",'').replace("]",'').strip().split(",") #separamos las coordenadas x, y del punto de salida y el punto de llegada
        from_address = str(b.strip()+","+a.strip())
        to_address = str(d.strip()+","+c.strip())  
        route = WazeRouteCalculator.WazeRouteCalculator(from_address, to_address, region,vehicle_type)  
        #If para determinar los minutos de salida dependiendo de la hora actual
        
        if((tiemIni-int(datetime.now().strftime("%H")))<0): #Si la hora actual es mayor que la hora a la que se desea salir
          td=(24+(tiemIni-int(datetime.now().strftime("%H"))))*60
          nuevahora=(datetime.now()+timedelta(hours=tiemIni-int(datetime.now().strftime("%H")))).strftime("%H:%M:%S")
        elif((tiemIni-int(datetime.now().strftime("%H")))>0):#Si la hora actual es menor que la hora a la que se desea salir
          td=(tiemIni-int(datetime.now().strftime("%H")))*60
          nuevahora=(datetime.now()+timedelta(hours=tiemIni-int(datetime.now().strftime("%H")))).strftime("%H:%M:%S")
        elif((tiemIni-int(datetime.now().strftime("%H")))==0):#Si la hora de salida es la misma a la actual
          nuevahora=datetime.now().strftime("%H:%M:%S")
        
        try:#Probara calcular la ruta
          if(td!=0): #Si la hora de salida no es la misma se usara el parametro time_delta
            route_time, route_distance=route.calc_route_info(time_delta=td)
          else: #Si la hora de salida  es la misma no sera necesario el parametro time_delta
            route_time, route_distance=route.calc_route_info()  
          df3["distancia"][i]=round(route_distance,2)
          df3["tiempo"][i]=round(route_time,2) 
        except Exception as e:#Si el calculo bota un error, se imprimira el mensaje de error
            print(e)
    print(i)
df3.to_csv("Calctiemposcorregido.csv") #archivo de salida con las correcciones
