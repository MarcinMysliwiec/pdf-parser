import os
import sys
import argparse

from default import default
from pathlib import Path

from PDF.Combine import PDFCombine
from PDF.Watermark import PDFWatermark
from PDF.ParseName import PDFParseName

def main(args):
    source_folder = Path(args.source_folder) if args.source_folder else default["SOURCE_FOLDER"]
    destination_folder = Path(args.destination_folder) if args.destination_folder else default["DEST_FOLDER"]
    output_filename = args.output_filename if args.output_filename else default["FILENAME"]

    # Create output folder if does not exists
    if not Path(destination_folder).exists():
        Path(destination_folder).mkdir()


    # Check if user provided valid output name
    output_filename = PDFParseName(output_filename)
    destination_full_path = str(Path(destination_folder, output_filename))

    # print('Saving file: ' + str(destination_full_path))
    PDFCombine(source_folder, destination_full_path)
    if args.watermark:
        PDFWatermark(destination_full_path, args.watermark)
    print('File saved!')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Merge directory filled with PDFs')

    parser.add_argument('--source-folder', help='Source folder with PDFs. Default ')
    parser.add_argument('--destination-folder', help='Desired destination folder. Default ' + str(default["SOURCE_FOLDER"]))
    parser.add_argument('--output-filename', help='Desired output filename. Default ' + str(default["FILENAME"]))
    parser.add_argument('--watermark', help='Add watermark for your new pdf. No watermark if empty')

    # Take parameters from terminal command execution
    args = parser.parse_args()
    sys.exit(main(args))