import cv2
from matplotlib import pyplot as plt


def histogram(input_img):
    img = cv2.imread(input_img)
    # CONVERTING TO GRAYSCALE
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # DISPLAYING ORIGINAL AND GRAYSCALE IMAGE
    # plt.subplot(2, 2, 1)
    # plt.imshow(img)
    # plt.subplot(2, 2, 2)
    # plt.imshow(gray)
    # plt.show()

    # APPLYING GAUSSIAN FILTER
    fig_size = 9
    image = cv2.GaussianBlur(gray, (fig_size, fig_size), 0)

    # DISPLAYING IMAGE AFTER GAUSSIAN FILTERING
    cv2.imshow("Gaussian filtered IMAGE", image)

    # Using Opencv to Calculate Histogram
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    return hist


Path = input("Enter image path: ")
result = histogram(Path)
plt.plot(result)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
