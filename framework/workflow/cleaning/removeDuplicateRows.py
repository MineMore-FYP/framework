import pandas as pd
import numpy as np
import sys
sys.path.append("..")
from userScript import *


df = pd.read_csv(outputDataset)


dfDroppedDuplicates = df.drop_duplicates()
dfDroppedDuplicates.reset_index(inplace=True)

dfDroppedDuplicates.to_csv (outputDataset, index = False, header=True)
