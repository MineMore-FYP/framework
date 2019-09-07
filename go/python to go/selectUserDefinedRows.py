# importing pandas module
import pandas as pd
import sys
sys.path.append("..")
from userScript import *

# making data frame from csv file
#drop values from index label
df = pd.read_csv(sys_argv[1])

for key, value in selectFromRow.items():
	selectValues = []
	n = 0

	while n < len(selectFromRow[key]):
		selectValues.append(selectFromRow[key][n])
		n = n+1
	for i in selectValues:
		print(i)
		print(key)
		dfAfterUserSelectedRows = df[df[key] == i]
		df = dfAfterUserSelectedRows


dfAfterUserSelectedRows.to_csv ("/home/amanda/FYP/testcsv/cleanedDataset.csv", index = False, header=True)
