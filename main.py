
"""
    Author : Gradi Joel Chikatsi
    date : 27 mars 2024
    
    motifs : Dans le cardre de la recherche et du support d'aide.

    description : 

    ce projet est entièrement libre et rigoureusement developpé
    suivant l'approche de l'API keras qui interface Tensorflow. Il est à noter que les 
    fonctions de pertes utilisés dans ce programme ne sont pas complète.

"""


from deep_learning import layers, neural_network
from deep_learning.normalisation import l1_normalisation
from deep_learning.activation_function import activation
from deep_learning.loss_function import loss_function
from deep_learning.dataset import dataset
import numpy as np



x_values, real_ouputs, _ = dataset.make_data_set_load_iris()
x_values, real_ouputs = np.array(x_values[0]), np.array(real_ouputs[0])

layer = layers.Dense(32, activation.Activation.RELU, (True, 1e-6))
layer_2 = layers.Dense(100, activation.Activation.RELU, (True, 1e-6))
layer_3 = layers.Dense(3, activation.Activation.SOFTMAX)

neural = neural_network.Neural_network(x_values.shape[0], [layer, layer_2], loss_function.Loss_function.MSE)
neural.add_layers(layer_3)
neural.compile()

parameters_train = {
    "x_values" : x_values,
    "y_values" : real_ouputs,
    "num_iter" : 10,
    "learning_rate" : 0.001,
    "shuffle" : True
}
"""x_values = np.concatenate((x_values, x_values, x_values, x_values, x_values), axis= 0)
print(x_values.shape)"""

print(neural.forward_propagation(x_values))