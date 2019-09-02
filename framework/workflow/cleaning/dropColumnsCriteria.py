import pandas as pd
import numpy as np
import sys
from userScript import *

#function to count thr number of missing values in a given column
def countMissingValues(colName, df):
  dfCol = df[colName]
  return dfCol.isnull().sum()


#read csv with defined missing values
df = pd.read_csv(outputDataset)

#user defined percentage of maximum of allowed missing values
maxPercentageOfMissingValues= userDefinedColPercentage

colNames = list(df)
noOfRows = df.shape[0]
#print("Total Number of Rows : ",noOfRows, "\n")
#print("Column Name : ", colNames, "\n")

dfMissingValueCriteriaDropped=df
for i in colNames:
  noMissingValues = countMissingValues(i,df)

  if ((noMissingValues/noOfRows)>(maxPercentageOfMissingValues/100)):
    dfMissingValueCriteriaDropped = dfMissingValueCriteriaDropped.drop(i, axis=1)

dfMissingValueCriteriaDropped.to_csv (outputDataset, index = False, header=True)
