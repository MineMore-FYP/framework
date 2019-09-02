import pandas as pd
import numpy as np
import sys
from userScript import *

#user defined missing values
missing_values = ["n/a", "na", "--"]

df = pd.read_csv(outputDataset, na_values = missing_values)

numOfColumns = len(df.columns)
#user defined percentage
maxPercentageOfMissingValues= userDefinedRowPercentage
threshold = (numOfColumns * maxPercentageOfMissingValues)/100


df = df.dropna(thresh=threshold)
df.to_csv (outputDataset, index = None, header=True)
