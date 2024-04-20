
"""
    Author : Gradi Joel Chikatsi
    date : 27 mars 2024
    
    motifs : Dans le cardre de la recherche et du support d'aide.

    description : 

    ce projet est entièrement libre et rigoureusement developpé
    suivant l'approche de l'API keras qui interface Tensorflow. Il est à noter que les 
    fonctions de pertes utilisés dans ce programme ne sont pas complète.

"""
""

from deep_learning import layers, neural_network
from deep_learning.normalisation import l1_normalisation
from deep_learning.activation_function import activation
from deep_learning.loss_function import loss_function
from deep_learning.dataset import dataset
import numpy as np
from voisins.knn import KNN



data_train, data_label = dataset.make_data_set_load_iris()[:-1]
x_train, x_label = data_train[:100], data_label[:100]
x_test, test_label = data_train[100:], data_label[100:]
model = KNN(x_train, x_label)
print("Accuracy : ",model.test_(x_test, test_label), "%")