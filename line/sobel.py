import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

def draw_lines(img, houghLinesP, color=[0, 255, 0], thickness=2):
    Lcount = 0
    for line in houghLinesP:
        Lcount += 1
        x1, y1, x2, y2 = line[0]
        cv2.line(img, (x1, y1), (x2, y2), color, thickness)
    print(Lcount,'lines')

def weighted_img(img, initial_img, α=0.8, β=1., λ=0.):
    return cv2.addWeighted(initial_img, α, img, β, λ)

def sobel(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    img_gaussian = cv2.GaussianBlur(gray_image, (3, 3), 0)

    img_sobelx = cv2.Sobel(img_gaussian, cv2.CV_8U, 1, 0, ksize=3)
    img_sobely = cv2.Sobel(img_gaussian, cv2.CV_8U, 0, 1, ksize=3)
    edges_image = img_sobelx + img_sobely
    return edges_image

image = mpimg.imread("road.jpg")
edges_image = sobel(image)


rho_resolution = 1
theta_resolution = np.pi / 180
threshold = 1150  # max 1196
min_line_length = 10  # Adjust as needed
max_line_gap = 5  # Adjust as needed

hough_linesP = cv2.HoughLinesP(edges_image, rho_resolution, theta_resolution, threshold,
                              minLineLength=min_line_length, maxLineGap=max_line_gap)

hough_linesP_image = np.zeros_like(image)
draw_lines(hough_linesP_image, hough_linesP)
original_image_with_hough_linesP = weighted_img(hough_linesP_image, image)

plt.title("sobel")
# plt.figure(figsize=(30, 20))
# plt.subplot(131)
# plt.imshow(image)
# plt.subplot(132)
plt.imshow(edges_image, cmap='gray')
# plt.subplot(133)
plt.imshow(original_image_with_hough_linesP, cmap='gray')
plt.show()
