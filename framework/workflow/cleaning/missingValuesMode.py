import pandas as pd
import numpy as np
import statistics

sys.path.append("..")
from userScript import *
from dataType import *

df = pd.read_csv(outputDataset)
#********************************** WHAT HAPPENS WHEN MODE IS NAN *************************************************************************
colNames = modeColumns

for col in colNames:
	modeOfCol = statistics.mode(df[col])
	if (modeOfCol!= "NaN"):
		df[col].fillna(modeOfCol, inplace = True)
	else:
		print("Can't fill with mode. The mode of ", col, " is NaN")

df.to_csv (outputDataset, index = False, header=True)
