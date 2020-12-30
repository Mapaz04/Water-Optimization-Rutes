# Problema de transporte

_Una vez obtenidos los costos de distancia individuales, se procede con la optimización_
ADAPTACIÓN DE: https://scipbook.readthedocs.io/en/latest/intro.html#transportation-problem

## Pre-requisitos

_La librería que permite la optimización es la siguiente:_
* pyscipopt 3.0.1: https://pypi.org/project/PySCIPOpt/

ANTES DE INSTALARLA! 
Tomar en cuenta que esta librería es una interfaz del software **SCIP Optimization Suite**. Por ello, 
EL SOFTWARE DEBE INSTALARSE PRIMERO: http://scip-interfaces.github.io/PySCIPOpt/docs/html/md_INSTALL.html (aquí documentación de la interfaz)
AQUI PARA INSTALAR SOFTWARE: https://www.scipopt.org/index.php#download

## Despliegue

_Para obtener, a partir de MINIMINAZAR DISTANCIA O TIEMPO, el valor óptimo, dé qué surtidor a qué nodo no abastecido se debe transportar y cuántos litros en esta ruta se realiza lo siguient:_

1. Abrir el archivo **Transportation-problem.ipynb** en **Jupyter Notebook** y usar los siguientes inputs:
  - nodosnoabastecidos.csv
  - generadoDF
  - dflatlongLima.csv
  - [Costos Individuales](https://github.com/bitmapup/upsunass/blob/master/6.%20Costos/6.1.%20Costos%20individuales/CSV-CostosIndiv-final.zip): descargar según el escenario que se desea optimizar
2. Correr uno a uno las celdas de **Transportation-problem.ipynb** y esperar que culmine el programa.
3. El resultado final será el valor óptimo, de qué surtido a qué nodo no abastecido debe dirigirse y cuántos litros transportar
