import pandas as pd
import csv
from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
##import os,sys,inspect
##currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
##parentdir = os.path.dirname(currentdir)
##sys.path.insert(0,parentdir)
##
##import userScript

# making data frame from csv file
data = pd.read_csv("D:/FYP/ds/outputDataset.csv",engine = 'python')

df = pd.DataFrame(data)
##print(df)
header = list(df)
##print(list(df))

for i in header:
    for j in header:
        if(i != j):
            dfin = DataFrame(data,columns=[i,j])
            X = dfin.to_numpy()
            kmeans = KMeans(n_clusters=3).fit(X)
            centroids = kmeans.cluster_centers_
            print("x axis: "+i + " , y axis: " + j)
            print(centroids)
            print("\n")

            #plt.scatter(df[i], df[j], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
            plt.scatter(X[:,0], X[:,1], c= kmeans.labels_, cmap='rainbow')
            plt.xlabel(i)
            plt.ylabel(j)
            #plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
            plt.scatter(centroids[:, 0], centroids[:, 1], c='black')
            plt.savefig("D:/FYP/ds/plots/"+ i + "-" + j + ".png")
