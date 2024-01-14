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

def prewitt(image):
    kernelx = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
    kernely = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    img_prewittx = cv2.filter2D(img_gaussian, -1, kernelx)
    img_prewitty = cv2.filter2D(img_gaussian, -1, kernely)
    edges_image = img_prewittx + img_prewitty
    return edges_image

image = mpimg.imread("road.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
img_gaussian = cv2.GaussianBlur(gray_image,(3,3),0)

#
edges_image = prewitt(image)

rho_resolution = 1
theta_resolution = np.pi / 360
threshold = 100  # Adjust as needed
min_line_length = 100  # Adjust as needed
max_line_gap = 5  # Adjust as needed

hough_linesP = cv2.HoughLinesP(edges_image, rho_resolution, theta_resolution, threshold,
                              minLineLength=min_line_length, maxLineGap=max_line_gap)

hough_linesP_image = np.zeros_like(image)
draw_lines(hough_linesP_image, hough_linesP)
original_image_with_hough_linesP = weighted_img(hough_linesP_image, image)

plt.title("prewitt")
plt.imshow(original_image_with_hough_linesP, cmap='gray')
plt.show()
