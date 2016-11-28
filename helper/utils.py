import numpy as np
from sklearn.preprocessing import normalize
import operator
import math
# np.set_printoptions(threshold=np.inf)


def is_int(s):
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

    if not int_flag:
        array = list()
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
    return Matrix(normalize(matrix, norm='l1', axis=0))


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


def to_clu(handle, matrix):



    output = ''
    mapping = dict()
    shape = matrix.shape[0]
    output += '*vertices ' + str(shape) + "\n"
    for i in xrange(shape):
        for j in xrange(shape):
            # if i == j:
            #     continue
            element = matrix[i,j]
            if j not in mapping.keys():
                mapping[j] = dict()
            if element > 0:
                mapping[j][i] = element
            else:
                mapping[j][j] = 0
    for k, v in mapping.items():
        output += str(sorted(mapping[k].items(), key=operator.itemgetter(1), reverse=True)[0][0]) + "\n"
        mapping[k] = sorted(mapping[k].items(), key=operator.itemgetter(1), reverse=True)[0]
    # print output
    print mapping
    handle.write(output)
    handle.close()


def print_ndarray(ndarray):
    for row in ndarray:
        print '[',
        for element in row:
            print "%.5f" % element, ",\t",
        print ']'
