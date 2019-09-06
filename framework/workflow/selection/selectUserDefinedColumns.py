import pandas as pd
import os.path
import sys
sys.path.append("..")

from userScript import *

df = pd.read_csv(inputDataset)

if (selectColumns != "all"):
    dfConcat = pd.DataFrame()

    for i in selectColumns:
        df_i=df[i]
        dfAfterUserSelectedColumns=pd.concat([dfConcat, df_i], axis=1)
        dfConcat=dfAfterUserSelectedColumns

    dfAfterUserSelectedColumns.to_csv (outputDataset, index = False, header=True)

else:
    df.to_csv (outputDataset, index = False, header=True)
