import numpy as np

N = 10
array = np.array(N)
array = np.zeros(N)
array = np.empty(N)

logical = array > 5 # array of True and False
logical_elems = array[logical] # Elements satisfying logical

