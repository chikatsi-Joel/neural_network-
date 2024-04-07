
import numpy as np
from sklearn.datasets import load_iris
import pandas as pd
import random


def make_data_set_load_iris() -> tuple[list]:
    """
        Le dataset est sous la forme  :
            output : x_values, real_ouputs, target_name
    """ 
    iris_data_set = load_iris()

    data_set = list(zip(iris_data_set['data'].tolist(), iris_data_set['target'].tolist()))
    random.shuffle(data_set)

    target_names  = iris_data_set['target_names'].tolist()
    value, target = zip(*data_set)
    
    targ = []
    for val in target :
        targ.append([1 if i == val else 0 for i in range(3)])
    

    datas = {
        "value" : value,
        "target" : target 
    }

    data_frame = pd.DataFrame(data = datas, columns = ["value", "target"])

    length = len(value)
    train_size = 3*length // 4

    train_data = data_frame[:train_size]
    test_data = data_frame[train_size:]

    return value, targ, target_names


