from matplotlib import axis
import pprint
import numpy as np

def calculate(list):
    converted_list = np.array(list).reshape(3,3)

    calculations = {
        'mean': [converted_list.mean(axis=0).tolist(), converted_list.mean(axis=1).tolist(), converted_list.mean()],
        'variance': [converted_list.var(axis=0).tolist(), converted_list.var(axis=1).tolist(), converted_list.var()],
        'standard deviation': [converted_list.std(axis=0).tolist(), converted_list.std(axis=1).tolist(), converted_list.std()],
        'max': [converted_list.max(axis=0).tolist(), converted_list.max(axis=1).tolist(), converted_list.max()],
        'min': [converted_list.min(axis=0).tolist(), converted_list.min(axis=1).tolist(), converted_list.min()],
        'sum': [converted_list.sum(axis=0).tolist(), converted_list.sum(axis=1).tolist(), converted_list.sum()]
    }

    return calculations

pprint.pprint(calculate([0,1,2,3,4,5,6,7,8]))