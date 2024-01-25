# Import Libraries
import imageio as iio
from scipy import ndimage
from skimage import filters
from skimage.color import rgb2gray  # only needed for incorrectly saved images
from skimage.measure import regionprops
import math
import numpy as np
from PIL import Image


def array2Img(array,name=None):
    array = array.astype(np.uint8)
    Img = Image.fromarray(array)
    if(name == None):
        Img.show()
    else:
        Img.save(name)
    return Img

# The function takes an image path as input and returns the numy array
def img2Array(filename):
    img = Image.open(filename)
    array = np.asarray(img)
    return array


if __name__ == "__main__":
    # Store both images to variables
    array1 = img2Array("1.png")
    array2 = img2Array("2.png")
    # storing the row, col and layer into variables of array1
    row1, col1, layer1 = array1.shape
    # storing the row, col and layer into variables of array2
    row2, col2, layer2 = array2.shape
    # Since the images have an offset using centre of mass for alignment
    # Coordinates of Centre of mass for array1 and array2
    (X1, Y1, Z1) = (ndimage.center_of_mass( array1 ))
    (X2, Y2, Z2) = (ndimage.center_of_mass( array2 ))

    # convert into integers
    X1 = math.floor(X1)
    Y1 = math.floor(Y1)
    Z1 = math.floor(Z1)


    # Intensity values for centre of mass for Image 1 [38 53 74]

    X2 = math.floor(X2)
    Y2 = math.floor(Y2)
    Z2 = math.floor(Z2)

    # print(X1, Y1, Z1)
    # Intensity values for centre of mass for image 2 [37 49 1]
    print(array1.shape)
    print(array2.shape)
    # Creating a new array for double size
    arraydouble =  np.zeros((row2 * 2, col2 * 2)) #broadcast , layer2
    rowDouble, colDouble = arraydouble.shape #broadcast , layerDouble
    # broadcast arraydouble[0:rowDouble:2, 0:colDouble:2] = array2[0:row2, 0:col2]
    #lets fill the values using spiral
    arraydouble = arraydouble.astype(np.uint8)
    # first the value of centre+1 using (centre of double image + centre+2 double image + array1(centre)/3
    # lets first navigate to the centre of all three arrays
    #print(array1[X1][Y1])
    # the value is 36 47 77
    #print(array2[X2][Y2])
    # [38 53 74]
    #print(arraydouble[X2*2][Y2*2])
    # [38. 53. 74.]

    if rowDouble > colDouble:
        dimension = rowDouble
    else:
        dimension = colDouble
    arraydouble = np.zeros((dimension, dimension))
    x = int(dimension / 2)
    y = int(dimension / 2)
    if dimension % 2 == 0:
        x = x - 1
        y = y - 1

    value = 1
    arraydouble[x][y] = value
    value += 1
    for i in range(dimension):
        if i % 2 == 0:
            for j in range(0, i):
                y -= 1
                arraydouble[x][y] = value
                value += 1
            for k in range(0, i):
                x -= 1
                arraydouble[x][y] = value
                value += 1
        if i % 2 != 0:
            for j in range(0, i):
                y += 1
                arraydouble[x][y] = value
                value += 1
            for k in range(0, i):
                x += 1
                arraydouble[x][y] = value
                value += 1

        if i == dimension - 1:
            if x == 0:
                for j in range(dimension - 1):
                    y += 1
                    arraydouble[x][y] = value
                    value += 1
            elif x == i:
                for j in range(dimension - 1):
                    y -= 1
                    arraydouble[x][y] = value
                    value += 1

    array2Img(arraydouble, "one1.png")
    # print(arraydouble[X3 ][Y3-2])
    print(arraydouble)
    print(arraydouble.shape)


'''# centre
    #arraydouble[X3][Y3]= (255,255,255)
    arraydouble[X3][Y3 + 1] = (((arraydouble[X3][Y3] + arraydouble[X3][Y3 + 2])) + array1[X1][Y1]) / 3
    arraydouble[X3 -1 ][Y3+1] = ((arraydouble[X3-2][Y3]*0.25 +arraydouble[X3-2][Y3+2]*0.25+arraydouble[X3][Y3]*0.25+arraydouble[X3][Y3+2]*0.25)+ array1[X1][Y1]) / 2
    arraydouble[X3 - 1][Y3] = ((arraydouble[X3][Y3]*0.5 + arraydouble[X3 - 2][Y3]*0.50)  + array1[X1 - 1][Y1 ]) / 2
    arraydouble[X3 -1 ][Y3-1] = ((arraydouble[X3][Y3]*0.25 +arraydouble[X3][Y3-2]*0.25+arraydouble[X3-2][Y3-2]*0.25+arraydouble[X3-2][Y3]*0.25)+ (array1[X1][Y1]*0.5+array1[X1-1][Y1]*0.5)) / 2
    arraydouble[X3][Y3-1] = ((arraydouble[X3][Y3]*0.5 + arraydouble[X3 ][Y3-2]*0.5) + array1[X1 ][Y1 - 1]) / 2
    arraydouble[X3 + 1][Y3 - 1] = ((arraydouble[X3][Y3] * 0.25 + arraydouble[X3][Y3 - 2] * 0.25 + arraydouble[X3 + 2][Y3 - 2] * 0.25 + arraydouble[X3 + 2][Y3] * 0.25) + (array1[X1][Y1] * 0.5 + array1[X1 + 1][Y1-1] * 0.5)) / 2
    arraydouble[X3+1][Y3 ] = ((arraydouble[X3][Y3] * 0.5 + arraydouble[X3+2][Y3 ] * 0.5) + array1[X1+2][Y1 ]) / 2
    arraydouble[X3 + 1][Y3 + 1] = ((arraydouble[X3][Y3] * 0.25 + arraydouble[X3][Y3 + 2] * 0.25 + arraydouble[X3 + 2][Y3 + 2] * 0.25 + arraydouble[X3 + 2][Y3] * 0.25) + (array1[X1][Y1+1] * 0.5 + array1[X1 + 1][Y1] * 0.5)) / 2
    arraydouble[X3 + 1][Y3+2] = ((arraydouble[X3][Y3+2] * 0.5 + arraydouble[X3 + 2][Y3+2] * 0.5) + (array1[X1 ][Y1]*0.50 + array1[X1+2][Y1+2])) / 2
    arraydouble[X3 - 1][Y3 + 2] = ((arraydouble[X3-2][Y3 + 2] * 0.5 + arraydouble[X3 ][Y3 + 2] * 0.5) + (array1[X1-1][Y1+1] * 0.50 + array1[X1 ][Y1 + 1])) / 2
    arraydouble[X3 - 2][Y3 + 1] = ((arraydouble[X3 - 2][Y3 ] * 0.5 + arraydouble[X3-2][Y3 + 2] * 0.5) + (array1[X1 - 1][Y1 ] * 0.50 + array1[X1-1][Y1 + 1])) / 2
    arraydouble[X3 - 2][Y3 - 1] =  ((arraydouble[X3 - 2][Y3 - 2]*0.5 + arraydouble[X3 - 2][Y3 ]*0.5 + array1[X1-1][Y1-1])/2)
    arraydouble[X3 - 1][Y3 - 2] =  (((arraydouble[X3 - 2][Y3 - 2]*0.5 +arraydouble[X3 ][Y3 - 2]*0.5)+array1[X1-1][Y1-1]))/2
    arraydouble[X3 + 1][Y3 - 2] = (((arraydouble[X3][Y3 - 2] * 0.5 + arraydouble[X3+2][Y3 - 2] * 0.5) + array1[X1 ][Y1 - 1])) / 2
    arraydouble[X3 + 2][Y3 - 1] = (((arraydouble[X3+2][Y3] * 0.5 + arraydouble[X3+2][Y3 - 2] * 0.5) + array1[X1+1 ][Y1])) / 2
    arraydouble[X3 + 2][Y3 + 1] = (((arraydouble[X3 + 2][Y3] * 0.5 + arraydouble[X3 + 2][Y3 +2] * 0.5) + array1[X1 + 1][Y1])) / 2
    arraydouble[X3 + 2][Y3 + 3] = (((arraydouble[X3 + 2][Y3+4] * 0.5 + arraydouble[X3 + 2][Y3 +2] * 0.5) + array1[X1 + 1][Y1+1])) / 2
    arraydouble[X3 + 1][Y3 + 3]  = (((arraydouble[X3 ][Y3+2] * 0.25 + arraydouble[X3 ][Y3+4]  * 0.25 + arraydouble[X3 +2 ][Y3+2]*0.25 + arraydouble[X3 +2 ][Y3+4]*0.25 ) + array1[X1 + 2][Y1+1])) / 2
    arraydouble[X3 ][Y3 + 3] =  (((arraydouble[X3 ][Y3+4] * 0.5 + arraydouble[X3 ][Y3 +2] * 0.5) + array1[X1 + 1][Y1+1])) / 2
    arraydouble[X3-1][Y3 + 3] = (((arraydouble[X3 -2 ][Y3+2] * 0.25 + arraydouble[X3 -2][Y3+4]  * 0.25 + arraydouble[X3  ][Y3+2]*0.25 + arraydouble[X3 ][Y3+4]*0.25 ) + array1[X1][Y1+1]*0.25+ array1[X1][Y1+2]*0.25+ array1[X1-1][Y1+1]*0.25+ array1[X1-1][Y1+2]*0.25)) / 2
    arraydouble[X3-2][Y3 + 3] = (((arraydouble[X3-2][Y3 + 2] * 0.5 + arraydouble[X3-2][Y3 + 4] * 0.5) + array1[X1 -1][Y1 + 1])) / 2
    arraydouble[X3 - 3][Y3 + 3]= (((arraydouble[X3 -4 ][Y3+2] * 0.25 + arraydouble[X3 -4][Y3+4]  * 0.25 + arraydouble[X3-  2][Y3+2]*0.25 + arraydouble[X3-2 ][Y3+4]*0.25 ) +
                                   array1[X1-1][Y1+1]*0.25+ array1[X1-1][Y1+2]*0.25+ array1[X1-2][Y1+1]*0.25+ array1[X1-2][Y1+2]*0.25)) / 2

    arraydouble[X3 - 3][Y3 + 2]= (((arraydouble[X3-4][Y3 + 2] * 0.5 + arraydouble[X3-2][Y3 + 2] * 0.5) + array1[X1 -1][Y1 + 1])) / 2
    arraydouble[X3 - 3][Y3 + 1]= (((arraydouble[X3 -2 ][Y3+2] * 0.25 + arraydouble[X3 -2][Y3]  * 0.25 + arraydouble[X3-  4][Y3+2]*0.25 + arraydouble[X3-4 ][Y3]*0.25 ) +
                                   array1[X1-1][Y1]*0.25+ array1[X1-1][Y1+1]*0.25+ array1[X1-2][Y1]*0.25+ array1[X1-1][Y1+1]*0.25)) / 2'''