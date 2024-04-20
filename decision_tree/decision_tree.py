import numpy as np


class decision_tree() :
    def __init__(self, data_set : list[np.ndarray], labels : list[int | str]) -> None:
        self.data_set = data_set
        self.label = labels