import cv2 as cv
import numpy as np
'''
print(cv.version.opencv_version)
image = cv.imread('1.jpg')
print(type(image))

cv.imshow('My Numpy Image', image)
cv.waitKey(0)

from PIL import Image
img = Image.open('1.jpg')
print(type(img))

img = np.asarray(img)
print(type(img))

img2 = Image.fromarray(img)
img2.show('Image')

print(image.shape)
image = cv.resize(image, (600, 600))
#cv.imshow('Image', image)
#cv.waitKey(0)

image[:, :, 1] = 0
image[:, :, 2] = 0
#cv.imshow('Updated Image', image)
#cv.waitKey(0)

green = image[:, :, 0]
print(green.shape)
#cv.imshow('Red Image', red)
#cv.waitKey(0)

from matplotlib import pyplot as plt
fig, ax = plt.subplots( nrows=1, ncols=1 )  # create figure & 1 axis
histr = cv.calcHist([image],[0],None,[64],[0,256])
#print(histr)
print(histr.shape)
print(np.sum(histr))
print(600*600)
ax.plot(histr)
#plt.show()
fig.savefig('check123.jpg')

img = cv.imread('water_coins.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(green,0,255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
cv.imshow('Thresholded', thresh)
cv.waitKey(0)

image = cv.imread("football.jpg")
cv.imshow("Original", image)
cv.waitKey(0)
print(image.shape)

sub = image[235:278, 277:320]
#cv.imshow("Sub", sub)
#cv.waitKey(0)

image[235:278, 25:68] = sub
cv.imshow("Updated", image)
cv.waitKey(0)

image = cv.imread("123.png")
hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

# Threshold of blue in HSV space
lower_blue = np.array([35, 140, 60])
upper_blue = np.array([255, 255, 180])

# preparing the mask to overlay
mask = cv.inRange(hsv, lower_blue, upper_blue)

# The black region in the mask has the value of 0,
# so when multiplied with original image removes all non-blue regions
result = cv.bitwise_and(image, image, mask=mask)

cv.imshow('frame', image)
cv.imshow('mask', mask)
cv.imshow('result', result)
cv.waitKey(0)
'''

image1 = cv.imread("123.png")
image2 = cv.Canny(image1, 100, 200)
cv.imshow('Image', image1)
cv.imshow('Edge', image2)
cv.waitKey(0)