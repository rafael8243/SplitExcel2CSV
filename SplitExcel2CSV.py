import csv
import pandas as pd

## variables
file_source = 'teste.xlsx'
file_path = ''

## Read sourcefile
xls = pd.read_excel(file_source,sheet_name=None)

## Split and write CSV
for sheet_name, df in xls.items():
    df['sheets'] = sheet_name   
    #df[['sheets']].to_csv(f'{sheet_name}.csv') #Add column with sheet name
    export_csv = df.to_csv (f'{file_path}{sheet_name}.csv', index = None, header=True)
