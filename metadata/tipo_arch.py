import pandas as pd


class TipoArch:

    tipos = ['xlsx', 'csv', 'txt', 'xlsm', 'xlsb']

    lectura = {'xlsx': pd.read_excel, 'csv': pd.read_csv, 'txt': pd.read_table,
               'xlsm': pd.read_excel, 'xlsb': pd.read_excel}
