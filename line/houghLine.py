import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

def draw_lines(img, houghLinesP, color=[0, 255, 0], thickness=2):
    for line in houghLinesP:
        x1, y1, x2, y2 = line[0]
        cv2.line(img, (x1, y1), (x2, y2), color, thickness)

def weighted_img(img, initial_img, α=0.8, β=1., λ=0.):
    return cv2.addWeighted(initial_img, α, img, β, λ)

image = mpimg.imread("road.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
blurred_image = cv2.GaussianBlur(gray_image, (9, 9), 0)
edges_image = cv2.Canny(blurred_image, 50, 120)

rho_resolution = 1
theta_resolution = np.pi / 180
threshold = 50  # Adjust as needed
min_line_length = 100  # Adjust as needed
max_line_gap = 50  # Adjust as needed

hough_linesP = cv2.HoughLinesP(edges_image, rho_resolution, theta_resolution, threshold,
                              minLineLength=min_line_length, maxLineGap=max_line_gap)

hough_linesP_image = np.zeros_like(image)
draw_lines(hough_linesP_image, hough_linesP)
original_image_with_hough_linesP = weighted_img(hough_linesP_image, image)

# plt.figure(figsize=(30, 20))
# plt.subplot(131)
# plt.imshow(image)
# plt.subplot(132)
# plt.imshow(edges_image, cmap='gray')
# plt.subplot(133)
plt.imshow(original_image_with_hough_linesP, cmap='gray')
plt.show()
