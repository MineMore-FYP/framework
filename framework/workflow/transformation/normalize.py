# Normalize data (length of 1)
from sklearn.preprocessing import Normalizer
import pandas
import numpy

dataframe = pandas.read_csv(outputDataset)

array = dataframe.values

noOfColumns = df.shape[1]
noOfRows = df.shape[0]
print(noOfColumns)
print(noOfRows)

# separate array into input and output components
X = array[:,0:noOfColumns]

scaler = Normalizer().fit(X)
normalizedX = scaler.transform(X)

# summarize transformed data
numpy.set_printoptions(precision=3)
print(normalizedX[0:5,:])
