import numpy as np


class features() :
    def __init__(self, values : np.ndarray, label : int | str) :
        self.values = values
        self.label = label

    def __str__(self) :
        return f" [Label : {self.label}  Values : {self.values} ]"
    

    def __repr__(self) :
        return f" [Label : {self.label}  Values : {self.values} ]\n"