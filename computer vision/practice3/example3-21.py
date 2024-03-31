import cv2 as cv

img = cv.imread('stddev30.jpg', cv.IMREAD_GRAYSCALE)
if img is None:
    print('File not found')
    
gImg1 = img
gImg2 = img
gImg3 = img
gImg4 = img
    
titles = ['original', 'GaussianBlur5', 'GaussianBlur9',
          'GaussianBlur15', 'GaussianBlur27']
images = [img, gImg1, gImg2, gImg3, gImg4]    
    
for i in range(5):
    cv.imshow(titles[i], images[i])
cv.waitKey()
cv.destroyAllWindows()