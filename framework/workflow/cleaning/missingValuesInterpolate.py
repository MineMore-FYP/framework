import pandas as pd
import numpy as np
from dataType import *


df = pd.read_csv(outputDataset)
colNames = list(df)

#Interpolate integer columns
for col in colNames:
    if dataType(col, df) == "int":
        # to interpolate the missing values
        df[col] = df[col].interpolate(method ='linear', limit_direction ='forward')



df.to_csv (r'/home/amanda/FYP/testcsv/missing.csv', index = None, header=True)
