#!/usr/bin/env python3
import cv2 as cv

def show_image(img):
    cv.imshow("image", img)
    # Wait for a key to destroy the preview window.
    cv.waitKey(0)
    cv.destroyAllWindows()


# reading the image file (returns numpy array)
img = cv.imread("./assets/test.jpg")
print(f"Image shape: {img.shape}")

# (width, height) tuple
resized = cv.resize(img, (600, 600), interpolation=cv.INTER_AREA)
print(f"Resized shape: {resized.shape}")


if __name__ == "__main__":
    show_image(resized)
