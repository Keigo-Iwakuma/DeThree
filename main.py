import numpy as np
from dethree import Variable
import dethree.functions as F
from dethree.utils import plot_dot_graph


if __name__ == "__main__":
    x0 = Variable(np.array([[1,2,3,]]))
    x1 = Variable(np.array([10]))
    y = x0 + x1
    print(y)

    y.backward()
    print(x1.grad)