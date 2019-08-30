# Standardize data (0 mean, 1 stdev)
from sklearn.preprocessing import StandardScaler
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

scaler = StandardScaler().fit(X)
rescaledX = scaler.transform(X)

# summarize transformed data
numpy.set_printoptions(precision=3)
print(rescaledX[0:5,:])
