import pandas as pd
import numpy as np

#function to count thr number of missing values in a given column
def countMissingValues(colName, df):
  dfCol = df[colName]
  return dfCol.isna().sum()  

#user defined missing values
missing_values = ["n/a", "na", "--"]

#read csv with defined missing values 
url = "https://raw.githubusercontent.com/dataoptimal/posts/master/data%20cleaning%20with%20python%20and%20pandas/property%20data.csv"
df = pd.read_csv(url, na_values = missing_values)

print(df, "\n")

#user defined percentage of maximum of allowed missing values
maxPercentageOfMissingValues=20

colNames = list(df)
noOfRows = df.shape[0]
print("Total Number of Rows : ",noOfRows, "\n")
print("Column Name : ", colNames, "\n")

dfMissingValueCriteriaDropped=df
for i in colNames:
  noMissingValues = countMissingValues(i,df)
  print("Total number of missing values in column ", i, "=", noMissingValues)
  #print(noMissingValues/noOfRows)
  #print(maxPercentageOfMissingValues/100)
  if ((noMissingValues/noOfRows)>(maxPercentageOfMissingValues/100)):
    dfMissingValueCriteriaDropped = dfMissingValueCriteriaDropped.drop(i, axis=1)
    print("dropped column ", i)
    
print("dropped due to criteria not met : \n", dfMissingValueCriteriaDropped, "\n")
