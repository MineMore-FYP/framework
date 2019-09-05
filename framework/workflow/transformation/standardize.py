# Standardize data (0 mean, 1 stdev)
from sklearn.preprocessing import StandardScaler
import pandas
import numpy
import scipy
import sys
sys.path.append("..")
from dataType import *
from userScript import *


dataframe = pandas.read_csv(inputDataset)

colNames = userDefinedStandardizeColumns

for col in colNames:
    if dataType(col, df) == "int":
        standardizeColumn = dataframe.filter([col], axis=1)
        dataframe = dataframe.drop(col, axis=1)

        array = standardizeColumn.values
        scaler = StandardScaler().fit(array)
        standardized = scaler.transform(array)
        dataframe[col] = standardized
    else:
        print("The column, ", col, "is not of type: integer. Cannot standardize")

dataframe.to_csv (outputDataset, index = False, header=True)
