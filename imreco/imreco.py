#!/usr/bin/env python3
"""Every diamension used here is of the form (width,height) rather than (height,width)!"""
import argparse
import cv2 as cv
import os

parser = argparse.ArgumentParser(prog="imreco", description="Resize or Convert images")
parser.add_argument("function", help="Resize or Convert")
parser.add_argument("-s", "--size", help="Diamensions to new File", required=False)
parser.add_argument("-i", "--input", help="Input file")
parser.add_argument("-o", "--output", help="Output file")
args = parser.parse_args()

def resize():
    width, height = map(int, args.size.split("x"))

    img = cv.imread(args.input)
    old_w, old_h, _ = img.shape
    filename = os.path.basename(args.input)

    resized = cv.resize(img, (width, height), interpolation=cv.INTER_AREA)
    cv.imwrite(f"./resized_{filename}", resized)

    print(f"Resizing from ({old_w}, {old_h}) to ({width}, {height})")
    print(f"Output saved as resized_{filename}!")

def convert():
    old_format = args.input.split(".")[-1]
    img = cv.imread(args.input)
    cv.imwrite(args.output, img)
    new_format = args.output.split(".")[-1]

    print(f"Converted {old_format} to {new_format}")

def main():
    if args.function == "resize":
        resize()
    elif args.function == "convert":
        convert()
    else:
        print("Function not supported! Try resize/convert")

if __name__ == "__main__":
    main()
