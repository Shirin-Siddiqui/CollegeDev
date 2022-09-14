import numpy as np

def matrix(n, symbol):
    a = np.zeros((n,n),  dtype='U1')
    np.fill_diagonal(a, symbol)
    np.fill_diagonal(np.fliplr(a), symbol)
    a[:,0] = symbol
    a[:,n-1] = symbol
    print(a)

matrix(5, "*")