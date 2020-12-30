
def Codificador(tipo, exCodi, df):
    CodeInput = input('Inserte el numero de ' + tipo + ': \nEjm: ' + exCodi +'\n')
    for name in range(0, len(df)):
        if (df['name'][name]==CodeInput):
            keyword = df['osmid'][name]
            return keyword