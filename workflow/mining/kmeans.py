import pandas as pd
import csv
from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import userScript

# making data frame from csv file

data = pd.read_csv(userScript.outputDataset,engine = 'python')
df = pd.DataFrame(data)
##print(df)
header = list(df)
##print(list(df))
pp = PdfPages('plot_Kmeans.pdf')
for i in header:
    for j in header:
        if(i != j):
            dfin = DataFrame(data,columns=[i,j])
            X = dfin.values
            kmeans = KMeans(n_clusters=3).fit(X)
            centroids = kmeans.cluster_centers_
            print("x axis: "+i + " , y axis: " + j)
            print(centroids)
            print("\n")

            plt.scatter(X[:,0], X[:,1], c= kmeans.labels_, cmap='rainbow')
            plt.xlabel(i)
            plt.ylabel(j)
            plt.scatter(centroids[:, 0], centroids[:, 1], c='black')
            plt.savefig(pp, format='pdf')
            plt.close()
pp.close()
