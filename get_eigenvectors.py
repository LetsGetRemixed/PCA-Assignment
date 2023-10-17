import numpy as np
import cv2

def get_eigenvectors(data_file_path, digit):
    """
    Computes the mean vector and eigenvectors of the covariance matrix of a given digit in a dataset.

    Args:
        data_file_path (str): The path to the dataset file.
        digit (int): The digit to extract from the dataset.

    Returns:
        tuple: A tuple containing the mean vector and eigenvectors of the covariance matrix.
    """
    
    # YOUR CODE HERE

    return mean_vector, eigenvectors