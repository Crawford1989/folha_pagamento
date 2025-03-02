import sistema1, sistema2
import pandas as pd


sistema1.sis1_df['Filial_Codigo'] = sistema1.sis1_df['Filial_Codigo'].astype(str)
sistema2.sis2_df['Filial_Codigo'] = sistema2.sis2_df['Filial_Codigo'].astype(str)

merge_df = pd.merge(sistema1.sis1_df, sistema2.sis2_df, how='inner', on=['Filial_Codigo', 'Descrição'])

merge_df.rename(columns={
    'Valor_x':'Total Sis 1',
    'Valor_y': 'Total Sis 2'},inplace=True)

merge_df['Diferença'] = round(merge_df['Total Sis 1'] - merge_df['Total Sis 2'],2)
merge_df.rename(columns={'Filial_Codigo':'ID'}, inplace=True)
merge_df = merge_df[['ID','Filial','Descrição','Total Sis 1','Total Sis 2','Diferença','Data']]

print(merge_df)