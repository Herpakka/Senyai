import sys
import cv2 as cv
import numpy as np

def main(argv):
    default_file = 'Meth.png'
    filename = argv[0] if len(argv) > 0 else default_file
    # Loads an image
    src = cv.imread(cv.samples.findFile(filename), cv.IMREAD_COLOR)
    # Check if image is loaded fine
    if src is None:
        print('Error opening image!')
        print('Usage: hough_circle.py [image_name -- default ' + default_file + '] \n')
        return -1

    # สี > ขาวดำ > เบลอ > binary(canny)
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)  # ขาวดำ
    blur = cv.GaussianBlur(gray, (9, 9), 0)  # เบลอ
    edges_image = cv.Canny(blur, 50, 120)  # หาขอบแบบcanny

    # หาวงกลม
    rows = edges_image.shape[0]
    circles = cv.HoughCircles(edges_image, cv.HOUGH_GRADIENT, 1, rows / 8,
                              param1=100, param2=30,
                              minRadius=1, maxRadius=30)

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

    cv.imshow("detected circles", src)
    cv.waitKey(0)

    return 0


if __name__ == "__main__":
    main(sys.argv[1:])