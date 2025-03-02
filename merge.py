import sistema1, sistema2
import pandas as pd


merge_df = pd.merge(sistema1.sis1_df, sistema2.sis2_df, how='inner', on=['Filial', 'Descrição'])

merge_df['Diferença'] = merge_df['Valor_x'] - ['Valor_y']

merge_df.rename(columns={
    'Valor_x':'Valor Sistema 1',
    'Valor_y': 'Valor Sistema 2'},inplace=True)

print(merge_df)