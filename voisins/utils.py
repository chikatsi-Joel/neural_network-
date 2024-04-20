import numpy as np


def distance_evaluate(inputs_1 : np.ndarray, inputs_2 : np.ndarray) -> float :
    return np.sqrt(np.sum(np.power(inputs_1 - inputs_2, 2)))


def vote(list_values : list, value) :
    pass