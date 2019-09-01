import pandas as pd
import numpy as np
from dataType import *


df = pd.read_csv("/home/amanda/FYP/testcsv/cleanedDataset.csv")
colNames = list(df)

#Interpolate integer columns
#********************************** Check what the weird codes in int columns are in the GDELT dataset ************************************
#********************************** CAN MAKE THIS USER DEFINED? ***************************************************************************



for col in colNames:
    if dataType(col, df) == "int":
        # to interpolate the missing values
        df[col] = df[col].interpolate(method ='linear', limit_direction ='forward')



df.to_csv (r'/home/amanda/FYP/testcsv/missing.csv', index = None, header=True)
