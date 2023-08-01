import cv2
import matplotlib.pyplot as plt
import numpy as np

def image1():
    image=cv2.imread("pythonImageProcessing/pandas.jpg",cv2.IMREAD_COLOR)
    cv2.imshow("image",image)
    cv2.waitKey(0) #Hold the screen untill user close it 
    cv2.destroyAllWindows() # remove/delete GUI window from screen memory

def image2():
    image=cv2.imread("pythonImageProcessing/pandas.jpg")
    plt.imshow(image)
    plt.waitforbuttonpress() # remove/delete GUI window from screen memory
    plt.close('all')

def image3():
    image=cv2.imread("pythonImageProcessing/pandas.jpg",cv2.IMREAD_GRAYSCALE)
    plt.imshow(image)
    plt.waitforbuttonpress() # remove/delete GUI window from screen memory
    plt.close('all')

def image4():
    image=cv2.imread("pythonImageProcessing/pandas.jpg",cv2.IMREAD_REDUCED_GRAYSCALE_2)
    plt.imshow(image)
    plt.waitforbuttonpress() # remove/delete GUI window from screen memory
    plt.close('all')
    
image = cv2.imread('pythonImageProcessing/pandas.jpg')
B, G, R = cv2.split(image) 
    
def image5():
    cv2.imshow("blue",R)
    cv2.waitKey(0)
    

#image1()
#image2()
#image3()
#image4()
image5()