import os
from PyPDF2 import PdfFileReader, PdfFileWriter

def PDFWatermark(source_file, watermark):
    template = PdfFileReader(open(source_file, 'rb'))
    watermark = PdfFileReader(open(watermark, 'rb'))
    output = PdfFileWriter()

    for i in range(template.getNumPages()):
        page = template.getPage(i)
        page.mergePage(watermark.getPage(0))
        output.addPage(page)

    with open(source_file, 'wb') as file:
        output.write(file)