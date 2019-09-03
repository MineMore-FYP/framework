import pandas as pd
import numpy as np
from dataType import *
sys.path.append("..")
from userScript import *


df = pd.read_csv(outputDataset)

if(interpolateColumns == "all"):
    #Interpolate all integer columns
    colNames = list(df)
else:
    #Interpolate user defined columns
    colNames = interpolateColumns

for col in colNames:
    if dataType(col, df) == "int":
        # to interpolate the missing values
        df[col] = df[col].interpolate(method ='linear', limit_direction ='forward')


df.to_csv (outputDataset, index = None, header=True)
