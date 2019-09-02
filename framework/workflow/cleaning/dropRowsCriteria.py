import pandas as pd
import numpy as np
import sys
from userScript import *

df = pd.read_csv(outputDataset)

numOfColumns = len(df.columns)
#user defined percentage
maxPercentageOfMissingValues= userDefinedRowPercentage
threshold = (numOfColumns * maxPercentageOfMissingValues)/100


df = df.dropna(thresh=threshold)
df.to_csv (outputDataset, index = False, header=True)
