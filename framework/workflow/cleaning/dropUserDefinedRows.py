# importing pandas module
import pandas as pd
import sys
from userScript import *


# making data frame from csv file
#drop values from index label

df = pd.read_csv(outputDataset)

for key, value in dropFromRow.items():
	deleteValues = []
	n = 0

	while n < len(dropFromRow[key]):
		deleteValues.append(dropFromRow[key][n])
		n = n+1
	for i in deleteValues:
		print(i)
		print(key)
		dfAfterUserDroppedRows = df[df[key] != i]
		df = dfAfterUserDroppedRows
		

dfAfterUserDroppedRows.to_csv (outputDataset, index = False, header=True)
