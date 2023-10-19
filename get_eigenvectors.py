import numpy as np
import cv2

def get_eigenvectors(data_file_path, digit):
    
    # YOUR CODE HERE
    digit_pixels = []

    # readin dat data
    with open(data_file_path, 'r') as file:
        for line in file:
            row = line.strip().split(',')
            label = int(row[0])
            if label == digit:
                pixel_values = np.array(list(map(int, row[1:])))
                digit_pixels.append(pixel_values)

    # list of pixels to array
    digit_pixels = np.array(digit_pixels)

    # mean vector
    mean_vector = np.mean(digit_pixels, axis=0)

    # covariance matrix
    cov_matrix = np.cov(digit_pixels, rowvar=False)

    # eigen values
    eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)

    # sort them values cuzzo
    sorted_indices = np.argsort(eigenvalues)[::-1]
    eigenvectors = eigenvectors[:, sorted_indices]

    return mean_vector, eigenvectors
