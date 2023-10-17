import numpy as np
import cv2
import matplotlib.pyplot as plt


def pca_detect_digit(image, mean_digit, eigenvectors, N):
    """
    Detects the center of a digit in an image using PCA.

    Parameters:
    image (numpy.ndarray): The input image.
    mean_digit (numpy.ndarray): The mean digit image (28x28 array)
    eigenvectors (numpy.ndarray): The eigenvectors of the digit images.
    N (int): The number of eigenvectors to use.

    Returns:
    tuple: The center of the detected digit as a tuple of (row, column) coordinates.
    """
    
    # YOUR CODE HERE

    return detection_center
