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
import csv
from pandas import DataFrame
import matplotlib.pyplot as plt

# making data frame from csv file 
data = pd.read_csv("D:/FYP/ds/combined.csv",engine = 'python')

df = pd.DataFrame(data,columns=['IsRootEvent','EventCode','EventBaseCode','EventRootCode','QuadClass','GoldsteinScale','NumMentions','NumSources','NumArticles',
                                'AvgTone'])

##print(type(data[0]))
X1 = df.iloc[:, 0:3].values
X2 = df.iloc[:, 5:8].values

X = pd.merge(X1, X2, how='inner')

print(X)
target = df.iloc[:, 4].values
print(target)


#Split dataset into training set and test set
##X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.3) # 70% training and 30% test
##
###Create KNN Classifier - see the results by changing no of neigbours
##knn = KNeighborsClassifier(n_neighbors=5)
##
###Train the model using the training sets
##knn.fit(X_train, y_train)
##
###Predict the response for test dataset
##y_pred = knn.predict(X_test)
##
### Model Accuracy, how often is the classifier correct?
##print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
##
