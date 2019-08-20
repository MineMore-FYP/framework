import pandas as pd
import numpy as np
import sys

#user defined missing values
missing_values = ["n/a", "na", "--"]

#read csv with defined missing values 
#url = "https://raw.githubusercontent.com/dataoptimal/posts/master/data%20cleaning%20with%20python%20and%20pandas/property%20data.csv"
df = pd.read_csv(sys.argv[1], na_values = missing_values)

#print(df)

dfDroppedDuplicates = df.drop_duplicates()
dfDroppedDuplicates.reset_index(inplace=True)

dfDroppedDuplicates.to_csv (r'/home/amanda/FYP/testcsv/cleanedDataset.csv', index = None, header=True)

#print(dfDroppedDuplicates)
