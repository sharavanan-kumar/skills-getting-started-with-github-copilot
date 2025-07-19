import numpy as np

def calculate_correlation(x, y):
    if len(set(x)) == 1 or len(set(y)) == 1:
        return np.nan
    return np.corrcoef(x, y)[0, 1]
