#Image Processing Module 
#Task1:Access Pixels
#28/09/2020
#Laura Whelan

######### import the necessary packages: #########

import cv2
import numpy as np

from matplotlib import pyplot as plt
from matplotlib import image as image
import easygui 

######### Task #########

#1.Read in any image (this is done as direct input)
I=cv2.imread('landscape.jpg')

#2.Convert this image to YUV
YUV = cv2.cvtColor(I, cv2.COLOR_BGR2YUV)
 
#3.Exctract the Y Channel (luminance)
y=YUV[:,:,0] 
 
#4.Convert the original image to grayscale (intensity)
G = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
 
#5.Show the two on the screen using OpenCV's imshow function
cv2.imshow("Luminance", y)
cv2.imshow("Greyscale", G)
cv2.waitKey(0)
 
#6.Show the two on the screen side by side with the intensity using matplotlibs subplot function
# Showing an image on the screen (MatPlotLib):
plt.figure(1)
plt.subplot(1,2,1)
plt.imshow(y, cmap='gray')
plt.title('Luminance')
plt.xticks([])
plt.yticks([])

plt.subplot(1,2,2)
plt.imshow(G,cmap='gray')
plt.title('Grayscale')
plt.xticks([])
plt.yticks([])

plt.show()
 

