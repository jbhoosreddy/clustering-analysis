from helper.utils import load_data
from helper.utils import to_clu
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

    def transform(self, power, inflation):
        matrix = self.data
        for i in xrange(power-1):
            matrix = np.dot(matrix, self.original)
            matrix = np.power(matrix, inflation)
            matrix = normalize(matrix, norm='l1', axis=0)
            # if np.allclose(prev, matrix, rtol=1):
            #     break
        return matrix

    def fit_transform(self, data, power=5, inflation=2):
        self.fit(data)
        return self.transform(power, inflation)

filename = 'yeast_undirected_metabolic'
# filename = 'sample'

mcl = MarkovClustering()
data = load_data('data/' + filename + '.txt')
matrix = mcl.fit_transform(data, power=10)
matrix[matrix < .5] = 0
print matrix
to_clu(open('output/' + filename + '.clu', 'w'), matrix)