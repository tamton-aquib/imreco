import cv2 as cv

class Converter:
    def __init__(self, input, output) -> None:
        self.input = input
        self.output = output
        self.output = self.output

    def convert(self):
        old_format = self.input.split(".")[-1]
        img = cv.imread(self.input)
        cv.imwrite(self.output, img)
        new_format = self.output.split(".")[-1]

        print(f"Converted {old_format} to {new_format}")
