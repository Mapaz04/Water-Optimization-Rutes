#generador de df a partir de un csv
import pandas as pd
def DfGenerator (csv):
    return pd.read_csv(csv, sep=',', decimal='.', engine='python')
