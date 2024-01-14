import matplotlib.pyplot as plt
import numpy as np
import cv2
from scipy import ndimage

# Function to draw lines on the image
def draw_lines(img, houghLinesP, color=[255, 0, 0], thickness=2):
    Lcount = 0
    for line in houghLinesP:
        Lcount += 1
        x1, y1, x2, y2 = line[0]
        cv2.line(img, (x1, y1), (x2, y2), color, thickness)
    print(Lcount,'lines')

# Function to blend two images
def weighted_img(img, initial_img, α=0.8, β=1., λ=0.):
    return cv2.addWeighted(initial_img, α, img, β, λ)

# Roberts Cross edge detection
def roberts_cross_edge_detection(image):
    roberts_cross_v = np.array([[1, 0], [0, -1]])
    roberts_cross_h = np.array([[0, 1], [-1, 0]])

    vertical = ndimage.convolve(image, roberts_cross_v)
    horizontal = ndimage.convolve(image, roberts_cross_h)

    edges_image = np.sqrt(np.square(horizontal) + np.square(vertical))
    edges_image = np.uint8(edges_image * 255)  # Convert to 8-bit unsigned integer
    return edges_image

# Load the image
image = cv2.imread("road.jpg", 0).astype('float64')
image /= 255

# Roberts Cross edge detection
edges_image = roberts_cross_edge_detection(image)

# Parameters for HoughLinesP
rho_resolution = 1
theta_resolution = np.pi / 180
threshold = 1150  # Adjust as needed
min_line_length = 10  # Adjust as needed
max_line_gap = 5  # Adjust as needed

# Apply Probabilistic Hough Transform
hough_linesP = cv2.HoughLinesP(edges_image, rho_resolution, theta_resolution, threshold,
                               minLineLength=min_line_length, maxLineGap=max_line_gap)

# Draw lines on a black image
hough_linesP_image = np.zeros_like(image)
draw_lines(hough_linesP_image, hough_linesP)

# Blend the original image with the image containing Hough lines
original_image_with_hough_linesP = weighted_img(hough_linesP_image, image)

# Display the result
# plt.figure(figsize=(30, 20))
# plt.subplot(131)
# plt.imshow(image)
# plt.subplot(132)
# plt.imshow(edges_image, cmap='gray')
# plt.subplot(133)
plt.imshow(original_image_with_hough_linesP)
plt.show()

