import os
import sys

# Get the absolute path of the script's directory
current_directory = os.path.abspath(os.path.dirname(__file__))
# Get the parent directory
parent_directory = os.path.dirname(current_directory)
# Add the parent directory to sys.path
sys.path.append(parent_directory)

import numpy as np
import cv2
import matplotlib.pyplot as plt
from get_eigenvectors import get_eigenvectors
from pca_detect_digit import pca_detect_digit
from draw_rectangle import draw_rectangle

def main():
    data_file_path = os.path.join(current_directory, 'data', 'mnist_data.csv')
    output_dir = os.path.join(current_directory, 'output')
    test_data_dir = os.path.join(current_directory, 'data', 'test_data')
    test_data_files = os.listdir(test_data_dir)

    ########### Task 1: Get the mean vector and top 5 eigenvectors for digit 2
    digit = 2
    mean_vector, eigenvectors = get_eigenvectors(data_file_path, digit)

    # Save the mean vector and top 5 eigenvectors as 28x28 images in the output folder using cv2.imwrite
    mean_vector_scaled = cv2.normalize(mean_vector, None, 0, 255, cv2.NORM_MINMAX)
    cv2.imwrite(os.path.join(output_dir, 'mean_vector.png'), mean_vector_scaled.reshape(28, 28))

    for i in range(5):
        eigenvector = eigenvectors[:, i]
        eigenvector_scaled = cv2.normalize(eigenvector, None, 0, 255, cv2.NORM_MINMAX)
        cv2.imwrite(os.path.join(output_dir, 'eigenvector_' + str(i) + '.png'), eigenvector_scaled.reshape(28, 28))


    ############ Task 2: For each image file in the data/test_data folder, 
    # detect the digit in the image using the PCA-based method
    mean_digit = mean_vector.reshape(28, 28)

    # Detect the digit in each image
    for test_data_file in test_data_files:
        image = cv2.imread(os.path.join(test_data_dir, test_data_file), cv2.IMREAD_GRAYSCALE)
        N = 10  # Number of eigenvectors to use
        detection_center = pca_detect_digit(image, mean_digit, eigenvectors, N)
        image_with_rectangle = draw_rectangle(image, detection_center[0]-14, detection_center[0]+14, detection_center[1]-14, detection_center[1]+14)
        cv2.imwrite(os.path.join(output_dir, test_data_file), image_with_rectangle)

if __name__ == '__main__':
    main()