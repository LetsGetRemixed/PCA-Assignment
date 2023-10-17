import os
import sys

# Get the absolute path of the script's directory
current_directory = os.path.abspath(os.path.dirname(__file__))

# Get the parent directory
parent_directory = os.path.dirname(current_directory)

# Add the parent directory to sys.path
sys.path.append(parent_directory)

import cv2
import numpy as np
import matplotlib.pyplot as plt
import pytest

from get_eigenvectors import get_eigenvectors
from pca_detect_digit import pca_detect_digit
from draw_rectangle import draw_rectangle

def setup_module(module):
    module.data_file_path = os.path.join(parent_directory, 'data', 'mnist_data.csv')
    module.output_dir = os.path.join(parent_directory, 'output')
    module.test_data_dir = os.path.join(parent_directory, 'data', 'test_data')
    module.test_data_files = os.listdir(module.test_data_dir)


def test_get_eigenvectors():
    """
    Test function for the get_eigenvectors function.

    Reads in data from data_file_path for a specific digit, calculates the mean vector and top 5 eigenvectors,
    and saves the mean vector and top 5 eigenvectors as 28x28 images in the output folder using cv2.imwrite.
    """
    digit = 2
    mean_vector, eigenvectors = get_eigenvectors(data_file_path, digit)

    # Check the shape of the mean vector
    assert mean_vector.shape == (784,)

    # Check the shape of the eigenvectors
    assert eigenvectors.shape == (784, 784)

    # Save the mean vector and top 5 eigenvectors as 28x28 images in the output folder using cv2.imwrite
    mean_vector_scaled = cv2.normalize(mean_vector, None, 0, 255, cv2.NORM_MINMAX)
    cv2.imwrite(os.path.join(output_dir, 'mean_vector.png'), mean_vector_scaled.reshape(28, 28))

    for i in range(5):
        eigenvector = eigenvectors[:, i]
        eigenvector_scaled = cv2.normalize(eigenvector, None, 0, 255, cv2.NORM_MINMAX)
        cv2.imwrite(os.path.join(output_dir, 'eigenvector_' + str(i) + '.png'), eigenvector_scaled.reshape(28, 28))


def test_pca_detect_digit():
    """
    Test function for PCA digit detection.

    This function tests the PCA digit detection algorithm by detecting the digit in each image in the test data folder
    and saving the image with the detection rectangle in the output folder.

    Note: No automatic tests are performed on the output images. You should visually inspect the output images to make sure
    that the detection algorithm is working correctly.
    """
    digit = 2
    mean_vector, eigenvectors = get_eigenvectors(data_file_path, digit)
    mean_digit = mean_vector.reshape(28, 28)

    # Detect the digit in each image and save the image with the detection rectangle in the output folder
    for test_data_file in test_data_files:
        image = cv2.imread(os.path.join(test_data_dir, test_data_file), cv2.IMREAD_GRAYSCALE)
        N = 10  # Number of eigenvectors to use
        detection_center = pca_detect_digit(image, mean_digit, eigenvectors, N)
        image_with_rectangle = draw_rectangle(image, detection_center[0]-14, detection_center[0]+14, detection_center[1]-14, detection_center[1]+14)
        cv2.imwrite(os.path.join(output_dir, test_data_file), image_with_rectangle)
