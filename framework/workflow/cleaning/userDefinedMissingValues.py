import pandas as pd
sys.path.append("..")
from userScript import *

missing_values = missingValues

#read csv with defined missing values
df = pd.read_csv(outputDataset, na_values = missing_values)
df.to_csv (outputDataset, index = False, header=True)
