# Rescale data (between 0 and 1)
import pandas
import scipy
import numpy
from sklearn.preprocessing import MinMaxScaler
sys.path.append("..")
from dataType import *
from userScript import *

df = pandas.read_csv(outputDataset)

for key, value in userDefinedRescaleColumns.items():
    if dataType(col, df) != "str":
        lowerBound = value[0]
        upperBound = value[1]
        col = key
        scaler = MinMaxScaler(feature_range=(lowerBound, upperBound))

        rescaleColumn = df.filter([col], axis=1)
        df = df.drop(col, axis=1)

        array = rescaleColumn.values
        rescaled = scaler.fit_transform(array)

        df[col] = rescaled
    else:
        print("The column, ", col, "is of type: string. Cannot rescale")

dataframe.to_csv (outputDataset, index = False, header=True)
