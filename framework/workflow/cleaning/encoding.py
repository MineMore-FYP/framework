#encoding
import pandas as pd
import numpy as np

# Import LabelEncoder
from sklearn import preprocessing
url = "https://raw.githubusercontent.com/dataoptimal/posts/master/data%20cleaning%20with%20python%20and%20pandas/property%20data.csv"
df = pd.read_csv(url ) 
columnName = "ST_NAME"
encodeColumn=df[columnName]
#creating labelEncoder
le = preprocessing.LabelEncoder()

# Converting string labels into numbers.
encodedData=le.fit_transform(encodeColumn)

print(encodedData)
