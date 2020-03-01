import requests
import xlrd
import xlwt
import os
import zipfile


url = 'https://stepik.org/media/attachments/lesson/245299/rogaikopyta.zip'
zipname = 'rogaikopyta.zip'
if not os.path.exists(zipname):
    with open(zipname, 'wb') as f_out:
        f_out.write(requests.get(url).content)

extract_dir = 'extracted'
if not os.path.exists(extract_dir):
    os.mkdir(extract_dir)
    with zipfile.ZipFile(zipname, 'r') as z:
        z.extractall(extract_dir)

result = xlwt.Workbook()
ws = result.add_sheet('Result')
ws.write(0, 0, 'ФИО')
ws.write(0, 1, 'Начислено')
lines = []
for i, filename in enumerate(os.listdir(extract_dir)):
    wb = xlrd.open_workbook(os.path.join(extract_dir, filename))
    sh = wb.sheet_by_index(0)
    ws.write(i + 1, 0, sh.row_values(1)[1])
    ws.write(i + 1, 1, sh.row_values(1)[3])
    lines.append(f'{sh.row_values(1)[1]} {int(sh.row_values(1)[3])}')

result.save('task005.xlsx')

for line in sorted(lines):
    print(line)
