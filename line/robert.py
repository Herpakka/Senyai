import sys
import cv2 as cv
import numpy as np
from scipy import ndimage

# ฟังก์ชัน robert
def robert(image):
    roberts_cross_v = np.array([[1, 0], [0, -1]])
    roberts_cross_h = np.array([[0, 1], [-1, 0]])

    image = image.astype('float64') / 255.0
    vertical = ndimage.convolve(image, roberts_cross_v)
    horizontal = ndimage.convolve(image, roberts_cross_h)

    edges_image = np.sqrt(np.square(horizontal) + np.square(vertical))
    edges_image = np.uint8(edges_image * 255)
    print(edges_image)  # Convert to 8-bit unsigned integer
    return edges_image


def main(argv):
    default_file = r'E:\Senyai-main\Senyai-main\line\road.jpg'
    filename = argv[0] if len(argv) > 0 else default_file
    # Loads an image
    src = cv.imread(cv.samples.findFile(filename), cv.IMREAD_COLOR)
    # Check if the image is loaded fine
    if src is None:
        print('Error opening image!')
        print('Usage: hough_circle.py [image_name -- default ' + default_file + '] \n')
        return -1

    # Convert to grayscale
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

    # Apply Roberts Cross edge detection
    edges_image = robert(gray)
    # หาวงกลม
    lines = cv.HoughLinesP(edges_image, 1, np.pi/180, 100 ,minLineLength=180, maxLineGap=0.4)


    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv.line(src, (x1, y1), (x2, y2), (0, 0, 255), 2)
    
    cv.imshow("gray", gray)
    cv.imshow("detected circles", src)
    cv.imshow("robert_edge", edges_image)
    cv.waitKey(0)

    return 0

if __name__ == "__main__":
    main(sys.argv[1:])
