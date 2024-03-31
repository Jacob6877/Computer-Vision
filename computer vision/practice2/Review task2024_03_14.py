import cv2
import numpy as np

# Load the image
image = cv2.imread('Erica.jpg')

if image is None:
    print('File not found')

# Step 1: Scale down the size of the image to 50%
pic1 = cv2.resize(image, None, fx=0.5, fy=0.5)

# Step 2: Convert the image to HSV color model
hsv_image = cv2.cvtColor(pic1, cv2.COLOR_BGR2HSV)

# Step 2a: Change the hue to 180 degrees
pic2 = np.copy(hsv_image)
pic2[:, :, 0] = (pic2[:, :, 0] + 90) % 180

# Step 3: Decrease the saturation by 50%
pic3 = np.copy(hsv_image)
pic3[:, :, 1] = np.clip(0.5 * pic3[:, :, 1], 0, 255).astype(np.uint8)

# Step 4: Increase the value by 50%
pic4 = np.copy(hsv_image)
pic4[:, :, 2] = np.clip(1.5 * pic4[:, :, 2], 0, 255).astype(np.uint8)

# Convert the images back to BGR for display and saving
pic2 = cv2.cvtColor(pic2, cv2.COLOR_HSV2BGR)
pic3 = cv2.cvtColor(pic3, cv2.COLOR_HSV2BGR)
pic4 = cv2.cvtColor(pic4, cv2.COLOR_HSV2BGR)

# Step 5: Merge 2x2 images
top_row = np.hstack((pic1, pic2))
bottom_row = np.hstack((pic3, pic4))
merged_image = np.vstack((top_row, bottom_row))

# Save the merged image
cv2.imwrite('erica_new1.jpg', merged_image)

# Display the merged image
cv2.imshow('Merged Image', merged_image)
cv2.waitKey(0)
cv2.destroyAllWindows()