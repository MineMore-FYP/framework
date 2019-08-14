import pandas as pd
import csv
from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np


# making data frame from csv file 
data = pd.read_csv("D:/FYP/ds/combined.csv",engine = 'python') 
  
df = pd.DataFrame(data,columns=['IsRootEvent','EventCode','EventBaseCode','EventRootCode','QuadClass','GoldsteinScale','NumMentions','NumSources','NumArticles',
                                'AvgTone'])
##print(df)
header = list(df)
##print(list(df))

for i in header:
    for j in header:
        if(i != j):
            dfin = DataFrame(data,columns=[i,j])
            kmeans = KMeans(n_clusters=3).fit(dfin)
            centroids = kmeans.cluster_centers_
            print("x axis: "+i + " , y axis: " + j)
            print(centroids)
            print("\n")
            plt.scatter(df[i], df[j], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
            plt.xlabel(i)
            plt.ylabel(j)
            plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
            plt.savefig("D:/FYP/ds/plots/"+ i + "-" + j + ".png")
