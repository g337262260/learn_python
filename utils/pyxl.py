#! python3

"""
    #: 操作excel的脚本
    #：待完善

"""

import openpyxl,pprint
import xlrd
import os
import json
import PyPDF2


def openxlsx():
    print('Opening workbook')
    wb = xlrd.open_workbook('android.xlsx')
    sheet = wb.sheet_by_name('sheet1')
    print('Reading workbook')
    data = {}
    for i in range(1,sheet.nrows):
        rows = sheet.row_values(i)
        datalist = []
        for cell in rows:
            datalist.append(cell)
            print(type(cell))
        data[str(rows[1])] = datalist
    print('Writing results')
    resultFile = open('data.txt','w')
    resultFile.write(json.dumps(data))
    resultFile.close()
    print('Done')

if __name__ == '__main__':
    openxlsx()