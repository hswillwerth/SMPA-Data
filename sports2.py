import csv
import requests
from BeautifulSoup import BeautifulSoup
import re

url = 'http://m.nationals.mlb.com/roster/transactions/2017/03'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('table')

list_of_rows = []
for row in table.findAll('tr')[1:-1]:
    list_of_cells = []
    for cell in row.findAll('td'):
        list_of_cells.append(cell.text)
    for link in row.findAll('a', attrs={'href': re.compile("^http://")}):
    	list_of_cells.append(link.get('href'))
    list_of_rows.append(list_of_cells)

outfile = open("transactions.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["Date", "Text", "URL"])
writer.writerows(list_of_rows)

import csv
import requests
from BeautifulSoup import BeautifulSoup

