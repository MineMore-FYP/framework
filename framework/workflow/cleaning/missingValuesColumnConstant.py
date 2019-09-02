import pandas as pd
import numpy as np
from collections import OrderedDict 
from dataType import *

df = pd.read_csv("/home/amanda/FYP/testcsv/cleanedDataset.csv")

od = OrderedDict() 
od["PID"] = 100045
od["SQ_FT"] = 1000

for col, value in od.items(): 
  if dataType(col, df) == "int":
    if type(value)== "int":
      df[col].fillna(value, inplace = True) 
  else if dataType(col, df) == "str":
    if type(value)== "str":
      df[col].fillna(value, inplace = True) 
  else if dataType(col, df) == "float":
    if type(value)== "float":
      df[col].fillna(value, inplace = True) 

df.to_csv (r'/home/amanda/FYP/testcsv/missing.csv', index = None, header=True)
