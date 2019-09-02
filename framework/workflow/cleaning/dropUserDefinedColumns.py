import pandas as pd
import numpy as np
import sys
from userScript import *

#read csv with defined missing values
missing_values = ["n/a", "na", "--"]
#url = "https://raw.githubusercontent.com/dataoptimal/posts/master/data%20cleaning%20with%20python%20and%20pandas/property%20data.csv"

df = pd.read_csv(outputDataset, na_values = missing_values)

#dropColumns list from userScript
dropCols = dropColumns

dfUserDroppedCols = df.drop(dropCols, axis=1)

dfUserDroppedCols.to_csv (outputDataset, index = False, header=True)
