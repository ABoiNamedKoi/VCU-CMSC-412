import csv
f = open('datafromamazon.csv')
csv_file = csv.reader(f)
URLarray = []

for row in csv_file:
	URLarray.append(row[0])

filename = "urlfile.csv"
f = open(filename, "w")

for URL in URLarray:
	f.write("ProductName" + "," + "Grade" + "," + "PercentageScore" + "," + "Users" + "," + URL + "\n")

f.close()
