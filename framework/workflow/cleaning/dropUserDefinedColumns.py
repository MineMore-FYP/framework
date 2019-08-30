import pandas as pd
import numpy as np
import sys

#read csv with defined missing values 
missing_values = ["n/a", "na", "--"]
#url = "https://raw.githubusercontent.com/dataoptimal/posts/master/data%20cleaning%20with%20python%20and%20pandas/property%20data.csv"

df = pd.read_csv(sys.argv[1], na_values = missing_values)

#print(df, "\n")

dropCols = []

#user input to dropCols list
for n in sys.argv[2:]:
	print (n)
	dropCols.append(n)
	
dfUserDroppedCols = df.drop(dropCols, axis=1)

#dfUserDropped.to_csv (r'/home/amanda/FYP/ds/cleanedDataset.csv', index = None, header=True)
dfUserDroppedCols.to_csv (r'/home/amanda/FYP/testcsv/cleanedDataset.csv', index = None, header=True)


#print(dfUserDropped, "\n")

