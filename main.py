#!/usr/bin/env python3
import cv2 as cv

def show_image(img):
    cv.imshow("image", resized)
    cv.waitKey(0)
    cv.destroyAllWindows()

img = cv.imread("./assets/test.jpg")
print(f"Image shape: {img.shape}")

resized = cv.resize(img, (600, 600), interpolation=cv.INTER_AREA)
print(f"Resized shape: {resized.shape}")

show_image(resized)

