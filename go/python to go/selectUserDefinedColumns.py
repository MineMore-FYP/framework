import pandas as pd
import os.path
import sys
from csv import reader

df = reader(sys.argv[1])
selectedColumns = ["GOLBALEVENTID"]

df1 = df[selectedColumns]

df1.to_csv ("/home/amanda/FYP/testcsv/clean.csv", index = False, header=True)

