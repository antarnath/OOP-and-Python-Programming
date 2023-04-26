import requests
import re
from bs4 import BeautifulSoup
import csv

url = 'https://en.wikipedia.org/wiki/IPhone'
text = requests.get(url).text.encode('utf-8').decode('ascii', 'ignore')
soup = BeautifulSoup(text, 'lxml')
table = soup.find('table', class_ = 'wikitable')
rows = table.find_all('tr')[1:]

iphone_price_dic = {}
for row in rows:
    data = row.find_all(['th', 'td'])
    try:
        version_text = data[0].a.text.split(' ')[1]
        version = re.sub(r"\D", "", version_text)
        version = int(version)
        # print(version)

        price_text = data[-1].text.split('/')[-1].replace('$', '')
        price = re.sub(r'\D', '', price_text)
        # print(version, price)
        price = int(price)
        if  version and price > 100:
            # print(version, price)
            iphone_price_dic[version] = price

    except:
        pass
# print(iphone_price_dic)
# for val , key in iphone_price_dic.items():
#     print(val , key)
csv_fields = ['version', 'price']
with open('iphone_price.csv', 'w', newline='') as csvFile:
    cvswriter = csv.writer(csvFile)
    cvswriter.writerow(csv_fields)
    for key, val in iphone_price_dic.items():
        cvswriter.writerow([key, val])
    csvFile.close()