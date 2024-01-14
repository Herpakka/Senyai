import sys
import cv2 as cv
import numpy as np

def main(argv):
    default_file = r'E:\Senyai-main\Senyai-main\line\road.jpg'
    filename = argv[0] if len(argv) > 0 else default_file
    # Loads an image
    src = cv.imread(cv.samples.findFile(filename), cv.IMREAD_COLOR)
    # Check if image is loaded fine
    if src is None:
        print('Error opening image!')
        print(f'Usage: canny.py [image_name -- default {default_file}] \n')
        return -1

    # Convert to grayscale
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

    # Apply Gaussian Blur
    blur = cv.GaussianBlur(gray, (9, 9), 2)

    # Apply Canny edge detection
    edges_image = cv.Canny(blur, 0, 67)
    print(edges_image)  # Convert to 8-bit unsigned integer

    # Use Hough Line Transform to detect lines
    lines = cv.HoughLinesP(edges_image, 1, np.pi/180, 80, minLineLength=60, maxLineGap=15)

    # Draw the lines on the original image
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv.line(src, (x1, y1), (x2, y2), (0, 0, 255), 2)

    cv.imshow("blur", blur)
    cv.imshow("gray", gray)
    cv.imshow("canny_edges", edges_image)
    cv.imshow("detected lines", src)
    cv.waitKey(0)

    return 0

if __name__ == "__main__":
    main(sys.argv[1:])
