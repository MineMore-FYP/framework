import pandas as pd
import numpy as np
import sys
sys.path.append("..")
from userScript import *

df = pd.read_csv(outputDataset)

#dropColumns list from userScript
dropCols = dropColumns

dfUserDroppedCols = df.drop(dropCols, axis=1)

dfUserDroppedCols.to_csv (outputDataset, index = False, header=True)
