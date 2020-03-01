data = open('output3.html', 'w', encoding='utf8')

print('<html>', '<body>', '<table>', file=data, sep='\n')
for i in range(1, 11):
    print('<tr>', file=data)
    for j in range(1, 11):
        print('<td>', '<a href=http://' + str(i*j) + '.ru>', i * j, '</a>', '</td>', file=data)
    print('</tr>', file=data)
print('</table>', '</body>', '</html>', file=data, sep='\n')
data.close()
