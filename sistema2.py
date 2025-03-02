import pandas as pd
import openpyxl

sis2 = pd.read_excel('data/Folha Pag_sis2.xlsx', header=1)


tabela2 = sis2[['Filial', 'Data Lcto', 'Valor', 'Hist Lanc']]

sis2_df = sis2.groupby(['Filial', 'Data Lcto', 'Hist Lanc'])['Valor'].sum().reset_index()
sis2_df.rename(columns={'Hist Lanc': 'Descrição','Valor':'Total Sis 2','Data Lcto':'Data'}, inplace=True)

print(sis2_df)


