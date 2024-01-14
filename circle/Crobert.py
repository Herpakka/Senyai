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
    edges_image = np.uint8(edges_image * 255)  # Convert to 8-bit unsigned integer
    return edges_image


def main(argv):
    default_file = 'E:\\Senyai-main\\Senyai-main\\circle\\Meth.png'
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
    rows = edges_image.shape[0]
    circles = cv.HoughCircles(edges_image, cv.HOUGH_GRADIENT, 1, rows / 8,
                              param1=100, param2=30,
                              minRadius=15, maxRadius=30)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        count = 0  # ตัวแปรนับจำนวนวงกลม
        for i in circles[0, :]:
            count += 1
            center = (i[0], i[1])
            # จุดศูนย์กลาง
            cv.circle(src, center, 1, (0, 0, 255), 3)
            # เส้นรอบวง
            radius = i[2]
            cv.circle(src, center, radius, (0, 255, 0), 3)
        print(count, 'circles')
    
    cv.imshow("gray", gray)
    cv.imshow("detected circles", src)
    cv.imshow("robert_edge", edges_image)
    cv.waitKey(0)

    return 0

if __name__ == "__main__":
    main(sys.argv[1:])
