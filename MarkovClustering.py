from helper.utils import load_data
import numpy as np
from sklearn.preprocessing import normalize
from copy import deepcopy


class MarkovClustering(object):
    def __init__(self):
        self.data = None
        self.original = None
        return

    def fit(self, data):
        self.data = data
        self.original = deepcopy(data)

    def transform(self, power=8, inflation=2):
        matrix = self.data
        prev = deepcopy(matrix)
        for i in xrange(power-1):
            matrix = np.dot(matrix, self.original)
            matrix = np.power(matrix, inflation)
            matrix = normalize(matrix, norm='l1', axis=0)
            if np.allclose(prev, matrix, rtol=1):
                break
        return matrix

    def fit_transform(self, data, power=5, inflation=2):
        self.fit(data)
        return self.transform(power, inflation)

mcl = MarkovClustering()
data = load_data('data/physics_collaboration_net.txt')
matrix = mcl.fit_transform(data, power=700)
# matrix[matrix < .00001] = 0
print matrix
