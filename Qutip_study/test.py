from qutip import *
import numpy as np
import matplotlib.pyplot as plt


print(Qobj())
print(Qobj([[1],[2],[3],[4],[5]]))
x = np.array([[1, 2, 3, 4, 5]])
print(Qobj(x))
r = np.random.rand(4, 4)
print(Qobj(r))