import pandas as pd
import numpy as np
from dataType import *
sys.path.append("..")
from userScript import *

df = pd.read_csv(outputDataset)

od = missingValueCons

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

df.to_csv (outputDataset, index = False, header=True)
