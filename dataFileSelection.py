import os
import glob
import pandas as pd

path = '/Users/rajiniwijayawardana/Desktop/dataFileSelection'
os.chdir(path)

allFiles = os.listdir()

print(os.name)

##allFiles = glob.glob(path + "/*.CSV")

print(allFiles)

if os.name == 'nt':
    import win32api, win32con
def file_is_hidden(p):
    if os.name== 'nt':
        attribute = win32api.GetFileAttributes(p)
        return attribute & (win32con.FILE_ATTRIBUTE_HIDDEN | win32con.FILE_ATTRIBUTE_SYSTEM)
    else:
        return p.startswith('.') #linux-osx

fileList = [filename for filename in os.listdir('.') if not file_is_hidden(filename)]
print(fileList)

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
    print(filename)
    filenameMonth=filename[4:6]
    if filenameMonth == desiredMonth:          
        selectedFiles.append(filename)

print(selectedFiles)

for filename in selectedFiles:
##    print(filename.replace(path + "\\", ''))
    #combine all files in the list
    combined_csv = pd.concat([pd.read_csv(filename, delimiter = "\t") for filename in allFiles])


##export to csv
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')
