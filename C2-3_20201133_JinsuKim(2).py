import numpy as np

x=([1,1])
y=([2,2])

def naive_vector_dot(x,y):
    assert len(x.shape) == 1
    assert len(y.shape) == 1
    assert x.shape[0] == y.shape[0]
    z=0
    for i in range(x.shape[0]):
        z+= x[i] * y[i]
    return z
