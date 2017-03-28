
import csv
import requests
from BeautifulSoup import BeautifulSoup

url = 'https://columbian.gwu.edu/{start_year-end_year}'
for text in url.findAll('{2015-2016}, {2014-2015},{2013-2014},{2012-2013},{2011-2012},{2010-2011}) 
	list_of_cells.append(url.replace({start_year-end_year})
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('table')

list_of_rows = []
for row in table.findAll('tr')[1:-1]:
    list_of_cells = []
    for cell in row.findAll('td'):
        list_of_cells.append(cell.text.encode('utf-8'))
    list_of_rows.append(list_of_cells)

outfile = open("faculty.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["Department", "Faculty", "Sponsor", "Title", "Year"])
writer.writerows(list_of_rows)

import csv
import requests
from BeautifulSoup import BeautifulSoup

