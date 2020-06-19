import os

def PDFParseName(filename):
    if not os.path.splitext(filename)[1] == '.pdf':
        return "".join((filename, '.pdf'))
    return filename