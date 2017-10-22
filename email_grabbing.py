import pandas as pd
import numpy as np
import json


dados = pd.read_csv('base_email_separada.csv', error_bad_lines=False)

number = dados.shape[0]

iterator = 0
barran = "\N"
nan = "nan"
nann = "NaN"
lista = []

for key, value in dados['Des_Email'].iteritems():
    value = str(value)
    value = value.strip()
    if value != None:
        if value != np.nan:
            if value != barran:
                if value != nan:
                    if value != nann:
                        iterator = iterator + 1
                        lista.append(value)

with open('json.json', 'w') as outfile:
    json.dump(lista, outfile)

