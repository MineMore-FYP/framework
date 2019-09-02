#AMANDA : delete after done. for reference only. I fixed the file "selectUserDefinedColumns.py" like you've done

import pandas as pd
from userScript import *

#AMANDA:not outputDataset here? since selection is the very first step
df = pd.read_csv(outputDataset)

#columns=["PID", "SQ_FT"] AMANDA : To be taken from the user script

dfConcat = pd.DataFrame()

for i in columns:
  df_i=df[i]
  dfAfterUserSelectedColumns=pd.concat([dfConcat, df_i], axis=1)
  dfConcat=dfAfterUserSelectedColumns
 
#AMANDA: outputDataset
dfAfterUserSelectedColumns.to_csv (outputDataset, index = False, header=True)
