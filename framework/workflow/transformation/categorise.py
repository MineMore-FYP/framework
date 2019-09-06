#categorise
import pandas as pd
import numpy as np
sys.path.append("..")
from dataType import *
from userScript import *

#done on integers to categorise into ranges


df = pd.read_csv(outputDataset)

#user defined number of categories
numberOfCategories=3

pd.cut(np.array([1, 7, 5, 4, 6, 3]), numberOfCategories)
