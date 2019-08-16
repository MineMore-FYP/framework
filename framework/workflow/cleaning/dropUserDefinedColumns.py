import pandas as pd
import numpy as np

#read csv with defined missing values 
missing_values = ["n/a", "na", "--"]
url = "https://raw.githubusercontent.com/dataoptimal/posts/master/data%20cleaning%20with%20python%20and%20pandas/property%20data.csv"
df = pd.read_csv(url, na_values = missing_values)

print(df, "\n")

#user input to dropCols list
dropCols = [ 'NUM_BEDROOMS', 'OWN_OCCUPIED']
dfUserDropped = df.drop(dropCols, axis=1)

print(dfUserDropped, "\n")

