import requests
from datetime import date,datetime
page=1
url = f'https://jsonmock.hackerrank.com/api/stocks/'
r = requests.get(url)
stocks = r.json()
res = stocks['data']

firstDate = "1-January-2000"
lastDate = "11-January-2000"

date_parser = lambda x: datetime.strptime(x, "%d-%B-%Y")

d1 = date_parser(firstDate)
d2 = date_parser(lastDate)

for each in res:
	dt = date_parser(each['date'])
	if dt>d1 and dt<d2:
		print(each)

total_pages = stocks['total_pages']
print(total_pages)

for page in range(total_pages):
	for each in page_data:
		dt = date_parser(each['date'])
		if dt>d1 and dt<d2:
			print(each)