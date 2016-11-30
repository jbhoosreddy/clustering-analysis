from MarkovClustering import *
from helper.utils import load_data
from helper.utils import to_clu

THRESHOLD = 0.9
POWER = 20
INFLATION = 2

filename = 'attweb_net'
# filename = 'physics_collaboration_net'
# filename = 'yeast_undirected_metabolic'
# filename = 'sample'

mcl = MarkovClustering()
data, key_map = load_data('data/' + filename + '.txt')
matrix = mcl.fit_transform(data, power=POWER, inflation=INFLATION)
matrix[matrix < THRESHOLD] = 0
to_clu(open('output/' + filename + '.clu', 'w'), matrix, key_map)
