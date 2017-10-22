import pandas as pd

dados = pd.read_excel('dados.xlsx')

row_number = dados.count()
list_for_dataframe = []
number_to_cut = row_count / 10
row_counter = 0
for i in range(row_number):
    row_counter = row_counter + 1
    if row_counter == number_to_cut:
        row_counter = 0
        newdf = pd.DataFrame(list_for_dataframe)
        newdf.to_csv('listacortada', header=True, index=False)
        list_for_dataframe = []
    list_for_dataframe.append(dados.iloc[i])







#print dados
