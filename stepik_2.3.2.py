import requests
import xlrd
import numpy as np
import pandas as pd
from os.path import exists


url = 'https://stepik.org/media/attachments/lesson/245290/trekking2.xlsx'
filename = 'trekking2.xlsx'
if not exists(filename):
    with open(filename, 'wb') as f_out:
        f_out.write(requests.get(url).content)

ration = pd.read_excel(filename, index_col=0, sheet_name='Раскладка')

products = pd.read_excel(filename, index_col=0) \
    .replace(np.nan, 0) \
    .rename_axis('Продукт')

ration = ration.join(products, on='Продукт')

names = ['ККал', 'Б', 'Ж', 'У']
for name in names:
    ration[f'{name}'] = ration[f'{name} на 100'] * ration['Вес в граммах'] / 100
