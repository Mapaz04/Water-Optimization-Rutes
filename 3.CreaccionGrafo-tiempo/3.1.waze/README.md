# Waze

_Esta carpeta permite tomar los tiempos de rutas de las calles (edges) de Lima, **antes de crear el grafo**._

LOS TIEMPOS QUE TOMA EN MINUTOS


## Pre-requisitos

_Se deben descargar todos los archivos de esta carpeta y guardarlos en un mismo lugar._

## Despliegue

_Para obtener el grafo final, se debe seguir el siguiente proceso:_

1. Descocmpromir el archivo calles.zip.
2. Se debe correr lo siguiente (para Ubuntu):
```
python rutas.py calles.csv

```
3. Lo anterior genera Calctiempos.csv con varios errores. Para ello se debe correr lo siguiente (para Ubuntu):
```
python errores.py Calctiempos.csv

```
Esto permitirá volver a tomar los tiempos de las filas que tiene errores.

4. Lo anterior genera Calctiemposcorregido.csv el cual igual posee errores. Por ello, a este csv se le debe agregar la columna **lengh** del archivo lenght.csv y correr (para Ubuntu):
```
python TiempoconVeloconstante.py Calctiemposcorregido.csv

```
Esto permitirá, con un velocidad constante de 500 metros/min y con las distancias (lenght) de cada calle, se hallen los tiempos.

## Consideraciones
_El archivo final obtenido para usarse en la creación del grafo será **TiemposCompletos.csv**_

_Todos los tiempos obtenidos con el proceso anterior se encuentran en un link de drive dentro de **TiemposFinalesCompletos.md**. Se obtuvo tiempos en los siguiente bloques:_
* Lunes-Jueves:
    - 8-10 am
    - 12-14 pm
    - 18-20 pm
* Viernes:
    - 8-10 am
    - 12-14 pm
    - 18-20 pm

_Se debe considerar que de los bloques anteriores, para obtener el tiempo se corre el proceso de la sección anterior una hora después del inicio, es decir para el bloque de lunes-jueves 8-10 am se debe desplegar a las 9 am dentro del lunes a jueves._
