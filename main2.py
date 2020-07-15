# pdf_merging.py
import PyPDF2 

from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.pdf import PageObject

import pdfkit


# pdfkit.from_file('http://10.113.11.15:8080/static/main-window/index.html', 'pliki testowe/localhost.pdf') 

# pdfkit.from_url('http://10.113.11.15:8080/', 'pliki testowe/angularz.pdf') 
# pdfkit.from_url('http://www.elmi.pl/oferta.html', 'pliki testowe/localhost2.pdf') 

# paths = [   
#             'pliki testowe/title.pdf',
#             'pliki testowe/conditions.pdf',
#             'pliki testowe/tab1.pdf',
#             'pliki testowe/tab.pdf',
#         ]

paths = {
    "frame": "pliki testowe/frame.pdf",
    "title": "pliki testowe/title.pdf",
    "conditions": "pliki testowe/conditions.pdf",
    "tab": "pliki testowe/tab2.pdf",
    "tab_inns": "pliki testowe/tab_inns.pdf"
}

def merge_pdfs(paths, output):
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF
    with open(output, 'wb') as out:
        pdf_writer.write(out)

def merge2():
        # Open the files that have to be merged one by one
    pdf1File = open('pliki testowe/r1', 'rb')
    pdf2File = open('pliki testowe/w1.pdf', 'rb')
    pdf3File = open('pliki testowe/tit1.pdf', 'rb')

    
    # Read the files that you have opened
    pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
    pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
    pdf3Reader = PyPDF2.PdfFileReader(pdf3File)

    
    # Create a new PdfFileWriter object which represents a blank PDF document
    pdfWriter = PyPDF2.PdfFileWriter()
    
    # Loop through all the pagenumbers for the first document
    for pageNum in range(pdf1Reader.numPages):
        pageObj = pdf1Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    
    # Loop through all the pagenumbers for the second document
    for pageNum in range(pdf2Reader.numPages):
        pageObj = pdf2Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    
    # Now that you have copied all the pages in both the documents, write them into the a new document
    pdfOutputFile = open('pliki testowe/MergedFiles.pdf', 'wb')
    pdfWriter.write(pdfOutputFile)
    
    # Close all the files - Created as well as opened
    pdfOutputFile.close()
    pdf1File.close()
    pdf2File.close()

def merge3():

    reader = PdfFileReader(open('pliki testowe/r1.pdf','rb'))
    invoice_page = reader.getPage(0)
    sup_reader = PdfFileReader(open('pliki testowe/w1.pdf','rb'))
    sup_page = sup_reader.getPage(0)  # We pick the second page here

    translated_page = PageObject.createBlankPage(None, sup_page.mediaBox.getWidth(), sup_page.mediaBox.getHeight())
    translated_page.mergeScaledTranslatedPage(sup_page, 1, 0, -400)  # -400 is approximate mid-page

    translated_page.mergePage(invoice_page)

    writer = PdfFileWriter()
    writer.addPage(translated_page)

    with open('pliki testowe/out.pdf', 'wb') as f:
        writer.write(f)

def openFiles(paths):
    for path in paths:
        pdf_reader = PdfFileReader(open(path))
    
def merge4():
    frame       = PdfFileReader(open("pliki testowe/frame.pdf" , "rb"))
    title       = PdfFileReader(open("pliki testowe/title.pdf", "rb"))
    conditions  = PdfFileReader(open("pliki testowe/conditions.pdf", "rb"))
    # tab         = PdfFileReader(open("pliki testowe/tab2.pdf", "rb"))
    tab         = PdfFileReader(open("out.pdf", "rb"))

    # tab_inns    = PdfFileReader(open("pliki testowe/tab_inns.pdf", "rb"))

    output = PdfFileWriter()

    page = frame.getPage(0) #frame
    page.mergeScaledTranslatedPage(tab.getPage(0), 1.38, -7, -780, expand=False) #
    page.mergeTranslatedPage(conditions.getPage(0), 0, -320, expand=False) #
    page.mergeTranslatedPage(title.getPage(0), 0, -70, expand=False) #

    # tabToBeScaled = tab.getPage(0)
    # tabToBeScaled = tabToBeScaled.scale(1.25,1.25)
    # page.mergeTranslatedPage(tabToBeScaled, 0, -450, expand=False) #
    # page.mergeTranslatedPage(tab_inns.getPage(0), 0, -470, expand=False) #

    output.addPage(page)

    outputStream = open("document2.pdf", "wb")
    output.write(outputStream)
    outputStream.close()

def getPdfContents():
    # page = PdfFileReader(open(paths[4], 'rb')).getPage(0)
    text  = page.getDocumentInfo()
    # plik.getPage(0)
    # plikObj = PageObject(plik)
    # getContents()
    print(text)

if __name__ == '__main__':
    # print(paths["frame"])
    # paths = ['pliki testowe/ramka elmi.pdf', 'pliki testowe/sku-61.2020-m2- wycinek3.pdf']
    # merge_pdfs(paths, output='pliki testowe/merged.pdf')
    merge4()
    