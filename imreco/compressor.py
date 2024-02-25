import cv2 as cv

class Compressor:

    def __init__(self, input, output) -> None:
        self.input = input
        self.output = output

    def compress(self, quality=80):
        try:
            img = cv.imread(self.input)
            cv.imwrite(self.output, img, [int(cv.IMWRITE_JPEG_QUALITY), int(quality)])
        except Exception as e:
            print(f"Error compressing the file!\n{e}")
