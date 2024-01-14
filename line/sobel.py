import sys
import cv2 as cv
import numpy as np

# ฟังก์ชัน sobel
def sobel(image):
    gray_image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    cv.imshow("gray_image", gray_image)  # ขาวดำ
    img_sobelx = cv.Sobel(gray_image, cv.CV_8U, 1, 0, ksize=3)  # kernel แกนx
    img_sobely = cv.Sobel(gray_image, cv.CV_8U, 0, 1, ksize=3)  # kernel แกนy
    edges_image = img_sobelx + img_sobely  # convolution
    return edges_image  # return ตัวแปรที่ convo 

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
    edges_image = sobel(src)  # หาขอบแบบcanny

    # หาวงกลม
    lines = cv.HoughLinesP(edges_image, 1, np.pi/180, 80 ,minLineLength=80, maxLineGap=1)


    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv.line(src, (x1, y1), (x2, y2), (0, 0, 255), 2)
    

    cv.imshow("detected circles", src)
    cv.imshow("sobel_edge",edges_image)
    cv.waitKey(0)

    return 0


if __name__ == "__main__":
    main(sys.argv[1:])