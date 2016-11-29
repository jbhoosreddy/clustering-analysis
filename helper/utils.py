import numpy as np
from sklearn.preprocessing import normalize
import operator
import math
# np.set_printoptions(threshold=np.inf)


def is_int(s):
    return False
    try:
        int(s)
        return True
    except ValueError:
        return False


def load_data(file_name):
    file = open(file_name)
    data = file.read().replace("\r", "").split("\n")
    if "\t" in data[0]:
        data = map(lambda d: d.split("\t"), data)
    else:
        data = map(lambda d: d.split(" "), data)
    file.close()
    nodes = set()

    for tokens in data:
        int_flag = False
        if is_int(tokens[0]):
            int_flag = True
        break
    array = list()
    if not int_flag:
        new_data = list()
        for tokens in data:
            if tokens[0] not in array:
                array.append(tokens[0])
            if tokens[1] not in array:
                array.append(tokens[1])
            new_data.append([array.index(tokens[0]), array.index(tokens[1])])
        data = new_data
    for tokens in data:
        nodes.add(int(tokens[0]))
        nodes.add(int(tokens[1]))
    size = max(nodes) + 1
    matrix = np.eye(size, dtype=np.float64)
    for tokens in data:
        tokens = int(tokens[0]), int(tokens[1])
        matrix.itemset((tokens[0], tokens[1]), 1)
        matrix.itemset((tokens[1], tokens[0]), 1)
    # print matrix
    return Matrix(normalize(matrix, norm='l1', axis=0)), array


def print_list(l, c=None, should_print=True):
    output = ""
    for i in l:
        if should_print:
            print i
        output += str(i)+"\n"
        if c:
            c -= 1
            if not c:
                break
    return output


def print_dict(d, c=None, should_print=True):
    output = ""
    for k,v in d.items():
        if should_print:
            print k,v
        output += str(k)+": "+str(v)+"\n"
        if c:
            c -= 1
            if not c:
                break
    return output


class Matrix(np.ndarray):

    def __new__(cls, *args, **kwargs):
        return np.asarray(args[0]).view(cls)


def to_clu(handle, matrix, key_map):
    vertices = set(xrange(len(key_map)))
    cluster = 1
    seen = list()
    mapping = dict()
    output = ''
    size = matrix.shape[0]
    output += '*vertices ' + str(size) + "\n"
    for row in matrix:
        empty_row = True
        for index, element in enumerate(row):
            if element > 0:
                if index not in seen:
                    empty_row = False
                    seen.append(index)
                    mapping[index + 1] = cluster
        if len(seen) == size:
            break
        if not empty_row:
            cluster += 1
    unseen = vertices - set(seen)
    for element in unseen:
        mapping[element + 1] = cluster
    output += "\n".join(map(lambda m: str(m), mapping.values()))
    handle.write(output)
    handle.close()


def print_ndarray(ndarray):
    for row in ndarray:
        print '[',
        for element in row:
            print "%.5f" % element, ",\t",
        print ']'
