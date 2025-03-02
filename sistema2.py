import pandas as pd
import openpyxl

sis2 = pd.read_excel('data/Folha Pag_sis2.xlsx', header=1)


tabela2 = sis2[['Filial', 'Data Lcto', 'Valor', 'Hist Lanc']]

sis2_df = sis2.groupby(['Filial', 'Data Lcto', 'Hist Lanc'])['Valor'].sum().reset_index()
sis2_df.rename(columns={'Filial':'Filial_Codigo','Hist Lanc': 'Descrição','Valor':'Total Sis 2','Data Lcto':'Data'}, inplace=True)
sis2_df['Data'] = pd.to_datetime(sis2_df['Data'], dayfirst=True).dt.strftime('%d-%m-%Y')

if __name__ == "__main__":
    print(sis2_df)


