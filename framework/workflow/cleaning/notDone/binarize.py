# binarization
from sklearn.preprocessing import Binarizer
import pandas
import numpy

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
dataframe = pandas.read_csv(url, names=names)

array = dataframe.values

noOfColumns = df.shape[1]
noOfRows = df.shape[0]
print(noOfColumns)
print(noOfRows)

# separate array into input and output components
X = array[:,0:noOfColumns-1]
Y = array[:,noOfColumns-1]

#user defined threshold
userThreshold = 0.0

binarizer = Binarizer(threshold=userThreshold).fit(X)
binaryX = binarizer.transform(X)

# summarize transformed data
numpy.set_printoptions(precision=3)
print(binaryX[0:5,:])
