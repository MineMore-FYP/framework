#encoding
import pandas as pd
import numpy as np
import sys
sys.path.append("..")
from dataType import *
from userScript import *
# Import LabelEncoder
from sklearn import preprocessing

df = pd.read_csv(outputDataset)

columnNames = userDefinedEncodeColumns

for col in columnNames:
    encodeColumn=df[col].astype(str)
    #creating labelEncoder
    le = preprocessing.LabelEncoder()
    # Converting string labels into numbers.
    encodedData=le.fit_transform(encodeColumn)

    df = df.drop(col, axis=1)

    df[col] = encodedData

    print(encodedData)

df.to_csv (outputDataset, index = False, header=True)
