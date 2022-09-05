#!/usr/bin/env python3
# NOTE: Every dimension used here is of the form (width,height) rather than (height,width)!

__version__ = "0.2.0"

import argparse
from imreco import converter, resizer

def parse_arguments():
    parser = argparse.ArgumentParser(
        prog="imreco",
        description=f"Resizing and Conversion of images. ({__version__})",
        formatter_class=lambda prog: argparse.HelpFormatter(prog,max_help_position=30)
    )
    parser.add_argument("function", help="Resize or Convert")
    parser.add_argument("-s", "--size", help="Diamensions to new File", required=False)
    parser.add_argument("-i", "--input", help="Input file")
    parser.add_argument("-o", "--output", help="Output file")
    return parser.parse_args()

def main():
    args = parse_arguments()

    if args.function == "resize":
        resizer.Resizer(args.input, args.output).resize(args.size)
    elif args.function == "convert":
        converter.Converter(args.input, args.output).convert()
    else:
        print("Function not supported! Try resize/convert")

if __name__ == "__main__":
    main()

