import numpy as np

def sum_array_module(array):
    """Returns the sum of the elements in a numpy array"""
    result = 0
    for element in array.flatten():
        result+=element
    return result