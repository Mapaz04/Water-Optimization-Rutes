# Creación de grafo - distancia

PRIMERO INGRESAR A LA CARPETA CREACIÓN --> LOS RESULTADOS ESTÁN EN LA CARPETA GRAFOS GENERADOS

_Se debe desarrollar un Grafo con los datos de Lima extraídos en el paso anterior para modelar considerando **calles == aristas** y **esquinas == nodos**_

LA DISTANCIA EN METROS


## Pre-requisitos

_Se deben descargar todos los archivos de esta carpeta, descomprimirlos y guardarlos en un mismo lugar._

## Despliegue

_Para obtener el grafo final, se debe tomar en cuenta el siguiente proceso:_

1. Descomprimir el archivo **creagrafo-distancia.ipynb.zip** y descargar los archivos de la carpeta compartida de Drive **CSV.TXT-distancia**. Luego abrirlo en **Jupyter Notebook**.
2. Correr uno a uno las celdas  **creagrafo-distancia.ipynb** y esperar que culmine el programa.
3. Copiar lo siguiente en un archivo de texto vacio en el siguiente orden:
    a) base-distancia.txt
    b) creacionnodos.txt
    c) creacionedges.txt
4. Pegar los siguiente al final:
```
</graph>
</graphml>

```
5. Guardar el archivo con la siguiente forma: **lima-distancia.graphml**

_El archivo de la forma graphml creado servirá de input para la carpeta **dijkstra**_
