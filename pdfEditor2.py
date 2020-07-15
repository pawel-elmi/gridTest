from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.pdf import PageObject

def merge4():
    frame       = PdfFileReader(open("pliki testowe/frame.pdf" , "rb"))
    title       = PdfFileReader(open("pliki testowe/title.pdf", "rb"))
    conditions  = PdfFileReader(open("pliki testowe/conditions.pdf", "rb"))
    # tab         = PdfFileReader(open("pliki testowe/tab2.pdf", "rb"))
    tab         = PdfFileReader(open("tableOut.pdf", "rb"))

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


if __name__ == '__main__':
    merge4()