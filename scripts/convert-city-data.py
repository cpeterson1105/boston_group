import csv

with open ("data/city-comparison-input.csv") as f:
	reader = csv.DictReader(f)
	cities = list(reader)
	cities = [dict(cities) for cities in cities]

with open ("data/city-comparison-output.csv", "w") as f:
	writer = csv.writer(f)
	writer.writerow(["id", "value"])
	for city in cities:
		writer.writerow(["flare.other."+city["City"], city["2020 Combined per cap"]])