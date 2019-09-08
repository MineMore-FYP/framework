import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as seabornInstance
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import userScript

dataset = pd.read_csv(sys.argv[1],engine = 'python')

df = pd.DataFrame(dataset,columns=userScript.selectedColumns2)
##print(df)
header = list(df)
##print(list(df))

for i in header:
    for j in header:
        if(i != j):
            X = dataset[i].values.reshape(-1,1)
            y = dataset[j].values.reshape(-1,1)

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

            regressor = LinearRegression()
            regressor.fit(X_train, y_train) #training the algorithm

            #To retrieve the intercept:
            print(regressor.intercept_)
            #For retrieving the slope:
            print(regressor.coef_)

            y_pred = regressor.predict(X_test)

            df = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})

            print(df)

            print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
            print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
            print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

            plt.scatter(X_test, y_test,  color='gray')
            plt.plot(X_test, y_pred, color='red', linewidth=2)
            plt.savefig("D:/FYP/ds/plots/"+ i + "-" + j + ".png")
