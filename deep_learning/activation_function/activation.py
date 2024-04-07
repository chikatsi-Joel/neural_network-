#__________Gradi Joel Piedjou________________#


import math
from enum import Enum
import numpy as np


class Activation(Enum) :

    SIGMOID = 1
    RELU = 2
    TANH = 3
    SOFTMAX = 4
    GELU = 5
    
    
    def apply(self, values : np.ndarray) -> np.ndarray | float:
        if self.name == 'SIGMOID' :
            return 1 / (1 + np.exp( -values))
        
        elif self.name == 'RELU' :
            return np.maximum(values, 0)
        
        elif self.name == 'TANH' :
            return (np.exp(values) - np.exp(-values)) / (np.exp(values) + np.exp( - values))
        
        else :
            return np.exp(values) / np.sum(np.exp(values))
        

    def calcul_derivate(self, values : np.ndarray) -> np.ndarray :
        if self.name == 'SIGMOID' :
            return Activation.SIGMOID.apply(values) * (1 - Activation.SIGMOID.apply(values))
        
        elif self.name == 'RELU' :
            values[values > 0] = 1
            values[values <= 0] = 0
            return values
        
        elif self.name == 'TANH' :
            return (np.exp(values) - np.exp(-values)) / (np.exp(values) + np.exp( - values))
        
        else :
            return np.exp(values) / np.sum(np.exp(values))