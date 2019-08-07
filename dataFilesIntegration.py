import os
import glob
import pandas as pd

path = 'D:/FYP/ds'
os.chdir(path)

allFiles = os.listdir()

print(allFiles)

fileList = [filename for filename in os.listdir('.')]
print(fileList)

for filename in selectedFiles:
    print(filename)
    #combine all files in the list
    combined_csv = pd.concat([pd.read_csv(filename, delimiter = "\t") for filename in selectedFiles])
    print(combined_csv)


##export to csv
#combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')
