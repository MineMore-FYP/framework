##simple kmeans
##import csv
##import pandas as pd
##from pandas import DataFrame
##import matplotlib.pyplot as plt
##from sklearn.cluster import KMeans
##
####Data = {'x': [25,34,22,27,33,33,31,22,35,34,67,54,57,43,50,57,59,52,65,47,49,48,35,33,44,45,38,43,51,46],
####        'y': [79,51,53,78,59,74,73,57,69,75,51,32,40,47,53,36,35,58,59,50,25,20,14,12,20,5,29,27,8,7]
####       }
##data = pd.read_csv('D:/FYP/ds/combined.csv', engine = 'python')
##
##
##df = DataFrame(data,columns=['EventBaseCode','GoldsteinScale'])
##  
##kmeans = KMeans(n_clusters=3).fit(df)
##centroids = kmeans.cluster_centers_
##print(centroids)
##
##plt.scatter(df['EventBaseCode'], df['GoldsteinScale'], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
##plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
##plt.show()
##


import pandas as pd
import csv
from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


# making data frame from csv file 
data = pd.read_csv("D:/FYP/ds/combined.csv",engine = 'python') 
  
# dropping passed columns - manual
data_new = data.drop(["GLOBALEVENTID","SQLDATE","MonthYear","Year","FractionDate","Actor1Code","Actor1Name","Actor1CountryCode","Actor1KnownGroupCode","Actor1EthnicCode","Actor1Religion1Code",
           "Actor1Religion2Code","Actor1Type1Code","Actor1Type2Code","Actor1Type3Code","Actor2Code","Actor2Name","Actor2CountryCode","Actor2KnownGroupCode",
           "Actor2EthnicCode","Actor2Religion1Code","Actor2Religion2Code","Actor2Type1Code","Actor2Type2Code","Actor2Type3Code","Actor1Geo_FullName",
           "Actor1Geo_CountryCode","Actor1Geo_ADM1Code","Actor1Geo_Lat","Actor1Geo_Long","Actor1Geo_FeatureID","Actor2Geo_FullName","Actor2Geo_CountryCode",
           "Actor2Geo_ADM1Code","Actor2Geo_Lat","Actor2Geo_Long","Actor2Geo_FeatureID","ActionGeo_Type","ActionGeo_FullName","ActionGeo_CountryCode","ActionGeo_ADM1Code",
           "ActionGeo_Lat","ActionGeo_Long","ActionGeo_FeatureID","DATEADDED","SOURCEURL","Actor1Geo_Type","Actor2Geo_Type"], axis = 1, inplace = True) 

df = pd.DataFrame(data_new,columns=["IsRootEvent","EventCode","EventBaseCode","EventRootCode","QuadClass","GoldsteinScale","NumMentions","NumSources","NumArticles",
                                "AvgTone"])

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
        
        

##plt.scatter(df['EventBaseCode'], df['GoldsteinScale'], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
##plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
##plt.show()


