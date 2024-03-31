import cv2 as cv
import sys
# read image 
gray_img = cv.imread('Erica.jpg', cv.IMREAD_GRAYSCALE)
# change it into color
color_img = cv.cvtColor(gray_img, cv.COLOR_GRAY2BGR)

# Enter student id
cv.putText(color_img, '2021054466', (10,550), cv.FONT_HERSHEY_SIMPLEX, 
            1.5, (0,255,0), 1)

def draw(event,x,y,flags,param):
    global ix, iy;
    
    if event == cv.EVENT_LBUTTONDOWN:
        ix,iy=x,y
    elif event == cv.EVENT_LBUTTONUP:
        cv.rectangle(color_img,(ix,iy),(x,y),(255,0,255),2)
    cv.imshow('Result', color_img)
    
cv.namedWindow('Result')
cv.setMouseCallback('Result',draw)


while(True):
    cv.imshow('Result',color_img)
    
    key = cv.waitKey(1)& 0xFF
    if key == 27:
        break

cv.imwrite('Task1_2021054466.jpg', color_img)

cv.destroyAllWindows()