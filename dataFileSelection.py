import os
import glob
import pandas as pd

##File selection

selectedFiles = []

def getMonthlyFiles(m):
    if (m == "JANUARY"):
        selectMonth = "01"
    elif (m == "FEBRUARY"):
        selectMonth = "02"
    elif (m == "MARCH"):
        selectMonth = "03"
    elif (m == "APRIL"):
        selectMonth = "04"
    elif (m == "MAY"):
        selectMonth = "05"
    elif (m == "JUNE"):
        selectMonth = "06"
    elif (m == "JULY"):
        selectMonth = "07"
    elif (m == "AUGUST"):
        selectMonth = "08"
    elif (m == "SEPTEMBER"):
        selectMonth = "09"
    elif (m == "OCTOBER"):
        selectMonth = "10"
    elif (m == "NOVEMBER"):
        selectMonth = "11"
    elif (m == "DECEMBER"):
        selectMonth = "12"
    return selectMonth

#def getAnnualFiles(m):

#def getDateRangeFiles(m):
            
#def getDayOfTheWeekFiles(m):

userMonth = "JULY"

for filename in fileList:
    desiredMonth = getMonthlyFiles(userMonth)
    print(filename + "- " + desiredMonth)
    filenameMonth=filename[4:6]
    print(filenameMonth)
    print(filenameMonth == desiredMonth)
    if filenameMonth == desiredMonth:          
        selectedFiles.append(filename)

print(selectedFiles)
