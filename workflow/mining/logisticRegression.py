import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn import preprocessing
from sklearn import utils

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression 

from sklearn import metrics
from sklearn.metrics import confusion_matrix 

from sklearn.metrics import accuracy_score 

from matplotlib.backends.backend_pdf import PdfPages

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import userScript

dataset = pd.read_csv(userScript.outputDataset,engine = 'python')

df = pd.DataFrame(dataset)
#print(df)

header = list(df)
#print(list(df))

pp = PdfPages('plot_logisticRegression.pdf')
for i in header:
    for j in header:
        if(i != j):
            X = dataset[i].values.reshape(-1,1)
            y = dataset[j].values.reshape(-1,1)

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
            
            #training
            regressor = LogisticRegression(C=1.0, solver='lbfgs', multi_class='ovr')
            regressor.fit(X_train, y_train.ravel()) 

            y_pred = regressor.predict(X_test)

            df = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})

            #confusion matrix
            cm = confusion_matrix(y_test, y_pred) 
            print ("Confusion Matrix : \n", cm) 
            
            #accuracy
            print ("Accuracy : ", accuracy_score(y_test, y_pred))

            plt.scatter(X_test, y_test,  color='gray')
            plt.xlabel(i)
            plt.ylabel(j)
            plt.plot(X_test, y_pred, color='red', linewidth=2)
            plt.savefig(pp, format='pdf')
            plt.close()
pp.close()
