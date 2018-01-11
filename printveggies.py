vegetables = [
{"name":"eggplant"},
{"name":"tomato"},
{"name":"corn"},
{"name":"potato"},
{"name":"corn"},
{"name":"corn"},
{"name":"kale"}
]

import csv

with open('veggie2.csv', 'w') as f:
	writer = csv.writer(f)
#Write header
	writer.writerow(['name','length'])
#Loop through each vegitable
	for veggie in vegetables:
		name = veggie['name']
		length = len(name)
		writer.writerow([name,length])
#For each vegetable write a row to the csv