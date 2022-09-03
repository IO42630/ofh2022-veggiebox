import os
import pandas as pd



print(os.getcwd())
os.chdir('./data')


file = 'WochenübersichtMV_2022.xlsx'
data = pd.ExcelFile(file)
print(data.sheet_names) #this returns the all the sheets in the excel file

