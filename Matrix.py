import numpy as np

# Solution using Numpy 

def matrix(n, symbol):
    a = np.zeros((n,n),  dtype='U1') # Take the input in a Matrix Format
    np.fill_diagonal(a, symbol) # Fill the right diagonal of the Matrix
    np.fill_diagonal(np.fliplr(a), symbol) # Fill the left diagonal of the Matrix
    a[:,0] = symbol # Fill the first element of every row
    a[:,n-1] = symbol # Fill the last element of every row
    print((4*n)-5 , end="\n") # Calculation to print the number of symbols in the Matrix
    for i in a:
        print('\t'.join(map(str, i))) # Print the formatted and spaced elements of the 2D Matrix

#matrix(7, "*")

# Solution using complexity of O(n)

def matrixloop(n, symbol):
    a = np.zeros((n,n),  dtype='U1')
    if ( n% 2 == 0):
        print((4*n)-4 , end="\n")
    else:
        print((4*n)-5 , end="\n")
    for i in range (0, n):
        a[i][0] = a[i][n-1] = a[i][i] = a[i, (n-1)-i] = "*"
    for i in a:
        print('\t'.join(map(str, i))) # Print the formatted and spaced elements of the 2D Matrix


    
matrixloop(5, "*")