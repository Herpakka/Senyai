import sys
import cv2 as cv
import numpy as np

# ฟังก์ชัน prewitt
def prewitt(image):
    gray_image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    cv.imshow("gray", gray_image)
    Hx = np.array([[-1, 0, 1],[-1, 0, 1],[-1, 0, 1]])
    Hy = np.array([[-1, -1, -1],[0, 0, 0],[1, 1, 1]])
    pre_x = cv.filter2D(gray_image, -1, Hx) / 8.0
    pre_y = cv.filter2D(gray_image, -1, Hy) / 8.0
    #calculate the gradient magnitude of vectors
    pre_out = np.sqrt(np.power(pre_x, 2) + np.power(pre_y, 2))
    # mapping values from 0 to 255
    pre_out = (pre_out / np.max(pre_out)) * 255
    return pre_out.astype(np.uint8)

def main(argv):
    default_file = r'E:\Senyai-main\Senyai-main\line\road.jpg'
    filename = argv[0] if len(argv) > 0 else default_file
    # Loads an image
    src = cv.imread(cv.samples.findFile(filename), cv.IMREAD_COLOR)
    # Check if image is loaded fine
    if src is None:
        print('Error opening image!')
        print('Usage: hough_circle.py [image_name -- default ' + default_file + '] \n')
        return -1

    # สี > ขาวดำ > เบลอ > binary(canny)
    
    edges_image = prewitt(src)  # หาขอบแบบcanny
   
    # หาวงกลม
    lines = cv.HoughLinesP(edges_image, 1, np.pi/180, 60 ,minLineLength=180, maxLineGap=2)

    # Draw the lines on the original image
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv.line(src, (x1, y1), (x2, y2), (0, 0, 255), 2)

    
    cv.imshow("detected circles", src)
    cv.imshow("prewitt_edge",edges_image)
    cv.waitKey(0)

    return 0


if __name__ == "__main__":
    main(sys.argv[1:])