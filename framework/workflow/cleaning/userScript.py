#Cleaning workflow
#Drop unique columns
#Drop one value columns

#Drop user defined cols
#user defined column array
dropColumns = ["Actor2Geo_FullName", "ActionGeo_FullName"]

#drop columns according to user defined empty value percentage
maxPercentageOfMissingColValues = 20

#drop user defined rows
dropFromColumn = ["Actor1Name"]
dropRows = ["BRAZIL", "UNITED STATES"]

#drop rows according to user defined empty value percentage
maxPercentageOfMissingRowValues = 20

#remove duplicate rows

#missing value interpolation
interpolateColumns = ["whatever"]
#or option of interpolating all int cols
