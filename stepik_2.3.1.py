from os.path import exists

import numpy as np
import pandas as pd
import requests

url = 'https://stepik.org/media/attachments/lesson/245290/trekking1.xlsx'
filename = 'trekking1.xlsx'
if not exists(filename):
    with open(filename, 'wb') as f_out:
        f_out.write(requests.get(url).content)

data = pd.read_excel(filename, index_col=0) \
    .replace(np.nan, 0) \
    .rename_axis('Название') \
    .sort_values(by=['ККал на 100', 'Название'], ascending=[False, True])

print('\n'.join(data.index.values))
