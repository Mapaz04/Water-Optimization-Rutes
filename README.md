# Proyecto de Distribución de Agua

_El siguiente proyecto tiene como objetivo encontrar la ruta óptima que deben seguir los camiones cisterna de SUNASS por las calles de Lima, Perú._

## Proceso del proyecto
_Para lograr esto se seguirá el siguiente proceso:._
1. **Extraer los datos (calles y esquinas) de Lima** a partir de OpenStreetMaps. Para ver cómo: carpeta **extracción-datos**.
2. Estos datos georreferenciados extraídos permitirán **elaborar el grafo de Lima que servirá como modelo**; donde las calles serán edges y las esquinas nodos del modelo. Para elaborar el grafo revisar carpeta **CreacionGrafo-distancia**, grafo con distancias de las calles, y **CreacionGrafo-tiempo**, para grafo con tiempos de ruta en las calles.
3. Con los 2 grafos obtenidos, se debe **correr el algoritmo dijkstra** que permitirá obtener la ruta más corta a partir de la distancia y del tiempo. El algortimo **dijkstra** y los grafos se encuentra en la carpeta del mismo nombre.
4. Esta ruta óptima, a partir de la distancia y tiempo, se mostrará en un **demo funcional** el cual se puede revisar en la carpeta Demo.
5. Para finalizar, se respondará la pregunta cuánto distribuir y de qué surtido a qué nodo no abastecido será la ruta. Todo este despliegue se encuenta en la carpeta **Costos**

## Pre-requisitos

_Lenguaje de programación: Python3_

_Plataformas de apoyo:_
* OpenStreetMaps
* Jupyter Notebook

_Librerías de Python para el despliegue:_
* WazeRouteCalculator 0.12 https://pypi.org/project/WazeRouteCalculator/
* folium 0.10.1 https://pypi.org/project/folium/
* osmnx 0.11.3 https://pypi.org/project/osmnx/
* networkx 2.4 https://pypi.org/project/networkx/
* pandas 1.0 https://pypi.org/project/pandas/
* matplotlib 3.2.0 https://matplotlib.org/3.2.0/users/installing.html
* pyproj 2.6.0 https://pypi.org/project/pyproj/
* IPython https://ipython.org/install.html
* scipy 1.5.1 https://pypi.org/project/scipy/
* sklearn 0.23.1 https://pypi.org/project/scikit-learn/
* plotly 4.8.2 https://pypi.org/project/plotly/
