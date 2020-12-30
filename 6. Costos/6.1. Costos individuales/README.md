
# Costos individuales

_Permite tener los costos en distancia y tiempo para recorrer desde cada surtidor a todos los nodos nos abastecidos._


## Pre-requisitos

_En el despliegue se importa **generadorDF**, el cual es un archivo de py que se encuentra en esta misma carpeta_
 

## Despliegue

_Para obtener los costos finales, se debe tomar en cuenta el siguiente proceso:_

1. Abrir el archivo **Costos_individuales.ipynb** en **Jupyter Notebook** y usar los siguientes inputs:
  - generadoDF.py
  - nodosnoabastecidos.csv
  - surtidoresajustados.csv
  - [Grafos generados](https://github.com/bitmapup/upsunass/tree/master/3.CreaccionGrafo-tiempo/3.3.grafos%20generados): descargar según el escenario que se desea obtener los costos
2. Correr una a una las celdas de **Costos_individuales.ipynb** y esperar que culmine el programa.
3. El resultado final será un CSV con todos los costos. 

Los resultados de obtenidos del programa se encuentran en **CSV-CostosIndiv-final.zip**. Distancias en METROS y tiempos en MINUTOS
