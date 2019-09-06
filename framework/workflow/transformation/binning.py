#Binning for integer features:
import pandas as pd
import numpy as np
sys.path.append("..")
from dataType import *
from userScript import *

df = pd.read_csv(outputDataset)
columnNames = userDefinedBinningColumns

for col in columnNames:
    #df_no_missing = data[colName].dropna()
    binArray = np.array([])

    for row in df_no_missing:
       intValue = int(row)
       binArray = np.append(binArray, intValue)

    binArray[0]
    #pd.cut(np.array([.2, 1.4, 2.5, 6.2, 9.7, 2.1]), 3, retbins=True)
    #pd.cut(np.ones(5), 4, labels=False)

    pd.cut(binArray, 3, labels=["0", "1","2"])

    #drop na already done by this stage.
