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
            prev = deepcopy(__matrix__)
            __matrix__ = np.dot(__matrix__, self.original)
            __matrix__ = np.power(__matrix__, inflation)
            __matrix__ = normalize(__matrix__, norm='l1', axis=0)
            if np.allclose(prev, __matrix__, rtol=1):
                break
        return __matrix__

    def fit_transform(self, data, power=5, inflation=2):
        self.fit(data)
        return self.transform(power, inflation)
