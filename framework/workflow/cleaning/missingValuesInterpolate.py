import pandas as pd
import numpy as np
sys.path.append("..")
from dataType import *
from userScript import *


df = pd.read_csv(outputDataset)

if(interpolateColumns == "all"):
    #Interpolate all integer columns
    colNames = list(df)
else:
    #Interpolate user defined columns
    colNames = interpolateColumns

for col in colNames:
    if dataType(col, df) != "str":
        # to interpolate the missing values
        df[col] = df[col].interpolate(method ='linear', limit_direction ='forward')
    else:
        #print("The column, ", col, "is of type: string. Cannot interpolate")


df.to_csv (outputDataset, index = None, header=True)
