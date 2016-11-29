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
        __matrix__ = self.data
        for i in xrange(power-1):
            print 'iteration:', i
            __matrix__ = np.dot(__matrix__, self.original)
            __matrix__ = np.power(__matrix__, inflation)
            __matrix__ = normalize(__matrix__, norm='l1', axis=0)
            # if np.allclose(prev, __matrix__, rtol=1):
            #     break
            print __matrix__
        return __matrix__

    def fit_transform(self, data, power=5, inflation=2):
        self.fit(data)
        return self.transform(power, inflation)

# filename = 'attweb_net'
# filename = 'physics_collaboration_net'
filename = 'yeast_undirected_metabolic'
# filename = 'sample'

mcl = MarkovClustering()
data, key_map = load_data('data/' + filename + '.txt')
print data
matrix = mcl.fit_transform(data, power=1000)
matrix[matrix < .9] = 0
print matrix
# print_ndarray(matrix)
to_clu(open('output/' + filename + '.clu', 'w'), matrix, key_map)
