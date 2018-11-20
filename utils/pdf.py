#! python3

"""
    #: 操作pdf的脚本
    #：待完善

"""
import PyPDF2
import sys

def readPdf():
    pdfFile = open('gonghang.pdf','rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    print('PDF page:'+str(pdfReader.numPages))

    pageobj = pdfReader.getPage(2)
    print(pageobj.extractText())

def combinePdf():
    print(sys.argv)
    pdfFile1 = open(sys.argv[1], 'rb')
    pdfReader1 = PyPDF2.PdfFileReader(pdfFile1)
    pdfFile2 = open(sys.argv[2], 'rb')
    pdfReader2 = PyPDF2.PdfFileReader(pdfFile2)

    pdfWriter = PyPDF2.PdfFileWriter()
    for pageNum in range(pdfReader1.numPages):
        pageobj = pdfReader1.getPage(pageNum)
        pdfWriter.addPage(pageobj)
    for pageNum in range(pdfReader2.numPages):
        pageobj = pdfReader2.getPage(pageNum)
        pdfWriter.addPage(pageobj)

    pdfcombineFile = open(sys.argv[3],'wb')
    pdfWriter.write(pdfcombineFile)
    pdfcombineFile.close()
    pdfFile1.close()
    pdfFile2.close()
    print('Done....')

combinePdf()