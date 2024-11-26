import cv2
import matplotlib.pyplot as plt

# Open the image
img = cv2.imread('image.png')

# Apply Canny edge detection
edges = cv2.Canny(img, 100, 200, 3, L2gradient=True)

# Save the image and display it
plt.figure()
plt.title('Canny Edge Detection')
plt.imsave('edges_output.png', edges, cmap='gray', format='png')
plt.imshow(edges, cmap='gray')
plt.show()
