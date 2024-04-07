#__________Gradi Joel Piedjou________________#

from functools import singledispatchmethod
import numpy as np
import random
from .layers import Dense
from .abstract_layers.abstract_layers import abstract_layers
from  .loss_function.loss_function import Loss_function


class Neural_network() :

    @singledispatchmethod
    def __init__( self, nbre_features : tuple[int], list_layers : list[Dense], loss_function : Loss_function ) :
        """
            list_layers :  list[abstract_layers]
            loss_function : Loss_function
        """
        self.list_layers = list_layers
        self.__loss_function = loss_function
        self.inputs_shape = nbre_features

    

    @property
    def loss_function(self) -> Loss_function:
        return self.__loss_function

    
    @loss_function.setter
    def loss_function(self, loss_func : Loss_function) -> None :
        self.__loss_function = loss_func


    def add_layers(self, layer : abstract_layers) :
        self.list_layers.append(layer)

    def loss_apply(self, forward_result : np.ndarray, real_result : np.ndarray) -> np.ndarray:
        return self.loss_function.calculate(real_result, forward_result)
    
    def compile(self) :
        self.list_layers[0].compute(self.inputs_shape)

        for i in range(1, len(self.list_layers)) :
            self.list_layers[i].compute(self.list_layers[i - 1].weights.shape[0])
        
    def forward_propagation(self, inputs : np.ndarray) -> np.ndarray :

        for layer in self.list_layers :
            inputs = layer(inputs)
            
        return inputs
    
    def backpropagation(self, inputs : np.ndarray, real_ouputs : np.ndarray, learning_rate : float) :
        fake_ouputs = self.forward_propagation(inputs)
        layer_ouput = self.list_layers[-1]

        print(fake_ouputs)
        print(layer_ouput.activation.calcul_derivate(fake_ouputs))

        gradient = (real_ouputs - fake_ouputs) * layer_ouput.activation.calcul_derivate(fake_ouputs) * inputs 
        
        return gradient
        

    
        
    def fit(
        self,
        x_values : list,
        y_values : list,
        num_iter : int,
        learning_rate : float = 1e-6,
        shuffle : bool = False
    ) :
        
        datas = list(zip(x_values, y_values))

        if shuffle :
            random.shuffle(datas)

        x_values, y_values = zip(*datas)

        x_values = np.array(x_values)
        y_values = np.array(y_values)


        for i in range(num_iter) :
            for inputs, real_ouputs in zip(x_values, y_values) :
                loss = self.backpropagation(inputs, real_ouputs, learning_rate)
                print(f"loss : {loss} \n")


