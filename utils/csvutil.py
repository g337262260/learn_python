#! python3

"""
   #:处理csv文件
   #: Guowei
"""

import csv


def readCsvFile(fileName):
    csvFile = open(fileName)
    csvReader = csv.reader(csvFile)
    # 生成一个list
    # csvData = list(csvReader)
    # print(csvData.__repr__())
    # 打印
    csvRows = []
    for row in csvReader:
        print('Row #' + str(csvReader.line_num) + '  ' + str(row))
        csvRows.append(row)
    print(csvRows.__repr__())

def writeCsvFile(filename):
    outputFile = open(filename,'w',newline='')
    # param1 :分隔单元格
    # param2 :设置行距
    outputWriter = csv.writer(outputFile, delimiter='\t', lineterminator='\n\n')

    outputWriter.writerow(['a','b','c','d'])
    outputWriter.writerow(['1','2','3','4'])

    outputFile.close()


if __name__ == '__main__':
    readCsvFile('example.csv')
    # writeCsvFile('output.csv')