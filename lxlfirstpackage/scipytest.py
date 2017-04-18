from scipy import linalg
import numpy as np

A = np.matrix([
    [1, 2, 3, 4],
    [1, 4, 9, 16],
    [1, 8, 27, 64],
    [1, 16, 81, 256]
])
p,l, u=linalg.lu(A)
b=linalg.inv(p)
print l*u
print p*A
print b