import pandas as pd
import numpy as np
from dataType import *



url = "https://raw.githubusercontent.com/dataoptimal/posts/master/data%20cleaning%20with%20python%20and%20pandas/property%20data.csv"
df = pd.read_csv(url)

col = list(df)
for i in col:
    print ("\n") 
    type = dataType(i, df)
    print(i, ": ", type)
    mode = df[i].mode()
    print("Mode :", mode)
    for j in df[i]:
      if type==int: 
        j.interpolate(method ='linear', limit_direction ='backward', limit = 1) 
      elif type==float:
        j.fillna(mode, inplace=True) 
      elif type==str:
        j.fillna(mode, inplace=True) 
     

# Making a list of missing value types
#default null - NA NaN nan blankspace
missing_values = ["n/a", "na", "--"]
df = pd.read_csv(url, na_values = missing_values)


print(df.isnull())  
print(df)



