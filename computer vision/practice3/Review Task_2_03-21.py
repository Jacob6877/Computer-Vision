# Otsu Threshold of soccer for Red Channel Image: 113.0
# Otsu Threshold of rose for Gray Image: 79.0
# Otsu Threshold of rose for Red Channel Image: 112.0

import cv2 as cv

# Read the image
img = cv.imread('soccer.jpg', cv.IMREAD_COLOR)  # Read the image in BGR format
img2 = cv.imread('rose.png', cv.IMREAD_COLOR)  # Read the image in BGR format
if img is None:
    print("File not found")

# Convert the image to grayscale
gray_img2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

# Extract the red channel
red_channel_img = img[:, :, 2]  # BGR channels are 0, 1, 2, here extracting the red channel    
red_channel_img2 = img2[:, :, 2]  # BGR channels are 0, 1, 2, here extracting the red channel    

# Apply thresholding
ret, thresh1 = cv.threshold(img, 128, 255, cv.THRESH_BINARY)
ret2, thresh2 = cv.threshold(red_channel_img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

print('Otsu Threshold of soccer for Red Channel Image:', ret2)

ret3, thresh3 = cv.threshold(gray_img2, 128, 255, cv.THRESH_BINARY+ cv.THRESH_OTSU)
ret4, thresh4 = cv.threshold(red_channel_img2, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

print('Otsu Threshold of rose for Gray Image:', ret3)
print('Otsu Threshold of rose for Red Channel Image:', ret4)

# Display images
titles = ['Original Image1', 'img1_Binary128', 'img1_Otsu','Original Image2', 'img2_Binary128', 'img2_Otsu']
images = [img, thresh1, thresh2,img2, thresh3, thresh4]

for i in range(6):
    cv.imshow(titles[i], images[i])

cv.waitKey(0)  # Wait for a key press, 0 means infinite wait
cv.destroyAllWindows()
