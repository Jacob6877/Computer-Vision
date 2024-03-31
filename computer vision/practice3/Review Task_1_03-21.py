import cv2 as cv
import numpy as np

img = cv.imread('lenna.png', cv.IMREAD_GRAYSCALE)
if img is None:
    print("File not found")

bImg = cv.blur(img, (5,5))    

# Compute integral image
integral_img = cv.integral(img)
bImg2 = np.zeros((img.shape[0], img.shape[1]),dtype = np.float32)
# Perform box filtering using integral image
kernel_size = 5
half_kernel = kernel_size // 2
rows, cols = img.shape
for i in range(rows):
    for j in range(cols):
        x1 = max(i - half_kernel, 0)
        y1 = max(j - half_kernel, 0)
        x2 = min(i + half_kernel, rows - 1)
        y2 = min(j + half_kernel, cols - 1)
        
        area = integral_img[x2+1, y2+1] - integral_img[x1, y2+1] - integral_img[x2+1, y1] + integral_img[x1, y1]
        bImg2[i, j] = area / ((x2 - x1 + 1) * (y2 - y1 + 1))

titles = ['Original Image', 'Blurred', 'With IntegralImg']
images = [img, bImg, bImg2.astype(np.uint8)]  # Convert back to uint8 for display

for i in range(3):
    cv.imshow(titles[i], images[i])

    # Save images to default path
    cv.imwrite(titles[i] + '.png', images[i])

cv.waitKey()
cv.destroyAllWindows()