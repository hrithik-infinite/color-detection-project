import cv2
# import numpy as np
# import pandas as pd


# Function to detect mouse click(double) as well as assign the R,G,B values to variables
def mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)


# The input image can be o different sizes sothis function resizes the image to a given width/height maintaing the aspect ratio.

def resizewithratio(img, width = None, height = None, inter = cv2.INTER_AREA):
    dim = None
    (h,w) = img.shape[:2]

    if width is None and height is None:
        return img
    if width is None:
        r = height/float(h)
        dim = (int(w*r),height)
    else:
        r = width/float(w)
        dim = (width,int(h*r))
    return cv2.resize(img,dim,interpolation= inter)



imgs = cv2.imread('img2.jpeg')  #Read the image
img = resizewithratio(imgs,width = 700) #resize to width of 700 pixels


clicked = False # default values of click is false
r = g = b = xpos = ypos = 0 # global declaration and assignment of variables 


# print(img.shape)


while(1):
    
    # cv2.resizeWindow("Color Recognition App",400,400)
    cv2.namedWindow('Color Recognition App') #Creating the image window
    cv2.setMouseCallback('Color Recognition App', mouse_click) #mousecallback executed when mouse event takes place
    cv2.imshow("Color Recognition App",img) #show the loaded image
    
    if (clicked): 
        cv2.rectangle(img,(0,20), (600,60), (b,g,r), -1) #draw rectange 
        text = ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b) + ' HEXCODE = '+ '#%02x%02x%02x' % (r, g, b) #fill rectange with R,G,B values and HEXCODE of color

        
        cv2.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA) # fill with text
        if(r+g+b>=600): #if color is light then display with black color
            cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
            
        clicked=False # reset click to false
    if cv2.waitKey(20) & 0xFF ==27: # ESC key to breakout of loop
        break
cv2.destroyAllWindows()