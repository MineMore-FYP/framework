# Rescale data (between 0 and 1)
import pandas
import scipy
import numpy
from sklearn.preprocessing import MinMaxScaler


url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
df = pandas.read_csv(url)

array = df.values

noOfColumns = df.shape[1]
noOfRows = df.shape[0]
print(noOfColumns)
print(noOfRows)

# separate array into input and output components
X = array[:,0:noOfColumns-1]
Y = array[:,noOfColumns-1]

scaler = MinMaxScaler(feature_range=(0, 1))
rescaledX = scaler.fit_transform(X)

# summarize transformed data
numpy.set_printoptions(precision=3)
print(rescaledX[0:5,:])
