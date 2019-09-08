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

numOfRows = df.shape[0]

for col in df.columns:
    if len(df[col].unique()) == numOfRows:
        df.drop(col,inplace=True,axis=1)

if(userScript.modeColumns == "all"):
    #Interpolate all integer columns
    colNames = list(df)
else:
    #Interpolate user defined columns
    colNames = userScript.modeColumns

df2 = df
df1 = pd.DataFrame()
for col in colNames:

	#if (modeOfCol!= "NaN"):

	df1 = df[col].dropna()
	print(col)
	modeOfCol = statistics.mode(df1[col])
	df2[col].fillna(modeOfCol, inplace = True)
	#else:
	print("Can't fill with mode. The mode of ", col, " is", modeOfCol)

df2.to_csv (sys.argv[1], index = False, header=True)
