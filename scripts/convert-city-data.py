import csv

#Read imported data and save it into variable "cities"
with open ("data/city-comparison-input.csv") as f:
	reader = csv.DictReader(f)
	cities = list(reader)
	cities = [dict(cities) for cities in cities]

#create a new csv in the format that the bubble chart D3 viz needs
with open ("data/city-comparison-output.csv", "w") as f:
	writer = csv.writer(f)
	#write new title rows
	writer.writerow(["id", "value"])
	for city in cities:
		#write each city's region, and city name, and per capita EVs
		writer.writerow([city["Region"]+"."+city["City"], city["2020 Combined per cap"]])