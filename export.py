import pandas as pd 
from merge import merge_df as df
import os

output_dir = 'output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def exportar_arquivo(df,formato):
    if formato == 1:
        df.to_excel(os.path.join(output_dir,'Dados_exportados.xlsx'), index=False)
        print('Arquivo exportado em EXCEL!')
    elif formato == 2:
        df.to_csv(os.path.join(output_dir,'Dados_exportados.csv'), index=False)
        print('Arquivo exportado em  CSV!')
    elif formato == 3:
        df.to_json(os.path.join(output_dir,'Dados_exportados.json'), index=False)
        print('Arquivo exportado em JSON!')
    else:
        print('Opção invalida!')
        
        
print('EXCEL -1, CSV -2, JSON -3')

formato =int(input('Escolha uma opção de exportação (1, 2 ou 3): '))
exportar_arquivo(df,formato)