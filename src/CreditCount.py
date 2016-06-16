import csv

file = open("OPTPF.csv")
data = csv.reader(file, delimiter='|')
total = 0

for rows in data:
    if rows[9] == 'C' and (int(rows[8]) / 100) > 15000:
        total += 1
print(total)

file.close()
