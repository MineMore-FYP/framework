import os
from collections import OrderedDict
#Workflow

dirpath = os.getcwd()
print(dirpath)

#input   location
inputDataset = "/home/amanda/FYP/testcsv/test.csv"

#specify output locatiion
outputDataset = "/home/amanda/FYP/testcsv/cleanedDataset.csv"

#SELECTION
#select columns
selectColumns = "all" #if "all" select everything. else give a list ["whatever1", "whatever2"]

#select rows
selectFromRow = OrderedDict()
selectFromRow['Actor1Name'] = ["BRAZIL", "UNITED STATES"]


#Drop unique columns
#Drop one value columns


#user defined missing values
missingValues = ["n/a", "na", "--"]

#Drop user defined cols
#user defined column array
dropColumns = ["Actor2Geo_FullName", "ActionGeo_FullName"]

#drop columns according to user defined empty value percentage
userDefinedColPercentage = 20

#drop user defined rows
dropFromRow = OrderedDict()
dropFromRow['Actor1Name'] = ["BRAZIL", "UNITED STATES"]
dropFromRow['Actor2Name'] = ["PAKISTAN"]
#print (dropFromRow['Actor1Name'][0])


#drop rows according to user defined empty value percentage
userDefinedRowPercentage = 20

#remove duplicate rows


#missing value interpolation
interpolateColumns = "all" #if interpolateColumns = "all", all int columns, else give a list

#mode for user defined columns
modeColumns = ["ActionGeo_CountryCode", "EventCode"]

#fill missing value with a constant
missingValueCons = OrderedDict()
missingValueCons["PID"] = 100045
missingValueCons["SQ_FT"] = 1000

#binning/encoding/categorising

#transformation

#mining
#which algorithms to use. and relevant params

#knowledge presentation
