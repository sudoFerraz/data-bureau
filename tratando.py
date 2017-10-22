import pandas as pd
from pycpfcnpj import cpfcnpj


dados = pd.read_excel('dados.xlsx')

#for key, value in dados['Num_CPF_CNPJ'].iteritems():
#    try:
#        x = cpfcnpj.validate(value)
#        if x == False:
#            dados.drop(key, inplace=True)
#    except:
#        dados.drop(key, inplace=True)

dados.to_csv('dados_filtrados.txt', header=True, index=False, sep='\t', mode='a')



