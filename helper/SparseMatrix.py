import pickle

from helper.utils import print_dict


class SparseMatrix(object):

    def __init__(self, data=None):
        self.data = data
        self.matrix = dict()
        if self.data is not None:
            self.create_matrix()

    def size(self):
        return len(self.points)

    def get(self, i, j):
        if i == j:
            return 1
        if (i,j) in self.matrix.keys():
            return self.matrix[(i,j)]
        return 0

    def set(self, i, j, value):
        self.matrix[(i,j)] = value

    def save(self, filename):
        handle = open('output/'+filename+".pickle", 'w')
        pickle.dump(self, handle)
        handle.close()

    def __repr__(self):
        matrix = self.matrix
        return print_dict(matrix, None, False)

    def __str__(self):
        matrix = self.matrix
        return print_dict(matrix, None, False)