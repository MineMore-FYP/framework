# importing pandas module 
import pandas as pd 
url = "https://raw.githubusercontent.com/dataoptimal/posts/master/data%20cleaning%20with%20python%20and%20pandas/property%20data.csv"
  
# making data frame from csv file 
#drop values from index label

df = pd.read_csv(url ) 
columnName = 'NUM_BATH'
deleteValues = ["1","2"]

for i in deleteValues:
  df_filtered = df[df[columnName] == i]
  

  
# display 
df_filtered

# Delete the rows with label "Ireland"
# For label-based deletion, set the index first on the dataframe:
#df = df.set_index("ST_NAME")
#df = df.drop(["BERKELEY", "PUTNAM"], axis=0) # Delete all rows with label "Ireland"

#df
