import cv2 as cv
import sys

img = cv.imread('Erica.jpg')

if img is None:
    print('No file found')


# mouse callback function
def draw(event,x,y,flags,param):
    global ix, iy;
    
    if event == cv.EVENT_LBUTTONDOWN:
        ix,iy=x,y
    elif event == cv.EVENT_LBUTTONUP:
        cv.rectangle(img,(ix,iy),(x,y),(0,255,0),2)
    cv.imshow('Drawing a rectangle', img)
    
cv.namedWindow('Drawing a rectangle')
cv.setMouseCallback('Drawing a rectangle',draw)

while(True):
    if cv.waitKey(1)==ord('q'):
        break
cv.destroyAllWindows()

