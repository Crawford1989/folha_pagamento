import pandas as pd
import openpyxl


sis1 = pd.read_excel('data/Folha Pag_sis1.xlsx', engine="openpyxl")

#print(sis1)


filial = sis1.columns[1]  # Pega a primeira filial a partir do nome da coluna
filiais = []  # Lista para armazenar as filiais
valores = []

for _, row in sis1.iterrows():
    if isinstance(row.iloc[1], str) and "Filial" in row.iloc[1]:  
        filial = row.iloc[1]  # Atualiza quando encontra um novo nome de filial
    #filiais.append(filial)  # Adiciona a filial para cada linha do DataFrame

    if isinstance(row.iloc[3], float) and not pd.isna(row.iloc[3]):
        filiais.append(filial)
        valores.append(row.iloc[3])
        
        
df_valores = pd.DataFrame({"Filial":filiais,"Valor":valores})
print(df_valores)






"""sis2 = pd.read_excel('data/Folha Pag_sis2.xlsx', header=1)


tabela2 = sis2[['Filial', 'Data Lcto', 'Valor', 'Hist Lanc']]

sis2_agrupado = sis2.groupby(['Filial', 'Hist Lanc'])['Valor'].sum().reset_index

#tabela2 = tabela2.sort_values(by='Filial')

pd.set_option('display.max_rows', None)  # Mostra todas as linhas
pd.set_option('display.max_columns', None)  # Mostra todas as colunas
print(sis2_agrupado )
#print(tabela2.head())"""