# -*- coding: utf-8 -*-
"""
% This function that you will implement is intended to behave like the built-in function 
% imfilter() in Matlab or equivalently the same function implemented as part of scipy.misc module
% in Python. You will implement imfilter from first principles, i.e., without using 
% any library functions. 

% See 'help imfilter' or 'help conv2'. While terms like "filtering" and
% "convolution" might be used interchangeably, we will essentially perform 2D correlation 
% between the filter and image. Referring to 'proj1_test_filtering.py' would help you with
% your implementation. 
  
% Your function should work for color images. Simply filter each color
% channel independently.

% Your function should work for filters of any width and height
% combination, as long as the width and height are odd (e.g. 1, 7, 9). This
% restriction makes it unambigious which pixel in the filter is the center
% pixel.

% Boundary handling can be tricky. The filter can't be centered on pixels
% at the image boundary without parts of the filter being out of bounds. If
% you look at 'help conv2' and 'help imfilter' in Matlab, you see that they have
% several options to deal with boundaries. You should simply recreate the
% default behavior of imfilter -- pad the input image with zeros, and
% return a filtered image which matches the input resolution. A better
% approach would be to mirror the image content over the boundaries for padding.

% % Uncomment if you want to simply call library imfilter so you can see the desired
% % behavior. When you write your actual solution, **you can't use imfilter,
% % correlate, convolve commands, but implement the same using matrix manipulations**. 
% % Simply loop over all the pixels and do the actual
% % computation. It might be slow.
"""


from scipy.misc import imfilter
import numpy as np
""" Exemplar Gaussian 3x3 filter shown below-- see filters defined in proj1_test_filtering.py """
#filter = #np.asarray([[0.1019,0.1154,0.1019],[0.1154,0.1308,0.1154],[0.1019,0.1154,0.1019]],\
         #           dtype=np.float32) 

#def my_imfilter(image,filter):  #which will work identically to the function below
#  output = imfilter(image, filter) #replace your code here

def my_imfilter(image, imfilter):

    num_of_channels = len(image[0][0]) 	# Number of channels 1 for grey scale and 3 for RGB

    output_img = np.zeros((image.shape[0], image.shape[1], num_of_channels))

    padded_img = np.zeros((image.shape[0] + imfilter.shape[0]-1, image.shape[1] + imfilter.shape[1]-1, num_of_channels))

    # Padding image
    padded_img[int((imfilter.shape[0]-1)/2) : image.shape[0]+int((imfilter.shape[0]-1)/2), int((imfilter.shape[1]-1)/2) : image.shape[1] + int((imfilter.shape[1]-1)/2)] = image

    for k in range(num_of_channels):
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                output_img[i][j][k] = np.sum(np.multiply(padded_img[i:i+imfilter.shape[0], j:j+imfilter.shape[1], k], imfilter))
    return output_img
