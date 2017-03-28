import csv
import requests
from BeautifulSoup import BeautifulSoup

url = 'http://www.tdcj.state.tx.us/death_row/dr_scheduled_executions.html'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('table')

list_of_rows = []
for row in table.findAll('tr')[1:-1]:
    list_of_cells = []
    for cell in row.findAll('td'):
        list_of_cells.append(cell.text)
    list_of_rows.append(list_of_cells)

outfile = open("executions.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["Link", "Last Name", "First Name", "TDCJ Number","Date of Birth","Race","Date Received","County"])
writer.writerows(list_of_rows)

import csv
import requests
from BeautifulSoup import BeautifulSoup

