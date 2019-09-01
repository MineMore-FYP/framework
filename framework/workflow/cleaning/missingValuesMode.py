import pandas as pd
import numpy as np
import statistics
from dataType import *

df = pd.read_csv("/home/amanda/FYP/testcsv/cleanedDataset.csv")
#********************************** WHAT HAPPENS WHEN MODE IS NAN *************************************************************************
colNames = ["ActionGeo_CountryCode", "EventCode"]

for col in colNames:
	modeOfCol = statistics.mode(df[col])
	df[col].fillna(modeOfCol, inplace = True) 


df.to_csv (r'/home/amanda/FYP/testcsv/missing.csv', index = None, header=True)
