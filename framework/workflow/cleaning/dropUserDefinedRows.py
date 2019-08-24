# importing pandas module 
import pandas as pd 
import sys

#url = "https://raw.githubusercontent.com/dataoptimal/posts/master/data%20cleaning%20with%20python%20and%20pandas/property%20data.csv"
  
# making data frame from csv file 
#drop values from index label

df = pd.read_csv(sys.argv[1] ) 
columnName = sys.argv[2]
deleteValues = [sys.argv[3], sys.argv[4]]

for i in deleteValues:

  dfUserDroppedRows = df[df[columnName] != i]
  

  
# display 
#dfUserDroppedRows

# Delete the rows with label "Ireland"
# For label-based deletion, set the index first on the dataframe:
#df = df.set_index("ST_NAME")
#df = df.drop(["BERKELEY", "PUTNAM"], axis=0) # Delete all rows with label "Ireland"

#df
dfUserDroppedRows.to_csv (r'/home/amanda/FYP/testcsv/cleanedDataset.csv', index = None, header=True)
