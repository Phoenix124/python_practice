import requests
import xlrd
import numpy as np
import pandas as pd
from os.path import exists


url = 'https://stepik.org/media/attachments/lesson/245267/salaries.xlsx'
filename = 'salaries.xlsx'
if not exists(filename):
    with open(filename, 'wb') as f_out:
        f_out.write(requests.get(url).content)

wb = xlrd.open_workbook(filename)
sh = wb.sheet_by_index(0)

data = np.array([sh.row_values(i)[1:] for i in range(1, sh.nrows)])

print(sh.row_values(1 + np.median(data, axis=1).argmax())[0])
print(sh.row_values(0)[1 + np.mean(data, axis=0).argmax()])

# Используя pandas:
data = pd.read_excel(filename, index_col=0)

print(data.median(axis=1).idxmax())
print(data.mean(axis=0).idxmax())
