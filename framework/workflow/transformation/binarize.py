# binarization
from sklearn.preprocessing import Binarizer
import pandas
import numpy
import scipy

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
dataframe = pandas.read_csv(url, names=names)

array = dataframe.values

#user defined threshold
userThreshold = 0.0

binarizer = Binarizer(threshold=userThreshold).fit(array)
binary = binarizer.transform(array)

# summarize transformed data
numpy.set_printoptions(precision=3)
print(binary[0:5,:])

#last two lines for printing first six rows. change as required to output CSV.
