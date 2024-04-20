import numpy as np
from .utils import distance_evaluate
from .features import features

class KNN :
    def __init__(
        self,
        data_set : list[np.ndarray],
        labels : list[int | str]
    ) :
        self.dataset : list[features] = list(map(lambda x : features(x[0], x[1]), zip(data_set, labels)))
        self.k = 1

    def predicts(self, inputs : np.ndarray, k : int) :
        list_data = [(val, distance_evaluate(val.values, inputs)) for val in self.dataset]
        list_data = sorted(list_data, key = lambda x : x[1])
        list_data = list_data[:k]

        self.k = k
        return max(set(list_data), key = list_data.count)[0].label
    
    
    def test_(self, data_tests : list[np.ndarray], labels : list[np.ndarray]) :
        acc = 0
        ind = 1
        for (val, lab) in zip(data_tests, labels) :
            prd = self.predicts(val, self.k)
            acc += 1 if prd == lab else 0
            print(f"prediction {ind} : {prd.upper() if type(prd) == str else prd}  Real label  : {lab.upper() if type(lab) == str else lab}  resultat : {lab == prd}")

        return round(acc * 100 / len(data_tests), 2)
    
