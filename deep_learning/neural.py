
import numpy as np
import math
from enum import Enum
from .activation_function import activation 




class neural(object) :
    def __init__(self, biais : float | None = None, weights : list[float] | None = None) :
        self.__biais = biais
        self.__weigths = np.array(weights, dtype = np.float32)

    @property
    def biais(self) :
        return self.__biais
    
    @property
    def weights(self) :
        return self.__weigths
    
    @biais.setter
    def biais(self, biais : float) :
        self.biais = biais

    @weights.setter
    def weights(self, weights : list[float]) :
        self.__weigths = np.array(weights, dtype = np.float32)

    def forward(self, inputs : list[float] | np.ndarray) -> float :
        if type(inputs) == list :
            inputs = np.array(inputs)

        if self.weights.shape != inputs.shape :
            raise AttributeError("attributs non pertinent")
        
        return activation.Activation.SIGMOID.apply(self.__weigths @ inputs.T + self.__biais)
    
