# Normalize data (length of 1)
from sklearn.preprocessing import Normalizer
import pandas
import numpy

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
dataframe = pandas.read_csv(url)

array = dataframe.values

noOfColumns = df.shape[1]
noOfRows = df.shape[0]
print(noOfColumns)
print(noOfRows)

# separate array into input and output components
X = array[:,0:noOfColumns-1]
Y = array[:,noOfColumns-1]

scaler = Normalizer().fit(X)
normalizedX = scaler.transform(X)

# summarize transformed data
numpy.set_printoptions(precision=3)
print(normalizedX[0:5,:])
