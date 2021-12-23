import numpy as np
def Bold(source, val):
    GenArray = np.empty((source.shape[0], source.shape[1]), dtype=np.int)
    for i in range(0, source.shape[0] - val + 1):
        for j in range(0, source.shape[1] - val + 1):
            GenArray[i: i + val, j: j + val] = np.full((val, val), np.min(source[i: i + val, j: j + val]),dtype=np.int)
    return GenArray