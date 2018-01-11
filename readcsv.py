import csv
from pprint import pprint

with open('veggies.csv') as f:
	reader = csv.DictReader(f)
	rows = list(reader)

pprint(rows)