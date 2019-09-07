import pandas as pd
import numpy as np
import statistics

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import dataType
import userScript

df = pd.read_csv(sys.argv[1])
#********************************** WHAT HAPPENS WHEN MODE IS NAN *************************************************************************
colNames = userScript.modeColumns

for col in colNames:
	modeOfCol = statistics.mode(df[col])
	if (modeOfCol!= "NaN"):
		df[col].fillna(modeOfCol, inplace = True)
	else:
		print("Can't fill with mode. The mode of ", col, " is NaN")

df.to_csv (sys.argv[1], index = False, header=True)
