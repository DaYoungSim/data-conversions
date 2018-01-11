# Read veggie2.csv
import csv

with open('veggie2.csv') as f:
	#convert to jsableson
	reader = csv.DictReader(f)
	vegetables = list(reader)
 
#Write to JSON file
import json

with open('veggie2.json', 'w') as f:
	json.dump(vegetables, f, indent=2)
  