import csv

import collections

file = open("OPTPF.csv")
data = csv.reader(file, delimiter='|')

recordsPerMerchant = collections.Counter()
for row in data:
    recordsPerMerchant[row[0]] += 1

# print(recordsPerMerchant.most_common())
print("DTV  : " + str(recordsPerMerchant.__getitem__('DTV')))
print("HANA : " + str(recordsPerMerchant.__getitem__('HANA')))
print("DIAM : " + str(recordsPerMerchant.__getitem__('DIAM')))
print("HERM : " + str(recordsPerMerchant.__getitem__('HERM')))
print("KTNS : " + str(recordsPerMerchant.__getitem__('KTNS')))
print("JESS : " + str(recordsPerMerchant.__getitem__('JESS')))
print("MALS : " + str(recordsPerMerchant.__getitem__('MALS')))
