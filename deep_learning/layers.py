from .activation_function.activation import Activation
from .loss_function.loss_function import Loss_function
from .abstract_layers.abstract_layers import abstract_layers
import numpy as np

class Dense(abstract_layers) :
    def __init__(
        self, 
        nbre_neurones : int,
        activation : Activation,
        drop_out : tuple[bool, float] = (False, 1)
    ) :
        super(Dense, self).__init__()

        self.nbre_neurones = nbre_neurones
        self.activation = activation

        self.weights : np.ndarray = None
        self.memory : dict[str, np.ndarray] = {}
        self.biais = np.random.rand(1, self.nbre_neurones)
        self.drop_out = drop_out


    def compute(self, feature_shape : int) :
        self.weights = np.random.uniform(-0.1, 0.1 , (self.nbre_neurones, feature_shape))

    def __call__(self, inputs : np.ndarray) :

        self.weights *=  self.drop_out[1] if self.drop_out[0] else 0.9

        self.memory['z'] = (inputs @ self.weights.T) + self.biais

        self.memory['o'] = self.activation.apply(self.memory['z'])

        return self.memory['o']
    
    def forward(self, inputs : abstract_layers | np.ndarray) -> np.ndarray:

        if type(inputs) == np.ndarray :
            self.weights = np.random.uniform(-0.1, 0.1 , (self.nbre_neurones, inputs.shape[0]))

        self.weights *=  self.drop_out[1] if self.drop_out[0] else 0.9

        self.memory['z'] = (inputs @ self.weights.T) + self.biais

        self.memory['o'] = self.activation.apply(self.memory['z'])

        return self.memory['o']
    
     
    
    def backward(self, activation_output_prev : np.ndarray, real_ouputs : np.ndarray) :
        pass
    
    def get_params(self):
        return super().get_params()
    


