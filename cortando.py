import pandas as pd

dados = pd.read_csv('20150430_PessoaFisica.csv', names=['numero', 'nome', 'cpf'], index_col=False, error_bad_lines=False, sep=';')

dados.usecols=['nome', 'cpf']
dados = dados.set_index(['nome'])
number_of_rows = dados.shape[0]
number_of_rows = int(number_of_rows)

begin_multiplier = 0
last_multiplier = 100000
iteration = 0
dados = dados.drop('numero', axis=1)

print dados

while last_multiplier < number_of_rows:
    newdf = dados[begin_multiplier:last_multiplier]
    iteration_string = str(iteration)
    novo_corte = iteration_string + 'Corte.csv'
    newdf.to_csv(novo_corte)
    last_multiplier = last_multiplier + 100000
    begin_multiplier = begin_multiplier + 100000
    iteration = iteration + 1

dados.to_csv('Pessoafisica_ajustado.csv')
