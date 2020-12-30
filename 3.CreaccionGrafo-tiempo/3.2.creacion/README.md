# Creación de grafo - tiempo

_Se debe desarrollar un Grafo con los datos de Lima extraídos en el paso anterior para modelar considerando **calles == aristas** y **esquinas == nodos**_


## Pre-requisitos

_Se deben descargar todos los archivos de esta carpeta y guardarlos en un mismo lugar._

_Se deben copiar los tiempos obtenido de la carpeta **WAZE** en una nueva columna dentro del archivo edges-distancia.csv (ver carpeta CreacionGrafo-distancia>>CSV.TXT-distancia>> edges-distancia.csv) y guardarlo con el nombre edges-tiempo.csv. Para este caso se copiaron los tiempos del bloque viernes 12-14 pm._

## Despliegue

_Para obtener el grafo final, se debe tomar en cuenta el siguiente proceso:_

1. Descomprimir el archivo **creagrafo-tiempo.ipynb.zip** y descargar los archivos de la carpeta compartida de Drive **CSV.TXT-tiempo**. Luego abrirlo en **Jupyter Notebook**.
2. Correr uno a uno las celdas  **creagrafo-tiempo.ipynb** y esperar que culmine el programa.
3. Copiar lo siguiente en un archivo de texto vacio en el siguiente orden:
    a) base-tiempo.txt
    b) creacionnodos.txt
    c) creacionedges.txt
4. Pegar los siguiente al final:
```
</graph>
</graphml>

```
5. Guardar el archivo con la siguiente forma: **lima-tiempo.graphml**

_El archivo de la forma graphml creado servirá de input para la carpeta **dijkstra**_
