import csv

file = open("OPTPF.csv")
data = csv.reader(file, delimiter='|')

for row in data:
    print(row[0]+" "+row[1]+" "+row[3]+" "+row[8])

file.close()