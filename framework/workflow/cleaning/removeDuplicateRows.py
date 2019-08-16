import pandas as pd
import numpy as np

#user defined missing values
missing_values = ["n/a", "na", "--"]

#read csv with defined missing values 
url = "https://raw.githubusercontent.com/dataoptimal/posts/master/data%20cleaning%20with%20python%20and%20pandas/property%20data.csv"
df = pd.read_csv(url, na_values = missing_values)

print(df)

dfDroppedDuplicates = df.drop_duplicates()
dfDroppedDuplicates.reset_index(inplace=True)

print(dfDroppedDuplicates)
