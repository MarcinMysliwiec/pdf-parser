import os
from PyPDF2 import PdfFileMerger

def PDFCombine(source_folder, destination_full_path):
    merger = PdfFileMerger()
    for filename in os.listdir(source_folder):
        if os.path.splitext(filename)[1] != '.pdf':
            continue
        source_full_path = os.path.join(source_folder, filename)
        print('Appending: ' + source_full_path)
        merger.append(source_full_path)
    merger.write(destination_full_path)