import pandas as pd
import openpyxl


#sis1 = pd.read_excel('data/Folha Pag_sis1.xlsx')
sis2 = pd.read_excel('data/Folha Pag_sis2.xlsx', header=1)


tabela2 = sis2[['Filial', 'Data Lcto', 'Valor', 'Hist Lanc']]

sis2_agrupado = sis2.groupby(['Filial', 'Hist Lanc'])['Valor'].sum().reset_index

#tabela2 = tabela2.sort_values(by='Filial')

pd.set_option('display.max_rows', None)  # Mostra todas as linhas
pd.set_option('display.max_columns', None)  # Mostra todas as colunas
print(sis2_agrupado )
#print(tabela2.head())