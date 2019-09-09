##import pandas as pd
##import numpy as np
##from sklearn.model_selection import train_test_split
##from sklearn.preprocessing import StandardScaler
##from sklearn.ensemble import RandomForestRegressor
##from sklearn import metrics
##
##dataset = pd.read_csv('D:/FYP/ds/combined.csv',engine = 'python')
##
##dataset.head()
##
##df = pd.DataFrame(data,columns=['IsRootEvent','EventCode','EventBaseCode','EventRootCode','QuadClass','GoldsteinScale','NumMentions','NumSources','NumArticles',
##                                'AvgTone'])
##
##X = df.iloc[:, 0:4].values
##y = df.iloc[:, 4].values
##
##X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
##
##sc = StandardScaler()
##X_train = sc.fit_transform(X_train)
##X_test = sc.transform(X_test)
##
##regressor = RandomForestRegressor(n_estimators=20, random_state=0)
##regressor.fit(X_train, y_train)
##y_pred = regressor.predict(X_test)
##
##print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
##print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
##print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
##


# Importing the libraries 
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 

data = pd.read_csv('D:/FYP/ds/combined.csv')
data.drop(["GLOBALEVENTID","SQLDATE","MonthYear","Year","FractionDate","Actor1Code","Actor1Name","Actor1CountryCode","Actor1KnownGroupCode","Actor1EthnicCode","Actor1Religion1Code",
           "Actor1Religion2Code","Actor1Type1Code","Actor1Type2Code","Actor1Type3Code","Actor2Code","Actor2Name","Actor2CountryCode","Actor2KnownGroupCode",
           "Actor2EthnicCode","Actor2Religion1Code","Actor2Religion2Code","Actor2Type1Code","Actor2Type2Code","Actor2Type3Code","Actor1Geo_FullName",
           "Actor1Geo_CountryCode","Actor1Geo_ADM1Code","Actor1Geo_Lat","Actor1Geo_Long","Actor1Geo_FeatureID","Actor2Geo_FullName","Actor2Geo_CountryCode",
           "Actor2Geo_ADM1Code","Actor2Geo_Lat","Actor2Geo_Long","Actor2Geo_FeatureID","ActionGeo_Type","ActionGeo_FullName","ActionGeo_CountryCode","ActionGeo_ADM1Code",
           "ActionGeo_Lat","ActionGeo_Long","ActionGeo_FeatureID","DATEADDED","SOURCEURL"], axis = 1, inplace = True) 

print(data) 

x = data.iloc[:, 1:11].values 
print(x) 
y = data.iloc[:, 12].values
print(y)

# Fitting Random Forest Regression to the dataset 
# import the regressor 
##from sklearn.ensemble import RandomForestRegressor 
##
### create regressor object 
##regressor = RandomForestRegressor(n_estimators = 100, random_state = 0) 
##
### fit the regressor with x and y data 
##regressor.fit(x, y) 
##
##
##y_pred = regressor.predict(6.5) # test the output by changing values 
##
### Visualising the Random Forest Regression results 
##
### arange for creating a range of values 
### from min value of x to max 
### value of x with a difference of 0.01 
### between two consecutive values 
##X_grid = np.arange(min(x), max(x), 0.01) 
##
### reshape for reshaping the data into a len(X_grid)*1 array, 
### i.e. to make a column out of the X_grid value				 
##X_grid = X_grid.reshape((len(X_grid), 1)) 
##
### Scatter plot for original data 
##plt.scatter(x, y, color = 'blue') 
##
### plot predicted data 
##plt.plot(X_grid, regressor.predict(X_grid), 
##		color = 'green') 
##plt.title('Random Forest Regression') 
##plt.xlabel('Position level') 
##plt.ylabel('Salary') 
##plt.show()
##
##
