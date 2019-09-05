# binarization
from sklearn.preprocessing import Binarizer
import pandas
import numpy
import scipy
sys.path.append("..")
from dataType import *
from userScript import *

dataframe = pandas.read_csv(outputDataset, names=names)


for key, value in userDefinedBinarizeColumns.items():
    if dataType(col, df) != "str":
        #user defined threshold
        userThreshold= value[0]
        col = key

        binarizeColumn = df.filter([col], axis=1)
        df = df.drop(col, axis=1)

        array = binarizeColumn.values
        binarizer = Binarizer(threshold=userThreshold).fit(array)
        binary = binarizer.transform(array)

        df[col] = binary
    else:
        print("The column, ", col, "is of type: string. Cannot binarize")

dataframe.to_csv (outputDataset, index = False, header=True)
