#__________Gradi Joel Piedjou________________#


import math
import numpy as np
from enum import Enum
from ..layers import Dense, Dense
from ..abstract_layers.abstract_layers import abstract_layers


class l1_normalisation (abstract_layers):
    def __init__(self, rate : float = 0.01) :
        self.rate = rate

    def __call__(self, layer : Dense, biais_also : bool = False) -> Dense:

        self.shape = layer.shape[0]
        
        layer.weights *= self.rate
        layer.biais *= self.rate if biais_also else 1

        return layer
    
    def get_params(self):
        return self.__dict__
    
    def get_shape_correspondance(self) :
        return self.shape
    
