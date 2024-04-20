#__________Gradi Joel Piedjou________________#


import math
import numpy as np
from enum import Enum


class Loss_function(Enum) :
    LOG_LOSS = 1
    ENTROPIE = 2
    MSE = 3


    def calculate(self, fake_ouputs : np.ndarray, real_ouputs : np.ndarray) :
        if self.name == 'LOG_LOSS' :
            pass
        elif self.name == "ENTROPIE" :
            pass
        
        elif self.name == "MSE" :
            return np.sum(np.power(real_ouputs - fake_ouputs, 2)) / len(fake_ouputs)
        
 
    def calculate_derivate(self, fake_ouputs : np.ndarray, real_ouputs : np.ndarray) :
        if self.name == "ENTROPIE" :
            pass

        elif self.name == "LOG_LOSS" :
            pass

        elif self.name == "MSE" :
            return 2 * np.sum(real_ouputs - fake_ouputs) / len(fake_ouputs)
        