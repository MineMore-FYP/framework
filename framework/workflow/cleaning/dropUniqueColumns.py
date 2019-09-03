import pandas as pd
import numpy as np
import sys
import os.path


os.chdir('..')
PATH = os.getcwd()

sys.path.append(PATH)

from userScript import *


df = pd.read_csv(outputDataset)
numOfRows = df.shape[0]

for col in df.columns:
    if len(df[col].unique()) == numOfRows:
        df.drop(col,inplace=True,axis=1)

df.to_csv(outputDataset, index = False, header=True)
