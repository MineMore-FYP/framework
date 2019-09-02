import pandas as pd
import numpy as np
import sys
from userScript import *

df = pd.read_csv(outputDataset)

for col in df.columns:
    if len(df[col].unique()) == 1:
        df.drop(col,inplace=True,axis=1)

df.to_csv (outputDataset, index = False, header=True)
