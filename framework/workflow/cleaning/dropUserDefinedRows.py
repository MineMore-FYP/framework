# importing pandas module
import pandas as pd
import sys



# making data frame from csv file
#drop values from index label

df = pd.read_csv(sys.argv[1] )
columnName = sys.argv[2]
deleteValues = []

for n in sys.argv[3:]:
	#print (n)
	deleteValues.append(n)

for i in deleteValues:
  dfUserDroppedRows = df[df[columnName] != i]

dfUserDroppedRows.to_csv (r'/home/amanda/FYP/testcsv/cleanedDataset.csv', index = None, header=True)
