#Binning for integer features:
import pandas as pd
import numpy as np

url = "https://raw.githubusercontent.com/dataoptimal/posts/master/data%20cleaning%20with%20python%20and%20pandas/property%20data.csv"
 
data = pd.read_csv(url)
colName = "ST_NUM"
df_no_missing = data[colName].dropna()
binArray = np.array([])


for row in df_no_missing:
   intValue = int(row)
   binArray = np.append(binArray, intValue)
  

  
binArray[0]  
#pd.cut(np.array([.2, 1.4, 2.5, 6.2, 9.7, 2.1]), 3, retbins=True)
#pd.cut(np.ones(5), 4, labels=False)

pd.cut(binArray, 3, labels=["0", "1","2"])
