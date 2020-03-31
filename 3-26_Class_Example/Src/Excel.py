'''
Created on Mar 31, 2020

@author: jakeluebbe
'''

from openpyxl import load_workbook
wb = load_workbook(filename = 'empl.xlsx')
sheet = wb['Sheet1']
print(sheet['A1'].value), print(sheet['A2'].value)
print(sheet['B1'].value), print(sheet['B2'].value)
print(sheet['C1'].value), print(sheet['C2'].value)

wb.close()
