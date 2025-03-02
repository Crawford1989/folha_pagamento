import pandas as pd
import openpyxl


sis1 = pd.read_excel('data/Folha Pag_sis1.xlsx', engine="openpyxl")

filial = sis1.columns[1] 
filiais = []  
descricoes = []
valores = []


for _, row in sis1.iterrows():
    if isinstance(row.iloc[1], str) and "Filial" in row.iloc[1]:  
        filial = row.iloc[1]  
    else:
        descricao = row.iloc[1]
  
    
    if isinstance(row.iloc[3], float) and not pd.isna(row.iloc[3]):
        filiais.append(filial)
        descricoes.append(descricao)
        valores.append(row.iloc[3])
        
        
sis1_df = pd.DataFrame({"Filial":filiais,"Descrição":descricoes,"Valor":valores})
sis1_df.rename(columns={'Valor':'Total Sis 1'}, inplace=True)

print(sis1_df)

