## multiple classes
#Import scikit-learn dataset library
from sklearn import datasets
#Import knearest neighbors Classifier model
from sklearn.neighbors import KNeighborsClassifier
#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics
# Import train_test_split function
from sklearn.model_selection import train_test_split
import pandas as pd
#import csv
##from pandas import DataFrame
import matplotlib.pyplot as plt

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import userScript

# making data frame from csv file 
df = pd.read_csv(userScript.outputDataset,engine = 'python')

targetColumnName = userScript.targetColumnName
targetColumn = userScript.targetColumn
y = df[targetColumnName].values#test
X = df.drop(targetColumn,axis=1)


#Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=1, stratify=y) # 80% training and 20% test

###Create KNN Classifier - see the results by changing no of neigbours
knn = KNeighborsClassifier(n_neighbors=userScript.numberOfneighbours)

###Train the model using the training sets
knn.fit(X_train, y_train)

###Predict the response for test dataset
y_pred = knn.predict(X_test)

### Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

##knn.score(X_test, y_test)
