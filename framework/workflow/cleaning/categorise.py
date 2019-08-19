#categorise
import pandas as pd
import numpy as np

url = "https://raw.githubusercontent.com/dataoptimal/posts/master/data%20cleaning%20with%20python%20and%20pandas/property%20data.csv"
df = pd.read_csv(url ) 

#user defined number of categories
numberOfCategories=3

pd.cut(np.array([1, 7, 5, 4, 6, 3]), numberOfCategories)
