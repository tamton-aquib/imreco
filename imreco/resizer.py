import cv2 as cv
import os

class Resizer:
    def __init__(self, input, size) -> None:
        self.input = input

    def resize(self, size):
        width, height = map(int, size.split("x"))

        img = cv.imread(self.input)
        old_w, old_h, _ = img.shape
        filename = os.path.basename(self.input)

        resized = cv.resize(img, (width, height), interpolation=cv.INTER_AREA)
        cv.imwrite(f"./resized_{filename}", resized)

        print(f"Resizing from ({old_w}, {old_h}) to ({width}, {height})")
        print(f"Output saved as resized_{filename}!")

