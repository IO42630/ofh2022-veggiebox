import os
import pandas as pd
import openpyxl


print(os.getcwd())
os.chdir('./data')


fileName = 'WochenübersichtMV_2022.xlsx'
data = pd.ExcelFile(fileName)
print(data.sheet_names) #this returns the all the sheets in the excel file

workbook = openpyxl.load_workbook(fileName)
worksheet1= workbook.worksheets[0]

for row in range(2, worksheet1.max_row + 1):
    test = worksheet1['B' + str(row)].value
    br = 0
