import pandas as pd
import numpy as np
import sys

#user defined missing values
missing_values = ["n/a", "na", "--"]

df = pd.read_csv(sys.argv[1], na_values = missing_values)
 
numOfColumns = len(df.columns)
#user defined percentage
maxPercentageOfMissingValues=int(sys.argv[2])
threshold = (numOfColumns * maxPercentageOfMissingValues)/100


df = df.dropna(thresh=threshold)
print(df)
dfMissingValueCriteriaDropped.to_csv (r'/home/amanda/FYP/testcsv/cleanedDataset.csv', index = None, header=True)
