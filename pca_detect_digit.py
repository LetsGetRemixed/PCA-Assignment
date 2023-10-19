import numpy as np
import cv2
import matplotlib.pyplot as plt


def pca_detect_digit(image, mean_digit, eigenvectors, N):
    
    # YOUR CODE HERE
    image_height, image_width = image.shape
    template_size = 28

    best_match_error = None
    best_match_position = None

    # Loop through tha windows
    for row in range(image_height - template_size + 1):
        for col in range(image_width - template_size + 1):
            # extract
            subwindow = image[row:row+template_size, col:col+template_size]

            # switch to float 64
            subwindow = subwindow.astype(np.float64)

            # zero mean
            subwindow -= np.mean(subwindow)

            # top N eigens
            projection = np.dot(subwindow.reshape(-1), eigenvectors[:, :N])

            # reconstruction era frfr
            reconstructed_subwindow = np.dot(projection, eigenvectors[:, :N].T)

            # Calculamination homie
            reconstruction_error = np.sum((subwindow - reconstructed_subwindow.reshape(template_size, template_size)) ** 2)

            # If low error change 
            if best_match_error is None or reconstruction_error < best_match_error:
                best_match_error = reconstruction_error
                best_match_position = (row + template_size // 2, col + template_size // 2)

    detection_center = np.array(best_match_position)
    return detection_center
