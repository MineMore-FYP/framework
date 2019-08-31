import pandas as pd
import numpy as np
import sys

df = pd.read_csv(sys.argv[1])
numOfRows = df.shape[0]

for col in df.columns:
    if len(df[col].unique()) == numOfRows:
        df.drop(col,inplace=True,axis=1)

df.to_csv (r'/home/amanda/FYP/testcsv/cleanedDataset.csv', index = None, header=True)
