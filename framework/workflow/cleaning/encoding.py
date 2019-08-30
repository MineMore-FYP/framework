#encoding
import pandas as pd
import numpy as np
from dataType import *

# Import LabelEncoder
from sklearn import preprocessing
#url = "https://raw.githubusercontent.com/dataoptimal/posts/master/data%20cleaning%20with%20python%20and%20pandas/property%20data.csv"
df = pd.read_csv(sys.argv[1]) 


columnName = []

for n in sys.argv[2:]:
	print (n)
	columnNames.append(n)
	
for i in columnName:
	encodeColumn=df[i]
	#creating labelEncoder
	le = preprocessing.LabelEncoder()

	# Converting string labels into numbers.
	encodedData=le.fit_transform(encodeColumn)

print(encodedData)
