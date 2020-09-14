import numpy as np

def naive_vector_dot(x, y):
    assert len(x.shape) == 1
    assert len(y.shape) == 1
    assert x.shape[0] == y.shape[0]
    z = 0.
    for i in range(x.shape[0]):
        z += x[i] * y[i]
    print(z)
    return z
x=np.array([2,1])
y=np.array([2,1])

naive_vector_dot(x,y)
print(x.shape[0])


