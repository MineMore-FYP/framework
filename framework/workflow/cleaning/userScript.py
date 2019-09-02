
from collections import OrderedDict
#Workflow

#input dataset location
inputDataset = "/home/amanda/FYP/testcsv/test.csv"

#specify output locatiion
outputDataset = "/home/amanda/FYP/testcsv/cleanedDataset.csv"

#Drop unique columns
#Drop one value columns

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
interpolateColumns = ["whatever"] #if interpolateColumns = "all", all int columns

#or option of interpolating all int cols

#mode for user defined columns

#binning/encoding/categorising

#transformation

#mining
#which algorithms to use. and relevant params

#knowledge presentation
