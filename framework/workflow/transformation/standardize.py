# Standardize data (0 mean, 1 stdev)
from sklearn.preprocessing import StandardScaler
import pandas
import numpy
import scipy

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
dataframe = pandas.read_csv(url)

array = dataframe.values

scaler = StandardScaler().fit(array)
standardized = scaler.transform(array)

# summarize transformed data
numpy.set_printoptions(precision=3)
print(standardized[0:5,:])

#last two lines for printing first six rows. change as required to output CSV.