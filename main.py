import argparse
import os

from PDF.Combine import PDFCombine
from PDF.Watermark import PDFWatermark
from PDF.ParseName import PDFParseName

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Merge directory filled with PDFs')

    parser.add_argument('source_folder', help='Source folder with PDFs')
    parser.add_argument('output_filename', help='Desired output filename')
    parser.add_argument('--destination-folder', help='Default value=output.')
    parser.add_argument('--watermark', help='Add watermark for your new pdf.')

    # Take parameters from terminal command execution
    args = parser.parse_args()
    source_folder = args.source_folder
    output_filename = args.output_filename
    destination_folder = args.destination_folder if args.destination_folder else 'output'

    # Create output folder if does not exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Check if user provided valid output name
    output_filename = PDFParseName(output_filename)
    destination_full_path = os.path.join(destination_folder, output_filename)

    print('Saving file: ' + destination_full_path)
    PDFCombine(source_folder, destination_full_path)
    if args.watermark:
        PDFWatermark(destination_full_path, args.watermark)
    print('File saved!')
