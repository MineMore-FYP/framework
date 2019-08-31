import pandas as pd
import numpy as np
import sys

df = pd.read_csv(sys.argv[1])

for col in df.columns:
    if len(df[col].unique()) == 1:
        df.drop(col,inplace=True,axis=1)

dfUniqueColumnsDropped.to_csv (r'/home/amanda/FYP/testcsv/cleanedDataset.csv', index = None, header=True)
