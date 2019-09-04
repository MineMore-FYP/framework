# Rescale data (between 0 and 1)
import pandas
import scipy
import numpy
from sklearn.preprocessing import MinMaxScaler

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
df = pandas.read_csv(url)

array = df.values

scaler = MinMaxScaler(feature_range=(0, 1))
rescaled = scaler.fit_transform(array)

# summarize transformed data
numpy.set_printoptions(precision=3)
print(rescaled[0:5,:])

#last two lines for printing first six rows. change as required to output CSV.